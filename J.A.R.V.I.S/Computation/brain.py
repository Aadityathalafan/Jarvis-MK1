from model1 import mind
from speak import speak
import wikipedia  # Correct import
from wikipedia.exceptions import DisambiguationError, PageError  # Handle Wikipedia-specific exceptions
import threading
import sys
import time
import webbrowser
import traceback  # For detailed error output

def load_qna_data(file_path):
    qa_dict = {}
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict

qna_file_path = r"C:\Users\user\OneDrive\Desktop\J.A.R.V.I.S\Computation\qna_data.txt"
qa_dict = load_qna_data(qna_file_path)

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)
    print()

def save_qa_data(file_path, qa_dict):
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")

def wiki_search(prompt):
    search_prompt = prompt.replace("jarvis", "").replace("wikipedia", "").strip()  # Ensure search_prompt is clean
    
    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)
        animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))  # Fixed argument format

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        qa_dict[search_prompt] = wiki_summary
        save_qa_data(qna_file_path, qa_dict)

    except DisambiguationError as e:  # Using correct Wikipedia exception
        speak("There is a Disambiguation page for the given query. Please provide more information.")
        print("There is a Disambiguation page for the given query. Please provide more information.")

    except PageError:  # Correct Wikipedia exception
        google_search(prompt)

def google_search(query):
    query = query.replace("who is", "").strip()  # Correct strip call placement

    if query:
        url = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(url)
        speak("You can see results on " + query + " in Google on your screen")
        print("You can see results on " + query + " in Google on your screen")

    else:
        speak("I didn't catch what you said")
        print("I didn't catch what you said")



