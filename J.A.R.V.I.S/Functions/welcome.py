from Computation.speak import speak
from Computation.dlg import *
import random

def welcome():
    welcome = random.choice(welcome_dlg)
    speak(welcome)