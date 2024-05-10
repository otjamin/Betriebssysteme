import threading
import time
class Library:
    def __init__(self):
        # Initialisiere Semaphoren für jedes Buch mit der Anzahl der verfügbaren Exemplare
        self.book1 = threading.Semaphore(3)
        self.book2 = threading.Semaphore(5)
        self.book3 = threading.Semaphore(4)
        self.book4 = threading.Semaphore(2)

class Student(threading.Thread):
    students_with_three_books = 0

    def __init__(self, library, readingTime, fstBooksToBorrow, sndBooksToBorrow):
        threading.Thread.__init__(self)             # Initialisiere den Thread
        self.library = library                      # Referenz auf die Bibliothek
        self.books_borrowed = 0                     # Counter für Anzahl der ausgeliehenen Bücher
        self.students_readingTime = readingTime     # Lesezeit des Studenten
        self.fstBooksToBorrow = fstBooksToBorrow    # erste Liste der Bücher, die der Student ausleihen soll
        self.sndBooksToBorrow = sndBooksToBorrow    # zweite Liste der Bücher, die der Student ausleihen soll

    def run(self):
        while True:
            # Versuche, Bücher 1, 2 und 3 auszuleihen
            if self.borrow_books(self.fstBooksToBorrow):
                #print(f"Student {self.name} hat Bücher 1, 2 und 3 ausgeliehen\n")
                time.sleep(self.students_readingTime)
                # Gib die Bücher zurück
                self.return_books(self.fstBooksToBorrow)

            # Versuche, Bücher 2, 3 und 4 auszuleihen
            elif self.borrow_books(self.sndBooksToBorrow):
                #print(f"Student {self.name} hat Bücher 2, 3 und 4 ausgeliehen\n")
                time.sleep(self.students_readingTime)
                # Gib die Bücher zurück
                self.return_books(self.sndBooksToBorrow)


    def borrow_books(self, books):
        for book in books:
            while not book.acquire(blocking=False):  #Versuchen, das Buch auszuleihen. blocking=True um Semaphore zu berücksichtigen und timeout um Deadlocks zu vermeiden
                pass
        self.books_borrowed += 1
        print(f"Student '{self.name}' hat _{self.books_borrowed}_ Mal alle Bücher ausgeliehen\n")
        Student.students_with_three_books += 1
        print(f"ALLE DREI: Es gibt _{Student.students_with_three_books}_ Studenten, die gerade drei Bücher haben\n")
        return True

    def return_books(self, books):
        for book in books:
            book.release()
        Student.students_with_three_books -= 1
        print(f"ALLE DREI: Es gibt _{Student.students_with_three_books}_ Studenten, die gerade drei Bücher haben\n")

def print_statistics(students):
    print("Zusammenfassung:")
    for student in students:
        print(f"Student '{student.name}' hat {student.books_borrowed} Mal Bücher ausgeliehen")

def main():
    library = Library()

    allBooks = [library.book1, library.book2, library.book3, library.book4]

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

    students = [Student(library, readingTime, fstBooksToBorrow, sndBooksToBorrow) for _ in range(numberOfStudents)]
    #students = [Student(library, readingTime) for _ in range(numberOfStudents)]
    for student in students:    # Starte alle Studenten-Threads
        student.start()

    # Bestimme den Parallelisierungsgrad
    parallelisierungsgrad = threading.active_count()

    for student in students:    # Warte auf das Ende aller Studenten-Threads
        student.join()

    # Ausgabe der Statistik über die Anzahl der ausgeliehenen Bücher pro Student
    print_statistics(students)

    # Ausgabe des Parallelisierungsgrads
    print(f"\nDer Parallelisierungsgrad beträgt: {parallelisierungsgrad}\n")

if __name__ == "__main__":
    main()

