import asyncio
import threading
import os
import edge_tts
import pygame
import sys
import time

#"en-US-JennyNeural"
VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.085)
    print()

def remove_file(filepath):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(filepath, "wb"):
                pass
            os.remove(filepath)
            break
        except Exception as e:
            print(f"error : {e}")
            attempts += 1

async def amain(TEXT, output_file) -> None:
    try:
        cm_text = edge_tts.Communicate(TEXT, VOICE)
        await cm_text.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
        print(f"error : {e}")
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()

        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

        pygame.quit()
    except Exception as e:
        print(f"error : {e}")

def speak1(TEXT, output_file=None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"
    asyncio.run(amain(TEXT, output_file))

def speak(text):
    t1 = threading.Thread(target=speak1, args=(text,))  # Pass 'text' as a tuple
    t2 = threading.Thread(target=print_animated_message, args=(text,))  # Pass 'text' as a tuple
    t1.start()
    t2.start()

    t1.join()
    t2.join()


