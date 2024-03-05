import time
import sys

def fake_update_screen():
    print("Starting fake update...")
    for i in range(101):
        time.sleep(0.1)  # Adjust time for effect
        sys.stdout.write("\rUpdating... {}%".format(i))
        sys.stdout.flush()
    print("\n Virus Uploaded.")

if __name__ == "__main__":
    fake_update_screen()
