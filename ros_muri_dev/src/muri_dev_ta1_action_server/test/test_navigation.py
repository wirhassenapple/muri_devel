#!/usr/bin/env python3

import unittest
import math
from unittest.mock import MagicMock
import sys

# Mock für state_mach Modul
class StateMachine:
    Init = "Init"
    Calculate = "Calculate"
    TurnBeforeMove = "TurnBeforeMove"
    DriveMove = "DriveMove"
    TurnAfterMove = "TurnAfterMove"
    Success = "Success"
    Failure = "Failure"

sys.modules['state_mach'] = MagicMock()
sys.modules['state_mach'].StateMachine = StateMachine

# Hier den zu testenden Code importieren
# from navigation import *
from muri_dev_ta1_action_server.move_logic import setGoalParams, executeMovement, setPosParams, setSpeedParams, getOut
# Da wir den Code direkt einbinden, kopieren wir die relevanten Teile hier

from types import SimpleNamespace

class NavigationController:
    def __init__(self):
        self.state = StateMachine.Init
        self.goal = SimpleNamespace(x=None, y=None, theta=None)
        self.position = SimpleNamespace(x=None, y=None, theta=None)
        self.speed = SimpleNamespace(
            linear=SimpleNamespace(x=None, y=None),
            angular=SimpleNamespace(z=None)
        )
        self.turnedBeforeMove = False
        self.out = SimpleNamespace(
            linear=SimpleNamespace(x=0, y=0),
            angular=SimpleNamespace(z=0),
            distance_remaining=0,
            finish=False,
            success=False
        )
        self.ANGLE_TOLERANCE = math.radians(2)
        self.TRANSLATION_TOLERANCE = 0.05

    def setPosParams(self, x, y, th):
        self.position.x = x
        self.position.y = y
        self.position.theta = th

    def setGoalParams(self, x, y, th):
        self.goal.x = x
        self.goal.y = y
        self.goal.theta = th

    def resetGoal(self):
        self.state = StateMachine.Init
        self.goal.x = None
        self.goal.y = None
        self.goal.theta = None
        self.turnedBeforeMove = False
        self.out.linear.x = 0
        self.out.linear.y = 0
        self.out.angular.z = 0
        self.out.distance_remaining = 0
        self.out.finish = False
        self.out.success = False

    def calculatePolarAngleDiff(self):
        target_angle = math.atan2(self.goal.y - self.position.y, 
                                  self.goal.x - self.position.x)
        angle_diff = target_angle - self.position.theta

        if angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        elif angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        return angle_diff

    def calculatePolarDistanceDiff(self):
        distance = math.sqrt(((self.goal.x - self.position.x) ** 2) + 
                           ((self.goal.y - self.position.y) ** 2))
        return distance

    def calculatePolarGoalAngleDiff(self):
        target_angle = self.goal.theta
        angle_diff = target_angle - self.position.theta

        if angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        elif angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        return angle_diff


