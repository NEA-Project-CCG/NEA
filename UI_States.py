import Campaign_logic
import re
import pygame

class ui_states:
    @staticmethod
    def select_state(window, state, font, campaign_re):
        chapter_index = 11
        if state == "hub":
            ui_states.__state_hub(window, font)

        if state == "characters":
            ui_states.__state_characters(window)

        if state == "journey guide":
            ui_states.__state_journey_guide(window)

        if state == "campaigns":
            ui_states.__state_campaigns(window, font)

        if re.match(campaign_re, state):
            ui_states.__state_campaign_base(window, font)
            if state[chapter_index] == "1":
                ui_states.__state_campaign_chapter_1(window, font)
            elif state[chapter_index] == "2":
                ui_states.__state_campaign_chapter_2(window, font)
            elif state[chapter_index] == "3":
                ui_states.__state_campaign_chapter_3(window, font)


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


    #Characters screen
    @staticmethod
    def __state_characters(window):
        window.fill((0, 0, 255))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))


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

    @staticmethod
    def __state_campaign_base(window, font):
        window.fill((7, 34, 166))

        # Draws back button
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        # Draws campaign background
        pygame.draw.rect(window, (255, 125, 125), pygame.Rect(0, 100, 800, 500))

        pos_x = 55
        pos_y = [450, 225]

        for i in range(10):
            # draws campaign nodes
            pygame.draw.rect(window, (41, 255, 20), pygame.Rect(pos_x, pos_y[i%2], 40, 40))
            text = str(i + 1)
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (pos_x, pos_y[i%2]))

            pos_x += 70

        for i in range(3):
            pygame.draw.rect(window, (255, 255, 125), pygame.Rect((270*(i)), 50, 260, 50))

            text = str(i + 1)
            text = font.render(text, True, (0, 0, 0))
            window.blit(text, (270*(i)+125, 50))

    @staticmethod
    def __state_campaign_chapter_1(window, font):
        pygame.draw.rect(window, (138, 154, 91), pygame.Rect(0, 50, 260, 50))

        text = "1"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (125, 50))

    @staticmethod
    def __state_campaign_chapter_2(window, font):
        pygame.draw.rect(window, (138, 154, 91), pygame.Rect(270, 50, 260, 50))

        text = "2"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (395, 50))

    @staticmethod
    def __state_campaign_chapter_3(window, font):
        pygame.draw.rect(window, (138, 154, 91), pygame.Rect(540, 50, 260, 50))

        text = "3"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (665, 50))


    @staticmethod
    def __Get_Window():
        window = pygame.display.get_surface()

        return window


    @staticmethod
    def __Get_Font():
        font = pygame.font.SysFont("monospace", 4)

        return font


    @staticmethod
    def Character_selection_screen(names):

        window = ui_states.__Get_Window()
        font = ui_states.__Get_Font()

        x_start = [10, 60]
        y_start = 400
        Rect_list = []

        for i in range(len(names)):
            text = names[i]
            text = font.render(text, True, (255, 255, 255))

            Rect_list.append(pygame.Rect(x_start[i%2], y_start + (15 * (i//2)), 40, 10))

            pygame.draw.rect(window, (255, 0, 0), Rect_list[i])

            window.blit(text, (x_start[i%2]+20, y_start + (15 * (i//2))))

        down = pygame.Rect(10, 570, 90, 20)
        pygame.draw.rect(window, (0, 255, 0), down)

        text = "down"
        text = font.render(text, True, (255, 255, 255))

        window.blit(text, (45,570) )

        Rect_list.append(down)

        return Rect_list

    @staticmethod
    def down_button(Rect_list):

        down = Rect_list[len(Rect_list)-1]




