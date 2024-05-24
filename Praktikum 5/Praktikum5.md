# Praktikum 5

## Aufgabe 1

### Befehle

| Befehl    | Client | Server |
| --------- | ------ | ------ |
| socket()  | Hiermit erstellt man ein neues Socket Objekt. Erfolgen keine weiteren Angaben wird ein Socket mit IPv4 und TCP erstellt. Möchte man einen UDP Socket erstellen, muss man den Typ als SOCK_DGRAM setzen. | siehe Client |
| connect() | Verbindet den Client mit einem Server Socket an der übergebene Adresse. Die Andresse muss entsprechend der Adressfamilie angegeben werden. | - |
| bind()    | - | Bindet den Server Socket an die Adresse, auf die später gelauscht wird. Die Angabe erfolgt normal in der Form (HOST, PORT). |
| listen()  | - | Erlaubt dem Server Verbindungen zu akzeptieren. |
| accept()  | - | Der Server akzeptiert eine Verbindung und gibt ein neues Socket Objekt und die Adresse dieser Verbindung zurück. |
| send()    | Sendet Daten in Form von Bytes an den anderen Verbindungsparter. Eine Verbindung muss bereits bestehen. Gibt die Anzahl der gesendeten Bytes zurück. | siehe Client |
| recv()    | Empfängt Daten vom anderen Verbindungspartner. Maximal die übergebene Größe an Daten wird auf Einmal empfangen. | siehe Client |
| close()   | Markiert den Socket als geschlossen. Beendet die Verbindung nicht zwangsläufig sofort. Nicht unbedingt notwendig, aber empfohlen, oder mit with Ausdruck. | siehe Client |


