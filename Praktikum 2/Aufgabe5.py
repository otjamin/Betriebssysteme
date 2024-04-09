import threading


# Die Klasse MyClass dient zur schöneren Gestaltung/Ordnung dieses Programmes,
# damit die Lesbarkeit gewährleitet bleibt.
class MyClass:

    def __init__(self, debug=False, num_threads=100):
        self.debug = debug  # Durch True setzen wird "var" ausgegeben, standardm. False.
        self.var = 0  # Dieser Wert wird durch die Threads angepasst
        self.num_threads = num_threads  # Anzahl der zu startenden Threads, standardm. 100

        '''
        Diese Methode addiert 5 auf die Variable var
        in einer Schleife von 1_000_000 Iterationen, indem die Variable
        je 5 Mal um 1 erhöht wird. Wenn debug=True, wird der Wert von var
        nach jeder Iteration ausgegeben.
        Dies kann zu einer unübersichtlichen Ausgabe führen, da Threads
        parallel laufen und die Ausgabe nicht synchronisiert ist. Im Debug-Modus
        wird die Schleife nur 10_000 Mal durchlaufen (Zeitgründe).
        '''


    def add(self):
        for i in range(1_000_000 if not self.debug else 10_000):
            for i in range(5):
                self.var += 1

            if self.debug:
                print("Wert von Var: ", self.var)

        '''
      Diese Methode subtrahiert 5 von der Variable var
      in einer Schleife von 1_000_000 Iterationen, indem die Variable
      je 5 Mal um 1 verringert wird. Wenn debug=True, wird die Schleife
      nur 10_000 Mal durchlaufen (Zeitgründe).
      '''


    def subtract(self):
        for i in range(1_000_000 if not self.debug else 10_000):
            for i in range(5):
                self.var -= 1


    def run(self):
        threads = []
        for i in range(self.num_threads):  # Starte die spezif. Anzahl an Threads
            if i % 2 == 0:  # Addiere die Hälfte der Zeit, Subtrahiere die andere
                threads.append(threading.Thread(target=self.add))
            else:
                threads.append(threading.Thread(target=self.subtract))

        for thread in threads:  # Starte alle Threads
            thread.start()

        for thread in threads:  # Warte auf alle Threads
            thread.join()

        for i in range(self.num_threads):  # Gebe aus, wenn alle Threads gejoined sind
            print(f"Thread Nr. {i} joined")

        print(f"var: {self.var}")  # Gebe das Ergebnis aus.


# Testen der Klasse
# my_class = MyClass(debug=True, num_threads=20)
my_class = MyClass(num_threads=19, debug=True)
my_class.run()
