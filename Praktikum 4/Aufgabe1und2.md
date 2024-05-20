# Praktikum 4

## Aufgabe 1

Für die Umsetzung dieser Aufgabe verwende ich folgende Synchronisationsobjekte:
- Jedes der Bücher wird durch ein (Bounded)Semaphore Objekt dargestellt. Dieses wird mit der Anzahl der Exemplare initialisiert. In unserem Beispiel also 3, 5, 4, und 2 Exemplare.

- Sollte ein Student nicht die Bücher finden, die er benötigt, blockiert er nicht weiter die Ausleihe sondern wartet auf ein Event Objekt, das signalisiert wenn ein anderer Student Bücher zurückgegeben hat. Initial ist die Flag im Event nicht wahr.

## Aufgabe 2

1. Der Studenten Thread versucht nacheinander die Bücher abzugreifen die er benötigt.

2. Scheitert das bei einem Buch, gibt er alle bisher entliehenen Bücher wieder zurück und wartet auf eine Rückgabe.

3. Andernfalls liest er seine Bücher für die angegebene Zeit und gibt sie dann alle wieder zurück.

4. Daraufhin startet der Ablauf von vorne.
