import random
import time
import os
import sys
import csv
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_problem(operation):
    if operation == "addition":
        a = random.randint(2, 100)
        b = random.randint(2, 100)
        return f"{a} + {b}", a + b
    elif operation == "subtraction":
        a = random.randint(2, 100)
        b = random.randint(2, 100)
        return f"{a + b} - {b}", a
    elif operation == "multiplication":
        a = random.randint(2, 12)
        b = random.randint(2, 100)
        return f"{a} x {b}", a * b
    elif operation == "division":
        a = random.randint(2, 12)
        b = random.randint(2, 100)
        product = a * b
        return f"{product} / {a}", b

def main():
    operations = ["addition", "subtraction", "multiplication", "division"]
    time_limit = 120
    start_time = time.time()

    clear_screen()
    print("Zetamac-style Arithmetic Game")
    print("You have 120 seconds. Go!")
    print()

    num_correct = 0
    while time.time() - start_time < time_limit:
        operation = random.choice(operations)
        problem, answer = generate_problem(operation)
        while True:
            clear_screen()
            user_input = input(f"Solve: {problem} = ")
            if user_input.isdigit() and int(user_input) == answer:
                num_correct += 1
                break
            else:
                print("Incorrect, try again.")
                time.sleep(0.1)
    print("Time's up! Your score is", num_correct)

    with open('data.txt', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), num_correct])

if __name__ == "__main__":
    main()

