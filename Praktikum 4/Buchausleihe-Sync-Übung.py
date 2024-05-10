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

    def __init__(self, library, readingTime):
        threading.Thread.__init__(self)             # Initialisiere den Thread
        self.library = library                      # Referenz auf die Bibliothek
        self.books_borrowed = 0                     # Counter für Anzahl der ausgeliehenen Bücher
        self.students_readingTime = readingTime     # Lesezeit des Studenten

    def run(self):
        # Versuche, Bücher 1, 2 und 3 auszuleihen
        if self.borrow_books([self.library.book1, self.library.book2, self.library.book3]):
            #print(f"Student {self.name} hat Bücher 1, 2 und 3 ausgeliehen\n")
            time.sleep(student.students_readingTime)
            # Gib die Bücher zurück
            self.return_books([self.library.book1, self.library.book2, self.library.book3])

        # Versuche, Bücher 2, 3 und 4 auszuleihen
        if self.borrow_books([self.library.book2, self.library.book3, self.library.book4]):
            #print(f"Student {self.name} hat Bücher 2, 3 und 4 ausgeliehen\n")
            time.sleep(student.students_readingTime)
            # Gib die Bücher zurück
            self.return_books([self.library.book2, self.library.book3, self.library.book4])

    def borrow_books(self, books):
        for book in books:
            while not book.acquire(blocking=True):
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


library = Library()

numberOfStudents = int(input("Anzahl der gewünschten Studenten eingeben: "))
readingTime = int(input("Gewünschte Lesezeit eingeben: "))

students = [Student(library, readingTime) for _ in range(numberOfStudents)]
for student in students:
    student.start()
for student in students:
    student.join()

print_statistics(students)


