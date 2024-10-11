from speak import *
from listen import *
from model1 import mind
from Functions.wish import wish
from Functions.welcome import *
from dlg import wake_key_word, bye_key_word, res_bye
import random
from Automation.open import open
from Automation.close import close

def jarvis():
    wish()
    while True:
        text = listen()
        if text:  
            text = text.lower()
            if text in wake_key_word:
                welcome()
            elif text in bye_key_word:
                res_random = random.choice(res_bye)
                speak(res_random)
                break
            elif text.startswith(("jarvis","bro","")):
                text.replace("","")
                text = mind(text)
                speak(text)
            
            elif text.endswith(("jarvis","buddy","jar","bro")):
                text = text.replace("jarvis","")
                text = text.replace("jar","")
                text = text.replace("bro","")
                text = text.replace("buddy","")
                text = text.strip()
                text = mind(text)
                speak(text)

            elif text.startswith(("open","kholo","show me")):
                text = text.replace("kholo","")
                text = text.replace("show me","")
                text = text.strip()
                open(text)

            elif text in open_input:
                text = text.replace("kholo", "")
                text = text.replace("jarvis", "")
                text = text.strip()
                open(text)

            elif text in close_dlg:
                close()

            else:
                pass


jarvis()
