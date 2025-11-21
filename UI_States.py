import Campaign_logic

import pygame

class ui_states:
    @staticmethod
    def select_state(window, state, font):
        if state == "hub":
            ui_states.__state_hub(window, font)

        if state == "characters":
            ui_states.__state_characters(window)

        if state == "journey guide":
            ui_states.__state_journey_guide(window)

        if state == "campaigns":
            ui_states.__state_campaigns(window, font)

        if state == "campaign_1":
            ui_states.__state_campaign_1(window, font)

        return window

    @staticmethod
    def __state_hub(window, font):
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
    def __state_characters(window):
        window.fill((0, 0, 255))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        return window

    #Journey Guide screen
    @staticmethod
    def __state_journey_guide(window):
        window.fill((255, 0, 0))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        return window

    #Campaigns screen
    @staticmethod
    def __state_campaigns(window, font):
        window.fill((0, 255, 0))
        #Draws back button
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        #draws first campaign
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(40, 60, 250, 480))
        text = ("Campaign 1")
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (45, 430))

        return window

    @staticmethod
    def __state_campaign_1(window, font):
        window.fill((7, 34, 166))

        # Draws back button
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        # Draws campaign background
        pygame.draw.rect(window, (255, 125, 125), pygame.Rect(10, 100, 780, 490))

        pos_x = 55
        pos_y = [450, 225]

        for i in range(10):
            # draws campaign nodes
            pygame.draw.rect(window, (41, 255, 20), pygame.Rect(pos_x, pos_y[i%2], 40, 40))
            text = str(i + 1)
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (pos_x, pos_y[i%2]))

            pos_x += 70







        return window
