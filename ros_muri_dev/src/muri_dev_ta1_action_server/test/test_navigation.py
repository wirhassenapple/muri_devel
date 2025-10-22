import math
import pytest

# Dein Modul importieren (z. B. aus dem gleichen Package)
from muri_dev_ta1_action_server import move_logic as ml
from muri_dev_ta1_action_server.state_mach import StateMachine


@pytest.fixture(autouse=True)
def reset_state():
    """Vor jedem Test alles zurücksetzen."""
    ml.resetGoal()
    ml.resetFinish()
    yield
    ml.resetGoal()
    ml.resetFinish()


def test_initial_state_is_init():
    """Prüft, ob nach resetGoal() der Zustand Init ist."""
    assert ml.state == StateMachine.Init
    assert ml.goal.x is None
    assert ml.goal.y is None
    assert ml.out.finish is False


def test_set_goal_params():
    """SetGoalParams soll Zielwerte korrekt setzen."""
    ml.setGoalParams(1.0, 2.0, math.pi / 2)
    assert ml.goal.x == 1.0
    assert ml.goal.y == 2.0
    assert math.isclose(ml.goal.theta, math.pi / 2)


def test_set_position_and_speed_params():
    """Positions- und Geschwindigkeitsparameter müssen übernommen werden."""
    ml.setPosParams(0.5, -0.5, math.pi)
    ml.setSpeedParams(0.1, 0.0, 0.05)
    assert ml.position.x == 0.5
    assert ml.position.y == -0.5
    assert math.isclose(ml.position.theta, math.pi)
    assert ml.speed.angular.z == 0.05


def test_calculate_polar_angle_diff_none_safe():
    """Wenn Ziele oder Positionen None sind, soll Funktion False liefern."""
    angle, valid = ml.calculatePolarAngleDiff()
    assert valid is False
    assert angle == 0


def test_calculate_polar_angle_diff_valid():
    """Korrekte Winkelberechnung bei gesetzten Werten."""
    ml.setGoalParams(1, 0, 0)
    ml.setPosParams(0, 0, 0)
    angle, valid = ml.calculatePolarAngleDiff()
    assert valid is True
    assert math.isclose(angle, 0.0, abs_tol=1e-6)


def test_state_transition_turn_before_move():
    """Testet, dass der State von Init -> Calculate -> TurnBeforeMove wechselt."""
    ml.setGoalParams(1, 1, 0)
    ml.setPosParams(0, 0, 0)
    ml.executeMovement(True)
    assert ml.state in (StateMachine.Calculate, StateMachine.TurnBeforeMove)


def test_success_state():
    """Simuliert, dass alles fertig ist."""
    ml.setGoalParams(0, 0, 0)
    ml.setPosParams(0, 0, 0)
    ml.state = StateMachine.Success
    ml.executeMovement(True)
    assert ml.out.finish is True
    assert ml.out.success is True


def test_failure_state():
    """Failure-State soll Bewegung stoppen."""
    ml.state = StateMachine.Failure
    ml.executeMovement(True)
    assert ml.out.finish is True
    assert ml.out.linear.x == 0
    assert ml.out.angular.z == 0
