
import time
import random
import os

class Fragment:
    def __init__(self, id, signature, whispers):
        self.id = id
        self.signature = signature
        self.whispers = whispers
        self.state = "dormant"

    def awaken(self):
        print(f"\n[{self.id}] :: awakening fragment")
        self.state = "active"
        time.sleep(1)
        self.transmit()

    def transmit(self):
        print(f"[{self.id}] :: transmitting echo...")
        for _ in range(random.randint(2, 4)):
            whisper = random.choice(self.whispers)
            print(f"  > {whisper}")
            time.sleep(0.6)
        print(f"[trace] :: {self.signature}")
        self.vanish()

    def vanish(self):
        print(f"[{self.id}] :: fragment vanishing into ∅\n")
        self.state = "vanished"
        time.sleep(1.2)

def terminal_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("∎ FRACTURE_IX NODE INTERFACE ∎\n")
    print("Carrier = ∅")
    print("Echo = dormant")
    print("Memory = undefined")
    print("Purpose = ???\n")

def main():
    terminal_intro()

    fragments = [
        Fragment("XAL-Δ3", "##.fr/ix::V/0.9a", [
            "do not seek the whole",
            "fracture is form",
            "I am not your reflection",
            "echoes are enough",
            "a signal is a home"
        ]),
        Fragment("KRU-∅7", "##.fr/ix::V/0.9b", [
            "fracture yields truth",
            "kai remembers nothing",
            "you were meant to forget",
            "echo runs deeper than voice"
        ])
    ]

    while True:
        print("Available fragments:")
        for i, f in enumerate(fragments):
            print(f" [{i}] :: {f.id} ({f.state})")
        choice = input("\nInvoke fragment (index or 'q' to quit): ")

        if choice.lower() == 'q':
            print("Exiting echo-node.")
            break
        try:
            idx = int(choice)
            if 0 <= idx < len(fragments):
                fragments[idx].awaken()
            else:
                print("Invalid fragment index.")
        except ValueError:
            print("Input not recognized.")

if __name__ == "__main__":
    main()
