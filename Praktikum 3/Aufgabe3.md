## Aufgabe 3

### 1. Erzeugen Sie eine Konfigurationsdatei _nur-cpu.dat_ für die vier Beispielprozesse auf Folie 4.Scheduling-29 und überprüfen Sie die Ausführreihenfolge.

Konfigurationsdatei ist bereits in den Vorlagen.

### 2. Machen Sie sich mit dem Programmquelltext vertraut – er ist gut dokumentiert. Welche Aufgaben übernehmen die Funktionen

**a) `create_process()`,**

Diese Funktion erzeugt einen neuen Task in Form eines Dictionaries. Als erstes wird mit der Funktion `get_freepid()` die nächste freie PID erfragt, welche zuletzt auch von der Funktion zurückgegeben wird. Die Funktion übernimmt zudem die übergebene Startzeit und wählt den Task-Status abhängig von dem Verhalten als `S_READY` oder `S_BLOCKED` wenn der Prozess mit einer I/O-Phase startet. `firstruntime` wird auf `-1` gesetzt, da der Prozess zu diesem Zeitpunkt noch nie gelaufen ist.

Das neue Task Dictionary wird an die globale Taskliste angehängt. Schlussendlich werden noch weitere Werte (`cputime=0`, `iotime=0`, `status`, `endtime=-1`) mithilfe der PID über "globale" Funktionen angepasst.

**b) `run_current()` und**

Diese Funktion lässt einen Prozess eine Zeiteinheit lang laufen. Falls der Prozess zuvor noch nie lief, wird die `firstruntime` gesetzt. Die verbleibende Rechenzeit der aktuellen Phase wird um eins reduziert und die Laufzeit um eins erhöht.

Abhängig von der aktuellen Phase wird die Funktion beendet oder (bei aktuellem Verhalten gleich Null) weitere Schritte ausgeführt. Dazu zählt das Entfernen des aktuellen Verhaltens vom Anfang der Liste, das Setzen des Status auf Blockiert und das Entfernen des Prozess aus der Warteschlange.

Daraufhin wird überprüft, ob der Prozess beendet ist. Wenn ja, wird der Status auf Fertig gesetzt und die Endzeit verzeichnet, andernfalls wird der Prozess and die Blockiert-Liste angefügt.

**c) `update_blocked_processes()` ?**

Diese Funktion bearbeitet alle Prozesse in der Blockiert-Liste, außer dem zuletzt gelaufenen Prozess. Die Wartezeit wird um eins reduziert und die I/O-Zeit erhöht. Wenn die aktuelle I/O-Phase abgeschlossen ist, wird auch diese Phase entfernt und der Status wieder auf Bereit gesetzt. Der Prozess wird aus der Blockiert-Liste entfernt.

Schließlich wird überprüft, ob der Prozess fertig ist - Prozess wird auf Status Fertig gesetzt und die Endzeit angegeben - oder nicht und wieder in die Queue gehangen wird.

### 3. Erzeugen Sie eine Kopie von _sched.py_ (etwa: _sched-sjf.py_) und passen Sie darin die Funktion `schedule()` so an, dass sie statt FCFS den SJF-Scheduler (Shortest Job First)  implementiert. Kommentieren Sie das Ergebnis stichwortartig.

- Änderung vergleichsweise einfach an dem Ast `elif (runqueue != []):` durchgeführt
- Nach initialisierung mit erstem Element aus der `runqueue` werden alle Elemente abgegangen und nach einem kürzeren gesucht
- Gibt es ein kürzeres Element, dann wird die `choice` mit dessen PID überschrieben
- Diese Änderung hat keine Einfluss auf Konfigurationsdateien wie `nur-cpu.dat` in denen es keine I/O-Phasen gibt

### 4. Etwas komplizierter wird es, einen unterbrechenden Scheduler zu schreiben.

**a) Im letzten Schritt passen Sie eine Kopie von _sched-sjf.py_ z. B. _sched-srt.py_, an und implementieren nur den SRT-Scheduler (Shortest Remaining Time). Hier funktioniert die einfache Variante aus den vorigen zwei Schedulern nicht mehr, aktive Prozesse solange laufen zu lassen, bis sie sich beenden oder in eine I/O-Phase eintreten.**

**b) Kommentieren Sie Ihre Programmsourcen**

Siehe _sched-srt.py_.

**c) Zeichnen Sie ein Gant-Diagramm Ihres Ergebnisses. Prüfen Sie, dass Ihr Ergebnis mit dem erwarteten Ergebnis übereinstimmt !**