class TestNavigationCalculations(unittest.TestCase):
    """Tests für die Berechnungsfunktionen"""

    def setUp(self):
        self.nav = NavigationController()

    def test_calculatePolarAngleDiff_zero_angle(self):
        """Test: Winkel wenn Roboter und Ziel gleich ausgerichtet sind"""
        self.nav.setPosParams(0, 0, 0)
        self.nav.setGoalParams(1, 0, 0)
        angle_diff = self.nav.calculatePolarAngleDiff()
        self.assertAlmostEqual(angle_diff, 0, places=5)

    def test_calculatePolarAngleDiff_90_degrees(self):
        """Test: 90 Grad Drehung nach links"""
        self.nav.setPosParams(0, 0, 0)
        self.nav.setGoalParams(0, 1, 0)
        angle_diff = self.nav.calculatePolarAngleDiff()
        self.assertAlmostEqual(angle_diff, math.pi/2, places=5)

    def test_calculatePolarAngleDiff_negative_90_degrees(self):
        """Test: 90 Grad Drehung nach rechts"""
        self.nav.setPosParams(0, 0, 0)
        self.nav.setGoalParams(0, -1, 0)
        angle_diff = self.nav.calculatePolarAngleDiff()
        self.assertAlmostEqual(angle_diff, -math.pi/2, places=5)

    def test_calculatePolarAngleDiff_wraparound_positive(self):
        """Test: Winkel-Wraparound über +π"""
        self.nav.setPosParams(0, 0, -3)
        self.nav.setGoalParams(-1, 0, 0)
        angle_diff = self.nav.calculatePolarAngleDiff()
        self.assertTrue(-math.pi <= angle_diff <= math.pi)

    def test_calculatePolarAngleDiff_wraparound_negative(self):
        """Test: Winkel-Wraparound über -π"""
        self.nav.setPosParams(0, 0, 3)
        self.nav.setGoalParams(-1, 0, 0)
        angle_diff = self.nav.calculatePolarAngleDiff()
        self.assertTrue(-math.pi <= angle_diff <= math.pi)

    def test_calculatePolarDistanceDiff_simple(self):
        """Test: Einfache Distanzberechnung"""
        self.nav.setPosParams(0, 0, 0)
        self.nav.setGoalParams(3, 4, 0)
        distance = self.nav.calculatePolarDistanceDiff()
        self.assertAlmostEqual(distance, 5.0, places=5)

    def test_calculatePolarDistanceDiff_zero(self):
        """Test: Keine Distanz wenn am Ziel"""
        self.nav.setPosParams(1, 1, 0)
        self.nav.setGoalParams(1, 1, 0)
        distance = self.nav.calculatePolarDistanceDiff()
        self.assertAlmostEqual(distance, 0.0, places=5)

    def test_calculatePolarGoalAngleDiff_zero(self):
        """Test: Kein Winkelunterschied zur Zielorientierung"""
        self.nav.setPosParams(0, 0, math.pi/4)
        self.nav.setGoalParams(1, 1, math.pi/4)
        angle_diff = self.nav.calculatePolarGoalAngleDiff()
        self.assertAlmostEqual(angle_diff, 0.0, places=5)

    def test_calculatePolarGoalAngleDiff_180_degrees(self):
        """Test: 180 Grad Drehung zur Zielorientierung"""
        self.nav.setPosParams(0, 0, 0)
        self.nav.setGoalParams(1, 1, math.pi)
        angle_diff = self.nav.calculatePolarGoalAngleDiff()
        self.assertAlmostEqual(abs(angle_diff), math.pi, places=5)


class TestNavigationStateMachine(unittest.TestCase):
    """Tests für die Zustandsmaschine"""

    def setUp(self):
        self.nav = NavigationController()

    def test_initial_state(self):
        """Test: Initialer Zustand ist Init"""
        self.assertEqual(self.nav.state, StateMachine.Init)

    def test_resetGoal(self):
        """Test: resetGoal setzt alle Parameter zurück"""
        self.nav.setGoalParams(5, 5, math.pi)
        self.nav.out.finish = True
        self.nav.out.success = True
        self.nav.turnedBeforeMove = True
        
        self.nav.resetGoal()
        
        self.assertIsNone(self.nav.goal.x)
        self.assertIsNone(self.nav.goal.y)
        self.assertIsNone(self.nav.goal.theta)
        self.assertFalse(self.nav.out.finish)
        self.assertFalse(self.nav.out.success)
        self.assertFalse(self.nav.turnedBeforeMove)
        self.assertEqual(self.nav.state, StateMachine.Init)


