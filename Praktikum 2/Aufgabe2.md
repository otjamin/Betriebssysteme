# Praktikum: 2. Prozesse und Threads

## 2.2 Threads

### Aufgabe 2 Python

1. Schreiben Sie ein Python-Programm, dem ein Argument übergeben wird, das in einer Endlosschleife das Argument ausgibt und sich 10 Sekunden schlafen legt (sleep).

#### Code:

```python

import time
import sys

if len(sys.argv) >= 1:
	while True:
		print(sys.argv[1])
		time.sleep(10)
else: print('Please specify argument after name of program (example: python3 Aufgabe2.py "your argument here ")')

```

#### Ausgabe:

```sh
devbox@devbox:~/Desktop/betriebsysteme/praktikum/Betriebssysteme/Praktikum 2$ python3 Aufgabe2.py "ausgabe"
ausgabe
ausgabe
```

#### Aus "man kill":

The default signal for kill is TERM. Use -l or -L to list available signals. Particularly useful signals include HUP, INT, KILL, STOP, CONT, and 0. Alternate signals may be specified in three ways: -9, -SIGKILL or -KILL. Negative PID values may be used to choose whole process groups; see the PGID column in ps command output. A PID of -1 is special; it indicates all processes except the kill process itself and init.

2.  Starten Sie das Programm zweimal als Shell-Hintergrundprozess:

```sh
python3 Aufgabe2.py "ausgabe1" &
python3 Aufgabe2.py "ausgabe2" &
```

3.  Senden Sie einem der Programme ein STOP-Signal, danach ein CONT-Signal.
    Zunächst benötigt man die PID. Diese lässt sich über den Befehl'ps' herausfinden.
    Danach lässt sich der Prozess mittels dem Befehl 'kill -STOP "PID" ' stoppen
    ![](<images/Screenshot 2024-04-10 161228.png>)
    Mittels ' kill -CONT "PID" ' kann man den Prozess wieder Starten.
    ![](<images/Screenshot 2024-04-12 083230.png>)

4.  Mit ' kill -TERM "PID" ' wird ein prozess Terminiert.![](<images/Screenshot 2024-04-12 083532.png>)

5.  Senden Sie einem Prozess, der Ihnen nicht gehört, ein 'kill -9'.
    ![](<images/Screenshot 2024-04-12 084541.png>)
6.  Ausgabe2_pid.py

```paython
import os

N = 3
pids = []  # Liste für Kind-Prozess-IDs

for i in range(N):
    pid = os.fork()
    if pid == 0:
        for j in range(200):
            print(f"Kind {i + 1} mit PID={os.getpid()}")
        exit(0)
    else:
        pids.append(pid)

for i in range(200):
    print(f"Vater mit PID={os.getpid()}: PID1={pids[0]}, PID2={pids[1]}, PID3={pids[2]}")

```

Ausführung in Aufgabe2.txt

Reihenfolge ist in diesem Fall Kind 1 -> Vater -> Kind 3 -> Kind 2
