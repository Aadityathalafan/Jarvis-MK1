import speech_recognition as sr
from colorama import Fore, Style
from mtranslate import translate

def listen():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print(Fore.GREEN + "Listening..." + Style.RESET_ALL)
        # Adjust for ambient noise and listen for audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(Fore.CYAN + f"Boss : {text.lower()}" + Style.RESET_ALL)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            return None

def translate_hindi_to_english(hindi_text):
    # Translate Hindi text to English
    english_translation = translate(hindi_text, 'en', 'hi').lower()
    return english_translation

# Example usage
if __name__ == "__main__":
    hindi_input = listen()
    if hindi_input:
        english_output = translate_hindi_to_english(hindi_input)
        print(Fore.GREEN + f"You said : {english_output}" + Style.RESET_ALL)


#took 1.5 hrs to make this by studing documentation