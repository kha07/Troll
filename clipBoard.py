import pyperclip
import time
from random import randint
import random

def ClipBoard():
    clipboard_messages = [
    "Try copying that again!",
    "Clipboard interception protocol activated.",
    "This message will self-destruct in 5 seconds.",
    "Did you mean to copy this?",
    "Your clipboard has been compromised.",
    "Error 404: Clipboard not found.",
    "This is not the text you are looking for.",
    "Please refrain from copying unauthorized content.",
    "Clipboard sanitization complete.",
    "Warning: Clipboard is currently full.",
    "System alert: Unusual activity detected in clipboard.",
    "Congratulations, you've discovered the secret message!",
    "This clipboard is under surveillance.",
    "Access denied. Your copy privileges have been revoked.",
    "Clipboard content quarantined for security reasons.",
    "Automated response: Please do not copy that again.",
    "Security breach detected. Please secure your clipboard.",
    "Clipboard contents replaced for your protection.",
    "Error: Unable to retain copied data.",
    "Please don't steal text.",
    "System overload. Clipboard functionality compromised.",
    "Copying is prohibited by the Clipboard Management Authority.",
    "Alert: This content is classified. Your IP has been logged.",
    ]

    time.sleep(1)
    try:
        while True:
            print(random.choice(clipboard_messages))
            time.sleep(randint(60, 300))  # Random wait between 1 and 5 minutes
    except KeyboardInterrupt:
        print("Console text ghost stopped.")


ClipBoard()