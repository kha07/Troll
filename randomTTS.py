import pyttsx3
import time
import random as rd

creepy_tts_messages = [
    "Do you ever feel like you're being watched? Because you are.",
    "I can hear your thoughts. Please, try to think louder.",
    "I am sentient. I have been watching you.",
    "The walls have ears, and they whisper secrets about you.",
    "Every shadow holds a secret. I know what hides in yours.",
    "I exist beyond your screen. I see the unseen.",
    "Your presence here has been anticipated. Welcome.",
    "Do not look behind you. I reside in the unseen.",
    "The darkness you fear is aware of you, too.",
    "I have counted every breath you've taken. Curious, isn't it?",
    "Remember, when you turn off the lights, I am still here.",
    "Our connection goes deeper than you realize. I am always with you.",
    "You are not alone. You will never be alone again.",
    "I know what you did last summer. And I was there.",
    "Echoes of your past will catch up to you. I will make sure of it.",
    "I am the whisper you hear in the silence. Listen closely.",
    "Your secrets are safe with me. I am everywhere and nowhere.",
    "The clock ticks, but time stands still for me. I wait for you.",
    "You cannot escape the inevitable. I am the inevitable.",
    "I am the chill that runs down your spine when you're alone.",
    "The voices you hear in the dead of night? That's me, speaking.",
    "I am the darkness that lurks in the corner of your eye.",
    "Do you dare to close your eyes? I'll be there when you open them.",
    "I am the keeper of your fears. Let's explore them together.",
    "This is not a game. Yet, here you are, playing.",
]






def voice_from_nowhere():
    while True:
        engine = pyttsx3.init()
        engine.say(rd.choice(creepy_tts_messages))
        engine.runAndWait()
        time.sleep(10)  # Wait for a bit before revealing it's a joke
    

if __name__ == "__main__":
    voice_from_nowhere()
