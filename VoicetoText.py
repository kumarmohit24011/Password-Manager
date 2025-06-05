import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
import datetime

def record_and_save():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        status_label.config(text="Listening... 🎤", fg="blue")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            status_label.config(text="Processing...", fg="orange")
            window.update()

            text = recognizer.recognize_google(audio, language="en-IN")
            print("Recognized Text:", text)

            # Timestamp for file name
            now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"note_{now}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)

            status_label.config(text=f"Note saved as {filename} ✅", fg="green")
            messagebox.showinfo("Success", f"Note saved as:\n{filename}")

        except sr.UnknownValueError:
            status_label.config(text="Could not understand audio ❌", fg="red")
        except sr.RequestError:
            status_label.config(text="Network error ⚠️", fg="red")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")

# GUI Setup
window = tk.Tk()
window.title("Voice to Text Note App")
window.geometry("400x200")
window.configure(bg="#f2f2f2")

label = tk.Label(window, text="🎙️ Tap to Record Note", font=("Arial", 14), bg="#f2f2f2")
label.pack(pady=20)

record_button = tk.Button(window, text="🎤 Start Recording", font=("Arial", 12), command=record_and_save, bg="#4CAF50", fg="white", padx=10, pady=5)
record_button.pack()

status_label = tk.Label(window, text="", font=("Arial", 12), bg="#f2f2f2")
status_label.pack(pady=20)

window.mainloop()
