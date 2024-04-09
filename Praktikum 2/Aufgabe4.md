# Praktikum: 2. Prozesse und Threads

## 2.2 Threads

### Aufgabe 4

Suchen und beschreiben Sie in 1-2 Sätzen die Python-Entsprechungen zu pthread_create() und pthread_join().

Für die Nutzung von Threads in Python bietet sich das "threading" Modul an. Mit diesem erstellt man Thread Objekte, welche die gewünschte Aufgabe, entweder durch eine übergebene Funktion oder indem man die run() Methode überschreibt, enthalten.

pthread_create() entspricht dem Erstellen des Thread Objektes und dem aufrufen der start() Methode. Ähnlich wie bei Linux kann man Argumente übergeben. Bei einem Fehler erzeugt die start() Methode einen RuntimeError.

pthread_join() entspricht der join() Methode auf dem Thread Objekt. Der aufrufende Thread wartet bis der gejointe Thread terminiert. Anders als bei Linux kann man in Python auch einen Timeout angeben.
