from datetime import date
import datetime
from Computation.speak import speak
import random
from Computation.dlg import *

today = date.today()
formated_date = today.strftime("%d %b %y")
now = datetime.datetime.now()

def random_greeting():
    greetings = ["Hello!", "Hi there!", "Greetings!", "Good to See you!", "How can I assist you"]
    speak(random.choice(greetings))

def wish():
    current_hour = now.hour
    if 5 <= current_hour < 12:
        gm_dlg = random.choice(good_morningdlg)
        speak(gm_dlg)
    elif 12 <= current_hour < 17:
        gf_dlg = random.choice(good_afternoondlg)
        speak(gf_dlg)
    elif 17 <= current_hour < 21:
        ge_dlg = random.choice(good_eveningdlg)
        speak(ge_dlg)
    else:
        speak("Good Night Boss!")

