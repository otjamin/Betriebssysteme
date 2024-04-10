import time
import sys

if len(sys.argv) >= 1:
	while True:
		print(sys.argv[1])
		time.sleep(10)
else: print('Please specify argument after name of program (example: python3 Aufgabe2.py "your argument here ")')
