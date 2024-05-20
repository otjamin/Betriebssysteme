import random
import time

comb_1 = [1, 2, 3]
comb_2 = [2, 3, 4] # these combinations may be changed, but adding
                   # a third will result in wrong logging.

def choose_next_book_combination():
    generated = random.randint(0, 1) == 0
    return comb_1 if generated == 0 else comb_2


class Student:
    def __init__(self, id, library, read_time=random.randint(1, 2)):
        self.id = id
        self.current_books = []
        self.time_last_borrowed_or_returned = time.perf_counter()
        self.library = library
        self.read_time = read_time
        self.running = True
        self.got_books = 0
        self.got_comb_1 = 0
        self.got_comb_2 = 0

    def log_combinations(self):
        self.got_comb_1 += 1 if self.current_books == comb_1 else 0
        self.got_comb_2 += 1 if self.current_books == comb_2 else 0

    def borrow(self):
        for book in choose_next_book_combination():
            success = self.library.borrow_book(book, self)
            if not success:
                self.return_books()
                self.time_last_borrowed_or_returned = time.perf_counter()
                self.library.add_timeout()
                return
        self.time_last_borrowed_or_returned = time.perf_counter()
        self.got_books += 1
        self.log_combinations()
        self.library.print_number_of_students_with_three_books()

    def return_books(self):
        for book in self.current_books:
            self.library.return_book(book, self)
        self.time_last_borrowed_or_returned = time.perf_counter()

    def simulate(self):
        while self.running:
            if time.perf_counter() > self.time_last_borrowed_or_returned + self.read_time:
                if not self.current_books:
                    self.borrow()
                else:
                    self.return_books()

#