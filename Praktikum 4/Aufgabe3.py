import sys
import time
import random

from threading import Thread, BoundedSemaphore, Event


class Library:
    def __init__(self):
        self.books = []
        self.returns = Event()

    def add_books(self, copies):
        for c in copies:
            self.books.append(BoundedSemaphore(c))

    def borrow_book(self, book_id) -> bool:
        return self.books[book_id-1].acquire(blocking=False)
    
    def return_book(self, book_id):
        self.books[book_id-1].release()

    def signal_return(self):
        self.returns.set()
        self.returns.clear()

    def wait_for_return(self):
        self.returns.wait()


class Student(Thread):
    def __init__(self, student_id, book_combination):
        Thread.__init__(self)
        self.student_id = student_id
        self.book_combination = book_combination
        self.books = []
        self.borrowings = 0

    def __print_info(self):
        print('{:<8} {:<23} {:<11}'.format(self.student_id, self.borrowings, '✅' if self.books else '❌'))

    def run(self):
        while True:
            for book_id in self.book_combination:
                if library.borrow_book(book_id):
                    self.books.append(book_id)
                else:
                    for book_id in self.books:
                        library.return_book(book_id)
                    self.books = []

                    self.__print_info()
                    library.returns.wait()
                    break

            self.borrowings += 1
            self.__print_info()
            time.sleep(reading_time)

            for book_id in self.books:
                library.return_book(book_id)
            library.signal_return()
            self.books = []


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 Aufgabe3.py <number of students> <reading time>")
        sys.exit(1)

    number_of_students = int(sys.argv[1])
    reading_time = int(sys.argv[2])

    library = Library()
    library.add_books([3, 5, 4, 2])

    book_combinations = [
        [1, 2, 3],
        [2, 3, 4]
    ]

    print('{:<8} {:<23} {:<11}'.format('Student', 'Hatte x mal die Bücher', 'Hat Bücher?'))

    students = [Student(i+1, random.choice(book_combinations)) for i in range(number_of_students)]
    for student in students:
        student.start()
    for student in students:
        student.join()
