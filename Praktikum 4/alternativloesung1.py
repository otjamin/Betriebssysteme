import argparse
import threading
import time
import random

STUDENT_QUANTITY = 10
READTIME = 0.1
LEARNINGSESSIONS = 3
BOOKS = []
BOOKCOMBINATIONS = []


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-sq', '--studentQuantity', type=int, default=20)
parser.add_argument('-rt', '--readTime', type=float, default=0.1)
parser.add_argument('-s', '--sessions', type=int, default=10)
parser.add_argument('-bt', '--bookTotal', type=int, nargs='*', default=[3, 5, 4, 2])
parser.add_argument('-bc', '--bookCombinations', type=int, nargs='*', default=[123, 234])

combinationsReceived = []
activeBookCombinations = 0
combinations_read = [0, 0]
print("books: ", len(BOOKCOMBINATIONS))
counter_lock = threading.Lock()

def student_thread(studentID):    
    global combinationsReceived
    global activeBookCombinations
    global combinations_read

    while True:
        bookCombination = random.choice(BOOKCOMBINATIONS)
        aquiredIndices = [i for i, x in enumerate(bookCombination) if x.acquire(blocking=False)]
        studentHasAllBooks = len(aquiredIndices) == len(bookCombination)
        
        if studentHasAllBooks:
            counter_lock.acquire()
            combinations_read[BOOKCOMBINATIONS.index(bookCombination)] += 1
            counter_lock.release()
            combinationsReceived[studentID] += 1
            activeBookCombinations += 1
            time.sleep(READTIME)
            
        for bookIndex in aquiredIndices:
            bookCombination[bookIndex].release()
            
        if studentHasAllBooks:
            activeBookCombinations -= 1
      
        if combinationsReceived[studentID] >= LEARNINGSESSIONS:
            break


def print_status():
    """
    Outputs a status report on various library-related activities involving students.
    
    Uses the global variables:
    - combinationsReceived: A list representing the number of books borrowed by each student.
    - activeBookCombinations: The total number of students currently using books.
    - studentsFinished: The number of students who completed sessions with a preset number of books.
    - LEARNINGSESSIONS: Constant representing the required number of books for a complete session.
    """
    print("\nAnzahl der Ausleihen pro Student:", combinationsReceived)
    print("Anzahl der Arbeitennden Studenten:", activeBookCombinations)
    print(f"Anzahl der Studenten mit {LEARNINGSESSIONS} Büchern:", studentsFinished)
    print(f"Anzahl Studysessions: {sum(x for x in combinationsReceived)}")
    print(f"Anzahl der Studenten, die noch nicht gelernt haben: {sum(x == 0 for x in combinationsReceived)}") 

if __name__ == "__main__":
    args = parser.parse_args()
    STUDENT_QUANTITY = args.studentQuantity
    READTIME = args.readTime
    LEARNINGSESSIONS = args.sessions
    for b in args.bookTotal:
        BOOKS.append(threading.Semaphore(b))
    for c in args.bookCombinations:
        indices = [int(x) for x in str(c)]
        BOOKCOMBINATIONS.append([BOOKS[x - 1] for x in indices])
    combinationsReceived = [0] * STUDENT_QUANTITY
    semaphoreValues = [x._value for x in BOOKS]

    print(f'\n{STUDENT_QUANTITY} Studenten, die ihre Bachelorarbeit schreiben, benötigen {LEARNINGSESSIONS} Mal, \njeweils gleichzeitig, eine der '
          f'folgenden Buchkombinationen: {args.bookCombinations}. \nVon den jeweiligen '
          f'Büchern stehen je {semaphoreValues} Exemplare zur Verfügung.\n')

    students = []
    for i in range(STUDENT_QUANTITY):
        t = threading.Thread(target=student_thread, args=(i,))
        students.append(t)
        t.start()

    startTime = time.time()
    while True:
        time.sleep(1)
        studentsFinished = sum(1 for b in combinationsReceived if b >= LEARNINGSESSIONS)

        if studentsFinished == STUDENT_QUANTITY:
            break
    print_status()        
    
    time.sleep(1)  
    endTime = time.time()
    timeElapsed = endTime - startTime
    studentTimeNeeded = str(round(READTIME * LEARNINGSESSIONS, 2))
    maxTime = READTIME * LEARNINGSESSIONS * STUDENT_QUANTITY
    print(f'\nAlle Studenten haben fertig gelernt.')
    print(f'Benötigte Zeit: {str(round(timeElapsed, 2))} Sekunden für {STUDENT_QUANTITY} Studenten mit '
          f'einer Lernzeit von jeweils {studentTimeNeeded} Sekunden.')
    print(f'Ohne Parallelisierung hätte dies '
          f'{str(round(maxTime, 2))} Sekunden gedauert.')
    print(f'Durchschnittlich haben also immer '
          f'{str(round(maxTime / timeElapsed, 2))} Studenten gleichzeitig gearbeitet.\n')
    print(f'Gelesene Kombinationen: {combinations_read}')
