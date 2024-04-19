import os
import signal
import time
from datetime import datetime


def handle_signal(sig, frame):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Empfangen von Signal {signal.Signals(sig).name} um {timestamp}")


def handle_signal_sighup(sig, frame):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Spezifischere Behandlung
    print(f"SIGHUP wurde Empfangen: {signal.Signals(sig).name} um {timestamp}")


# Signal-Handler registrieren
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGUSR1, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)  # Terminierungssignal (Standardmäßig verwendet, um Prozesse zu beenden)
signal.signal(signal.SIGHUP,
              handle_signal_sighup)  # Hangup-Signal (oft verwendet, um Prozesse zu informieren,  dass sie neu starten sollen)
print(f"Die Prozess-ID lautet: {os.getpid()}")  # Zur einfacheren Erkennung der PID

while True:
    print("Schlafen für 10 Sekunden...")
    time.sleep(10)
