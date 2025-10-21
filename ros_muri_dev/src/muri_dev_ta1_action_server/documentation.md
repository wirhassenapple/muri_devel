# M.U.R.I devel Teilaufgabe 1 Teil 3/3

### Bewegungsbefehl
Nach dem Empfang des GoTo-2D-Pose-Befehls (Eingabe für die Zielposition) wird die aktuelle Roboterposition aus dem Topic /odom eingelesen.
Daraufhin erfolgt die Berechnung der Entfernung zum Ziel, wobei dieser Berechnungsvorgang zeitgesteuert aufgerufen wird.

Liegt die ermittelte Entfernung über der definierten Toleranzgrenze, wird zunächst der Sollwinkel in Richtung des Zielpunkts berechnet. Aus der Differenz zwischen Soll- und Istwinkel ergibt sich die benötigte Winkelverdrehung.

Ist diese Winkelabweichung größer als die zulässige Toleranz, wird die erforderliche Winkelgeschwindigkeit berechnet und anschließend auf dem Topic /cmd_vel veröffentlicht.

Liegt die Winkelabweichung innerhalb der Toleranz, wird die Winkelgeschwindigkeit auf 0 gesetzt. Stattdessen wird die lineare Geschwindigkeit berechnet und ebenfalls über /cmd_vel publiziert.

Während des gesamten Prozesses wird regelmäßig ein Feedback mit der aktuellen Roboterposition ausgegeben.
Sobald sich der Roboter innerhalb der definierten Ziel- und Winkeltoleranzen befindet, wird der Status succeed = True gesetzt, um den erfolgreichen Abschluss der Bewegung zu signalisieren.

## Ziel: Ein Turtlebot bewegt sich von einer Position auf eine andere Vorgegebene 2D Position