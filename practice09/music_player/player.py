import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        pygame.mixer.init()
        self.music_dir = music_dir
        self.playlist = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        self.current_index = 0
        self.paused = False

    def play(self):
        if not self.playlist:
            print("Список воспроизведения пуст!")
            return
            
        path = os.path.join(self.music_dir, self.playlist[self.current_index])
        
        if not os.path.exists(path):
            print(f"Ошибка: Файл {path} не найден!")
            return

        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            try:
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
            except pygame.error as e:
                print(f"Не удалось загрузить файл: {e}")

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        return self.playlist[self.current_index] if self.playlist else "No tracks"