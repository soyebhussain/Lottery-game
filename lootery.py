import time
import random
from datetime import datetime

log_file = "lottery_log.txt"

participants = []

def is_valid(username):
    if username == "":
        return False
    if not username.isalnum() and "_" not in username:
        return False
    return True

def register_users(duration_seconds):
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        remaining = int(duration_seconds - (time.time() - start_time))
        print("Time left:", remaining // 60, "minutes", remaining % 60, "seconds")

        username = input("Enter your username: ").strip()

        if not is_valid(username):
            print("Invalid username. Only letters, numbers, and underscores allowed.")
            continue

        if username in participants:
            print("Username already registered. Please choose a different one.")
            continue

        participants.append(username)
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - Registered: {username}\n")
        print("User registered successfully. Total:", len(participants))

        time.sleep(1)  

def pick_winner():
    if len(participants) == 0:
        print("No users registered. Exiting the program.")
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - No users registered. Program ended.\n")
        return

    winner = random.choice(participants)
    print("\nLottery Closed.")
    print("Total Participants:", len(participants))
    print("Winner is:", winner)

    with open(log_file, "a") as f:
        f.write(f"\n{datetime.now()} - Winner: {winner}\n")
        f.write(f"Total Participants: {len(participants)}\n")

print("---Welcome to the Lottery System---")
print("Registration is open for 1 hour (60 minutes).")

register_users(60 * 60)


if len(participants) < 5:
    print("Less than 5 users registered. Extending registration by 30 minutes.")
    register_users(30 * 60)


pick_winner()
