# Roboter-Zustandsmaschine

Dieses Dokument beschreibt die Implementierung einer einfachen Zustandsmaschine in Python zur Steuerung eines Roboters.  
Die Maschine verarbeitet Positions- und Zielkoordinaten und steuert den Roboter Schritt für Schritt zu einem Zielpunkt.

---

## Übersicht der Zustände

Die Zustandsmaschine (`StateMachine`) hat folgende Zustände:

| Zustand             | Beschreibung                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `Init`             | Initialisierung der Maschine                                                 |
| `Calculate`        | Berechnung der Winkel- und Distanzdifferenzen zum Ziel                      |
| `TurnBeforeMove`   | Drehen, bis der Roboter auf das Ziel ausgerichtet ist                        |
| `DriveMove`        | Vorwärtsbewegung zum Ziel                                                    |
| `TurnAfterMove`    | Drehen auf die gewünschte Endorientierung am Ziel                             |
| `Success`          | Ziel erreicht                                                                |
| `Failure`          | Ziel konnte nicht erreicht werden                                             |

---

## Globale Variablen

```python
state = StateMachine.Init
goal = SimpleNamespace(x=None, y=None, theta=None)
position = SimpleNamespace(x=None, y=None, theta=None)
speed = SimpleNamespace(
    linear=SimpleNamespace(x=None, y=None),
    angular=SimpleNamespace(z=None)
)
turnedBeforeMove = False
out = SimpleNamespace(
    linear=SimpleNamespace(x=0, y=0),
    angular=SimpleNamespace(z=0),
    distance_remaining=0,
    finish=False,
    success=False
)
ad, dd, agd = None, None, None
ANGLE_TOLERANCE = math.radians(2)
TRANSLATION_TOLERANCE = 0.05
```

## Funktionen 

(`getOut()`) 
Gibt die aktuellen Ausgabewerte der Zustandsmaschine zurück.

```python
def getOut():
    global out
    return out
```

(`setPosParams(x, y, th)`)
Setzt die aktuelle Roboterposition.

```python
def setPosParams(x, y, th):
    position.x = x
    position.y = y
    position.theta = th
```

(`setSpeedParams(lx, ly, az)`)
Setzt die aktuellen Geschwindigkeiten.

(`setGoalParams(x, y, th)`)
Setzt das Ziel für den Roboter.

(`resetGoal()`)
Setzt Ziel und Status zurück und stoppt die Bewegung.

(`resetFinish()`)
Setzt die (`finish`)-Flags zurück.

(`calculatePolarAngleDiff()`)
Berechnet den Winkel zwischen aktueller Position und Ziel.
Gibt (`(angle_diff, valid_flag)`) zurück.

```python
def calculatePolarAngleDiff():
    if (goal.x is None) or (goal.y is None) or (position.x is None) or (position.y is None):
        return 0, False
    target_angle = math.atan2(goal.y - position.y, goal.x - position.x)
    angle_diff = target_angle - position.theta

    if angle_diff > math.pi:
        angle_diff -= 2 * math.pi
    elif angle_diff < -math.pi:
        angle_diff += 2 * math.pi

    return angle_diff, True
```
(`calculatePolarDistanceDiff()`)
Berechnet die Distanz zum Ziel:
```python
def calculatePolarDistanceDiff():
    if (goal.x is None) or (goal.y is None) or (position.x is None) or (position.y is None):
        return 0, False
    distance = math.sqrt((goal.x - position.x)**2 + (goal.y - position.y)**2)
    return distance, True
```
(`calculatePolarGoalAngleDiff()`)
Berechnet den Unterschied zwischen der Zielorientierung und der aktuellen Orientierung:

```python
def calculatePolarGoalAngleDiff():
    if (goal.theta is None) or (position.theta is None):
        return 0, False
    angle_diff = goal.theta - position.theta
    if angle_diff > math.pi:
        angle_diff -= 2 * math.pi
    elif angle_diff < -math.pi:
        angle_diff += 2 * math.pi
    return angle_diff, True

```
(`checkGoalExceeded(ad)`)
Prüft, ob der Winkel das Limit überschreitet:

```python
def checkGoalExceeded(ad):
    if ad > math.pi:
        return True
    return False

```
## Hauptfunktion (`executeMovement(reset)`)
Steuert die Zustandsmaschine und entscheidet, welche Bewegung ausgeführt wird.