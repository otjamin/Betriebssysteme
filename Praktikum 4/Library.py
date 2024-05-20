import sys
import threading
import time

from Student import Student


class Library:
    def __init__(self, book_stock=None):
        if book_stock is None:  # Default argument value would be mutable
            book_stock = [3, 5, 4, 2]
        self.books = []
        self.book_stock = book_stock
        self.students = []
        self.initialize_books()
        self.timeouts = 0

    def add_timeout(self):
        self.timeouts += 1

    def initialize_books(self):
        # Initialisiere Bücher mit deren Anzahl an Exemplaren

        for i, stock in enumerate(self.book_stock):
            self.books.append([i, threading.Semaphore(stock)])

    def borrow_book(self, id, borrower):
        start = time.perf_counter()
        result = self.books[id - 1][1].acquire(timeout=60)
        if result:
            borrower.current_books.append(id)
        else:
            print(f"Borrower {borrower.id} had to wait for too long.")
            return False
        end = time.perf_counter()
        if end - start > 0.01:
            print(f"Borrower {borrower.id} had to wait for {end - start} seconds.")
        return True

    def return_book(self, id, borrower):
        self.books[id - 1][1].release()
        borrower.current_books.remove(id)

    def initialize_students(self, number_of_students, read_time, stop_time=20):
        for i in range(number_of_students):
            student = Student(i, self, read_time)
            self.students.append(student)
            thread = threading.Thread(target=student.simulate)
            thread.start()
        time.sleep(stop_time)
        print("Stopping simulation...")
        for student in self.students:
            student.running = False

        self.print_results()
        sys.exit()

    def print_number_of_students_with_three_books(self):
        num = len([student for student in self.students if len(student.current_books) == 3])
        print(f"Number of students with three books: {num}")

    def print_results(self):
        for student in self.students:
            print(f"Student {student.id} borrowed {student.got_books} times.")
        print("-" * 20)
        print(f"Number of timeouts: {self.timeouts}")
        total_book_combs = sum([student.got_books for student in self.students])
        print("-" * 20)
        print("Total number of combinations borrowed: ", total_book_combs)
        print("Total time without parallelism: ", total_book_combs * reading_time)
        print("Total time with parallelism: ", stop_after)
        print("Total time saved: ", total_book_combs * reading_time - stop_after, " seconds.")
        print("Degree of parallelism: ", total_book_combs * reading_time / stop_after)
        print("-" * 20)
        print("Number of students who borrowed combination 1: ", sum([student.got_comb_1 for student in self.students]))
        print("Number of students who borrowed combination 2: ", sum([student.got_comb_2 for student in self.students]))



if __name__ == "__main__":
    library = Library()
    reading_time = 1  # Read-Time in Sekunden
    num_students = 5  # Anzahl der Studenten
    stop_after = 15  # Stop-Time in Sekunden
    library.initialize_students(num_students, reading_time, stop_after)
