import os

N = 3
pids = []  # Liste für Kind-Prozess-IDs

for i in range(N):
    pid = os.fork()
    if pid == 0:
        for j in range(200):
            print(f"Kind {i + 1} mit PID={os.getpid()}")
        exit(0)
    else:
        pids.append(pid)

for i in range(200):
    print(f"Vater mit PID={os.getpid()}: PID1={pids[0]}, PID2={pids[1]}, PID3={pids[2]}")
