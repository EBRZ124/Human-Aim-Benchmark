import pygame, sys, global_variables, time, random
from buttons import Button

pygame.init()
clock = pygame.time.Clock()
resolutions_4_3 = [
    (1008, 756),
    (1224, 918),
    (1440, 1080)
]

current_resolution = 2
pygame.display.set_caption("Human Benchmark")
screen_scaler = global_variables.global_scaler
screen = pygame.display.set_mode(resolutions_4_3[current_resolution])

global_variables.load_assets()
global_variables.apply_scaling()

def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["main_menu_bg"], (0, 0))
        PLAY_BUTTON = Button(image=None, pos=(720*screen_scaler, 540*screen_scaler),
                        text_input="PLAY", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="#E57B1E", hovering_color="White")
        
        for button in [PLAY_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    circles_numbers_timed()

        pygame.display.update()

def new_cricle_x():
    circle_pos_x = random.randint(130, 1290)
    return circle_pos_x

def new_cricle_y():
    circle_pos_y = random.randint(95, 980)
    return circle_pos_y

def circles_numbers_timed():
    ShowStartScreen = True
    running = False
    wait = False
    screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
    screen.blit(global_variables.images["playing_area"], (0, 0))


    while ShowStartScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ShowStartScreen = False
                    running = True
                    circle_pos_x = new_cricle_x()
                    circle_pos_y = new_cricle_y()
                if event.key == pygame.K_ESCAPE:
                    ShowStartScreen = False

        pygame.display.update()

    while running:
        dt = clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()

        circle = Button(image=global_variables.images["circle"], pos=(circle_pos_x, circle_pos_y), text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
        circle.update(screen)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if circle.checkForInput(mouse_pos):
                    circle_pos_x= new_cricle_x()
                    circle_pos_y= new_cricle_y()
                    circle = Button(image=global_variables.images["circle"], pos=(circle_pos_x, circle_pos_y), text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
                    circle.update(screen)

        pygame.display.update()

main_menu()