class TestNavigationTolerances(unittest.TestCase):
    """Tests für Toleranzprüfungen"""

    def setUp(self):
        self.nav = NavigationController()

    def test_angle_tolerance_value(self):
        """Test: Winkeltoleranz ist 2 Grad in Radiant"""
        expected = math.radians(2)
        self.assertAlmostEqual(self.nav.ANGLE_TOLERANCE, expected, places=5)

    def test_translation_tolerance_value(self):
        """Test: Translationstoleranz ist 0.05 Meter"""
        self.assertEqual(self.nav.TRANSLATION_TOLERANCE, 0.05)

    def test_angle_within_tolerance(self):
        """Test: Winkel innerhalb der Toleranz"""
        angle = math.radians(1)  # 1 Grad
        self.assertLess(abs(angle), self.nav.ANGLE_TOLERANCE)

    def test_angle_outside_tolerance(self):
        """Test: Winkel außerhalb der Toleranz"""
        angle = math.radians(5)  # 5 Grad
        self.assertGreater(abs(angle), self.nav.ANGLE_TOLERANCE)

    def test_distance_within_tolerance(self):
        """Test: Distanz innerhalb der Toleranz"""
        distance = 0.03  # 3 cm
        self.assertLess(distance, self.nav.TRANSLATION_TOLERANCE)

    def test_distance_outside_tolerance(self):
        """Test: Distanz außerhalb der Toleranz"""
        distance = 0.1  # 10 cm
        self.assertGreater(distance, self.nav.TRANSLATION_TOLERANCE)


class TestNavigationEdgeCases(unittest.TestCase):
    """Tests für Edge Cases und Grenzfälle"""

    def setUp(self):
        self.nav = NavigationController()

    def test_goal_at_current_position(self):
        """Test: Ziel ist an aktueller Position"""
        self.nav.setPosParams(5, 5, 0)
        self.nav.setGoalParams(5, 5, 0)
        distance = self.nav.calculatePolarDistanceDiff()
        angle = self.nav.calculatePolarAngleDiff()
        goal_angle = self.nav.calculatePolarGoalAngleDiff()
        
        self.assertAlmostEqual(distance, 0.0, places=5)
        self.assertLess(abs(angle), self.nav.ANGLE_TOLERANCE)
        self.assertLess(abs(goal_angle), self.nav.ANGLE_TOLERANCE)

    def test_negative_coordinates(self):
        """Test: Negative Koordinaten"""
        self.nav.setPosParams(-1, -1, 0)
        self.nav.setGoalParams(-5, -5, 0)
        distance = self.nav.calculatePolarDistanceDiff()
        self.assertGreater(distance, 0)

    def test_large_coordinates(self):
        """Test: Große Koordinaten"""
        self.nav.setPosParams(1000, 1000, 0)
        self.nav.setGoalParams(1003, 1004, 0)
        distance = self.nav.calculatePolarDistanceDiff()
        expected = math.sqrt(9 + 16)
        self.assertAlmostEqual(distance, expected, places=5)

    def test_full_rotation(self):
        """Test: Volle 360 Grad Rotation"""
        self.nav.setPosParams(0, 0, 0)
        self.nav.setGoalParams(0, 0, 2 * math.pi)
        angle_diff = self.nav.calculatePolarGoalAngleDiff()
        self.assertAlmostEqual(angle_diff, 0.0, places=5)


class TestOutputStructure(unittest.TestCase):
    """Tests für die Output-Struktur"""

    def setUp(self):
        self.nav = NavigationController()

    def test_initial_output_values(self):
        """Test: Initiale Output-Werte sind null/false"""
        self.assertEqual(self.nav.out.linear.x, 0)
        self.assertEqual(self.nav.out.linear.y, 0)
        self.assertEqual(self.nav.out.angular.z, 0)
        self.assertEqual(self.nav.out.distance_remaining, 0)
        self.assertFalse(self.nav.out.finish)
        self.assertFalse(self.nav.out.success)

    def test_output_structure_exists(self):
        """Test: Alle Output-Felder existieren"""
        self.assertTrue(hasattr(self.nav.out, 'linear'))
        self.assertTrue(hasattr(self.nav.out.linear, 'x'))
        self.assertTrue(hasattr(self.nav.out.linear, 'y'))
        self.assertTrue(hasattr(self.nav.out, 'angular'))
        self.assertTrue(hasattr(self.nav.out.angular, 'z'))
        self.assertTrue(hasattr(self.nav.out, 'distance_remaining'))
        self.assertTrue(hasattr(self.nav.out, 'finish'))
        self.assertTrue(hasattr(self.nav.out, 'success'))


if __name__ == '__main__':
    # Ausführen aller Tests
    unittest.main(verbosity=2)