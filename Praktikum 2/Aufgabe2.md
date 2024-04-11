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
The default signal for kill is TERM.  Use -l or -L to list available signals.  Particularly useful signals include HUP, INT, KILL, STOP, CONT, and 0.  Alternate signals may be specified in three ways: -9, -SIGKILL or -KILL.  Negative PID values may be used to choose whole process groups; see the PGID column in ps command output.  A PID of -1 is special; it indicates all processes except the kill process itself and init.




2. Starten Sie das Programm zweimal als Shell-Hintergrundprozess:
3. 
4. Senden Sie einem der Programme ein STOP-Signal, danach ein CONT-Signal.
   
### Fragen:
◦ was beobachten Sie ?
◦ welchen Status haben die Prozesse, während sie schlafen (ps).
• Senden Sie einem Prozess ein kill-Signal (TERM).
Frage: was beobachten Sie ?
• Senden Sie einem Prozess, der Ihnen nicht gehört, ein 'kill -9'.
Frage: was beobachten Sie ?
• Schreiben Sie ein Programm, das mittels fork N Childs erzeugt, mit N=3:
◦ der Vaterprozess soll 200mal die PIDs seiner Childs ausgeben: PID1, PID2, PID3
◦ die Kind-Prozesse sollen jeweils ihre eigene PID 200 mal ausgeben: „Kind mit PID=XXX“
Frage: Was beobachten Sie bezüglich der Reihenfolge der Prozessausführung?