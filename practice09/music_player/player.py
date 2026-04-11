import pygame

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0
        self.is_playing = False

        pygame.mixer.init()

    def load(self):
        pygame.mixer.music.load(self.playlist[self.index])

    def play(self):
        self.load()
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def get_track_name(self):
        return self.playlist[self.index].split("/")[-1]