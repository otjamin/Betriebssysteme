# Implementierung von Nils

import threading
import time

global fstCombinationCounter
fstCombinationCounter =  0
global sndCombinationCounter
sndCombinationCounter = 0
class Library:
    def __init__(self):
        # Initialisiere Semaphoren für jedes Buch mit der Anzahl der verfügbaren Exemplare
        self.book1 = threading.Semaphore(3)
        self.book2 = threading.Semaphore(5)
        self.book3 = threading.Semaphore(4)
        self.book4 = threading.Semaphore(2)

class Student(threading.Thread):
    studentsWithThreeBooks = 0

    def __init__(self, library, readingTime, fstBooksToBorrow, sndBooksToBorrow):
        threading.Thread.__init__(self)             # Initialisiere den Thread
        self.library = library                      # Referenz auf die Bibliothek
        self.books_borrowed = 0                     # Counter für Anzahl der ausgeliehenen Bücher
        self.students_readingTime = readingTime     # Lesezeit des Studenten
        self.fstBooksToBorrow = fstBooksToBorrow    # erste Liste der Bücher, die der Student ausleihen soll
        self.sndBooksToBorrow = sndBooksToBorrow    # zweite Liste der Bücher, die der Student ausleihen soll

    def run(self):
        global fstCombinationCounter, sndCombinationCounter
        n = 0
        while n < 10:    # Begrenzung um eine Endlosschleife zu vermeiden und die Daten auswerten zu können
            n += 1
            # Versuche, Bücher mit übergebener Kombination auszuleihen
            if self.borrow_books(self.fstBooksToBorrow):
                #print(f"Student {self.name} hat Bücher 1, 2 und 3 ausgeliehen\n")
                fstCombinationCounter += 1
                time.sleep(self.students_readingTime)   # Lesezeit
                # Gib die Bücher zurück
                self.return_books(self.fstBooksToBorrow)

            # Versuche, Bücher mit weiterer übergebener Kombination auszuleihen
            elif self.borrow_books(self.sndBooksToBorrow):
                #print(f"Student {self.name} hat Bücher 2, 3 und 4 ausgeliehen\n")
                sndCombinationCounter += 1
                time.sleep(self.students_readingTime)   # Lesezeit
                # Gib die Bücher zurück
                self.return_books(self.sndBooksToBorrow)


    def borrow_books(self, books):
        for book in books:
            if not book.acquire(blocking=True, timeout=1):  #Versuchen, die Bücher auszuleihen. blocking=True um Semaphore zu berücksichtigen und timeout um Deadlocks zu vermeiden
                return False
        self.books_borrowed += 1
        print(f"Student '{self.name}' hat _{self.books_borrowed}_ Mal alle Bücher ausgeliehen\n")
        Student.studentsWithThreeBooks += 1
        print(f"ALLE DREI: Es gibt _{Student.studentsWithThreeBooks}_ Studenten, die gerade drei Bücher haben\n")
        return True

    def return_books(self, books):
        for book in books:
            book.release()
        Student.studentsWithThreeBooks -= 1
        print(f"ALLE DREI: Es gibt _{Student.studentsWithThreeBooks}_ Studenten, die gerade drei Bücher haben\n")

def print_statistics(students):
    print("Zusammenfassung:")
    for student in students:
        print(f"Student '{student.name}' hat {student.books_borrowed} Mal Bücher ausgeliehen")

def main():
    library = Library()
    allBooks = [library.book1, library.book2, library.book3, library.book4]

    # Eingabe
    #############
    fstBookId = (input("Geben sie die erste Ausleih-Kombination ein: "))

    # Konvertiere die IDs in eine Liste von Integer-Werten
    fstBookIds = list(map(int, fstBookId.split(',')))

    # Hole die entsprechenden Buchobjekte aus der Bibliothek
    fstBooksToBorrow = [allBooks[id - 1] for id in fstBookIds]

    sndBookId = (input("Geben sie die zweite Ausleih-Kombination ein: "))

    # Konvertiere die IDs in eine Liste von Integer-Werten
    sndBookIds = list(map(int, sndBookId.split(',')))

    # Hole die entsprechenden Buchobjekte aus der Bibliothek
    sndBooksToBorrow = [allBooks[id - 1] for id in sndBookIds]

    numberOfStudents = int(input("Anzahl der gewünschten Studenten (Threads) eingeben: "))
    readingTime = float(input("Gewünschte Lesezeit eingeben: "))
    #############

    # initialisiere Liste an Studenten anhand der vom User gegebenen Parameter
    students = [Student(library, readingTime, fstBooksToBorrow, sndBooksToBorrow) for _ in range(numberOfStudents)]

    # Starte alle Studenten-Threads
    for student in students:
        student.start()

    # Warte auf das Ende aller Studenten-Threads
    for student in students:
        student.join()

    # Ausgabe der Statistik über die Anzahl der ausgeliehenen Bücher pro Student
    print_statistics(students)
    # Ausgabe über die Verteilung der verschiedenen Ausleih - Kombinationen
    print(f"Erste Kombination wird {fstCombinationCounter} Mal ausgeliehen.\nZweite Kombination wird {sndCombinationCounter} Mal ausgeliehen.")

if __name__ == "__main__":
    main()