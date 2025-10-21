# M.U.R.I devel Teilaufgabe 1 Teil 3/3

### Bewegungsbefehl
Nach dem Empfang des GoTo-2D-Pose-Befehls (Eingabe für die Zielposition) wird die aktuelle Roboterposition aus dem Topic `/odom` eingelesen.
Daraufhin erfolgt die Berechnung der Entfernung zum Ziel, wobei dieser Berechnungsvorgang zeitgesteuert aufgerufen wird.

```python
def get_distance_to_goal(current_pos, goal_pos):
    return math.sqrt(
        (goal_pos.x - current_pos.x) ** 2 + 
        (goal_pos.y - current_pos.y) ** 2
    )
```

Liegt die ermittelte Entfernung über der definierten Toleranzgrenze, wird zunächst der Sollwinkel in Richtung des Zielpunkts berechnet:

```python
def calculate_target_angle(current_pos, goal_pos):
    return math.atan2(
        goal_pos.y - current_pos.y,
        goal_pos.x - current_pos.x
    )
```

Aus der Differenz zwischen Soll- und Istwinkel ergibt sich die benötigte Winkelverdrehung:

```python
angle_diff = target_angle - current_angle
if angle_diff > math.pi:
    angle_diff -= 2 * math.pi
elif angle_diff < -math.pi:
    angle_diff += 2 * math.pi
```

Ist diese Winkelabweichung größer als die zulässige Toleranz, wird die erforderliche Winkelgeschwindigkeit berechnet und über `/cmd_vel` publiziert:

```python
if abs(angle_diff) > ANGLE_TOLERANCE:
    cmd_vel_msg = Twist()
    cmd_vel_msg.angular.z = K_ANGULAR * angle_diff
    cmd_vel_publisher.publish(cmd_vel_msg)
```

Bei akzeptabler Winkelausrichtung wird die lineare Bewegung gesteuert:

```python
else:
    cmd_vel_msg = Twist()
    cmd_vel_msg.linear.x = min(K_LINEAR * distance_to_goal, MAX_LINEAR_SPEED)
    cmd_vel_publisher.publish(cmd_vel_msg)
```

Der Fortschritt wird kontinuierlich überwacht:

```python
def publish_feedback():
    feedback_msg = GoToPoseFeedback()
    feedback_msg.current_pose = current_pose
    self._action_server.publish_feedback(feedback_msg)
```

Bei Erreichen der Zielposition innerhalb der Toleranzen wird der Erfolg signalisiert:

```python
if distance_to_goal < POSITION_TOLERANCE and abs(angle_diff) < ANGLE_TOLERANCE:
    result = GoToPoseResult()
    result.success = True
    self._action_server.set_succeeded(result)
```

## Ziel: Ein Turtlebot bewegt sich von einer Position auf eine andere Vorgegebene 2D Position
### Allgemein
Nach dem Empfang des GoTo-2D-Pose-Befehls (Eingabe für die Zielposition) wird die aktuelle Roboterposition aus dem Topic /odom eingelesen. Daraufhin erfolgt die Berechnung der Entfernung zum Ziel, wobei dieser Berechnungsvorgang zeitgesteuert aufgerufen wird.

Liegt die ermittelte Entfernung über der definierten Toleranzgrenze, wird zunächst der Sollwinkel in Richtung des Zielpunkts berechnet. Aus der Differenz zwischen Soll- und Istwinkel ergibt sich die benötigte Winkelverdrehung.

Ist diese Winkelabweichung größer als die zulässige Toleranz, wird die erforderliche Winkelgeschwindigkeit berechnet und anschließend auf dem Topic /cmd_vel veröffentlicht.

Liegt die Winkelabweichung innerhalb der Toleranz, wird die Winkelgeschwindigkeit auf 0 gesetzt. Stattdessen wird die lineare Geschwindigkeit berechnet und ebenfalls über /cmd_vel publiziert.

Während des gesamten Prozesses wird regelmäßig ein Feedback mit der aktuellen Roboterposition ausgegeben. Sobald sich der Roboter innerhalb der definierten Ziel- und Winkeltoleranzen befindet, wird der Status succeess = True gesetzt, um den erfolgreichen Abschluss der Bewegung zu signalisieren.

