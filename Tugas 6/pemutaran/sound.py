import tkinter as tk
from tkinter import filedialog
import pygame.mixer

class MP3Player:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Player")
        self.root.geometry("400x300")

        self.create_buttons()
        self.create_volume_slider()

    def create_buttons(self):
        play_button = tk.Button(self.root, text="Play", command=self.play_mp3)
        play_button.pack(side=tk.LEFT, padx=10)

        pause_button = tk.Button(self.root, text="Pause", command=self.pause_mp3)
        pause_button.pack(side=tk.LEFT, padx=10)

        resume_button = tk.Button(self.root, text="Resume", command=self.resume_mp3)
        resume_button.pack(side=tk.LEFT, padx=10)

        stop_button = tk.Button(self.root, text="Stop", command=self.stop_mp3)
        stop_button.pack(side=tk.LEFT, padx=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(side=tk.RIGHT, padx=10)

    def create_volume_slider(self):
        volume_label = tk.Label(self.root, text="Volume")
        volume_label.pack(pady=5)

        self.volume_slider = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL)
        self.volume_slider.set(70)
        self.volume_slider.pack(pady=10)

    def play_mp3(self):
        file_path = filedialog.askopenfilename(filetypes=[("mp3 Files", "*.mp3")])
        if file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(self.volume_slider.get() / 100)
            pygame.mixer.music.play()

    def pause_mp3(self):
        pygame.mixer.music.pause()

    def resume_mp3(self):
        pygame.mixer.music.unpause()

    def stop_mp3(self):
        pygame.mixer.music.stop()
        pygame.mixer.quit()


if __name__ == "__main__":
    root = tk.Tk()
    mp3_player = MP3Player(root)
    root.mainloop()
