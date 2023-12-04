import tkinter as tk
from tkinter import filedialog
from playsound import playsound
import threading

class MusicPlayerApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Music Player")

        self.selected_music_file = None
        self.music_playing = False

        self.create_widgets()

    def create_widgets(self):
        # Label to display the currently playing music
        self.current_music_label = tk.Label(self.master, text="Now Playing: None")
        self.current_music_label.pack(pady=10)

        # Buttons
        self.play_button = tk.Button(self.master, text="Play Music", command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop Music", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.choose_file_button = tk.Button(self.master, text="Choose Music File", command=self.choose_music_file)
        self.choose_file_button.pack(pady=10)

    def play_music(self):
        if not self.music_playing and self.selected_music_file:
            self.music_playing = True
            # Use threading to play music in the background
            threading.Thread(target=self.play_music_thread).start()

    def play_music_thread(self):
        try:
            playsound(self.selected_music_file)
            self.current_music_label.config(text=f"Now Playing: None")
        except Exception as e:
            self.current_music_label.config(text=f"Error: {e}")
        finally:
            self.music_playing = False

    def stop_music(self):
        # Currently, there is no direct way to stop playsound library
        # You might want to use a different library or implement your own player for more control
        pass

    def choose_music_file(self):
        self.selected_music_file = filedialog.askopenfilename(
            initialdir="/", title="Select Music File",
            filetypes=(("MP3 files", "*.mp3"), ("all files", "*.*"))
        )
        self.current_music_label.config(text=f"Now Playing: {self.selected_music_file}")

if __name__ == "_main_":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()