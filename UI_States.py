from tkinter import font

import pygame

class ui_states:
    @staticmethod
    def select_state(window, state, font):
        if state == 0:
            ui_states.__state_0(window, font)

        if state == 1:
            ui_states.__state_1(window)

        if state == 2:
            ui_states.__state_2(window)

        if state == 3:
            ui_states.__state_3(window, font)

        return window

    @staticmethod
    def __state_0(window, font):
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 0, 255), pygame.Rect(0, 0, 350, 400))
        text = ("Characters")
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (30, 350))

        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(0, 425, 350, 175))
        text = ("Journey Guide")
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (15, 550))

        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(375, 0, 425, 600))
        text = ("Campaigns")
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (415, 550))

        return window

    #Characters screen
    @staticmethod
    def __state_1(window):
        window.fill((0, 0, 255))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        return window

    #Journey Guide screen
    @staticmethod
    def __state_2(window):
        window.fill((255, 0, 0))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        return window

    #Campaigns screen
    @staticmethod
    def __state_3(window, font):
        window.fill((0, 255, 0))
        #Draws back button
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        #draws first campaign
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(40, 60, 250, 480))
        text = ("Campaign 1")
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (45, 430))

        return window

