import pygame
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.mixer.fadeout(999)
input()
