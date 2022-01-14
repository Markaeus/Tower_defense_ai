import pygame, sys
from button import Button
from play_button import Play_Button
from exit import Exit_Button

pygame.init()

SCREEN = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/bg.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(300, 200),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


# def options():
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
#
#         SCREEN.fill("white")
#
#         OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
#
#         OPTIONS_BACK = Button(image=None, pos=(640, 460),
#                               text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
#
#         OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
#                     main_menu()
#
#         pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # MENU_TEXT = get_font(20).render("MAIN MENU", True, "#b68f40")
        # MENU_RECT = MENU_TEXT.get_rect(center=(200, 100))

        PLAY_BUTTON = Play_Button(image=pygame.image.load("assets/start_btn.png"), pos=(200, 250))
        # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
        #                         text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Exit_Button(image=pygame.image.load("assets/exit.png"), pos=(450, 238))

        # SCREEN.blit(MENU_TEXT, MENU_RECT)

        PLAY_BUTTON.update(SCREEN)
        QUIT_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()