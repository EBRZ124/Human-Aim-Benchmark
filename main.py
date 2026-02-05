import pygame, sys, global_variables, time, random
import nCirclesTimed, circlesInTIme
from buttons import Button

pygame.init()
clock = pygame.time.Clock()
resolutions_4_3 = [
    (1008, 756),
    (1224, 918),
    (1440, 1080)
]

current_resolution = 1
pygame.display.set_caption("Human Benchmark")
screen_scaler = global_variables.global_scaler
screen = pygame.display.set_mode(resolutions_4_3[current_resolution])

global_variables.load_assets()
global_variables.apply_scaling()

# ------------------------------------------------ HOME SCREEN ------------------------------------------------

def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["main_menu_bg"], (0, 0))
        PLAY_BUTTON = Button(image=global_variables.images["play_button"], pos=(720*screen_scaler, 540*screen_scaler),
                        text_input="", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")

        options_button = Button(image=global_variables.images["options_button"], pos=(720*screen_scaler, 765*screen_scaler),
                        text_input="", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")
        
        exit_button = Button(image=global_variables.images["exit_button_mm"], pos=(80*screen_scaler, 80*screen_scaler),
                        text_input="", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")
        
        for button in [PLAY_BUTTON, options_button, exit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    game_select_n_circles_timed()
                if exit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if options_button.checkForInput(mouse_pos):
                    options_menu()

        pygame.display.update()
# ------------------------------------------------ OPTIONS MENU ------------------------------------------------
def options_menu():

    global current_resolution, screen, screen_scaler
    resolution_images =[global_variables.images["1440res"], global_variables.images["1224res"], global_variables.images["1024res"],
                        global_variables.images["1440res_selected"], global_variables.images["1224res_selected"], global_variables.images["1024res_selected"]]

    while True:
        status_1024 = 2
        status_1224 = 1
        status_1440 = 0

        if current_resolution == 0:
            status_1024 = 5
        elif current_resolution == 1:
            status_1224 = 4
        elif current_resolution == 2:
            status_1440 = 3

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["options_menu_screen"], (0, 0))
        back_button = Button(image=global_variables.images["back_button"], pos=(80*screen_scaler, 80*screen_scaler),
                            text_input="", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")
        
        resolution_1024 = Button(image=resolution_images[status_1024], pos=(275*screen_scaler, 540*screen_scaler),
                            text_input="", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")
        
        resolution_1224 = Button(image=resolution_images[status_1224], pos=(720*screen_scaler, 540*screen_scaler),
                            text_input="", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")
        
        resolution_1440 = Button(image=resolution_images[status_1440], pos=(1165*screen_scaler, 540*screen_scaler),
                            text_input="", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(mouse_pos):
                    main_menu()
                if resolution_1024.checkForInput(mouse_pos):
                    status_1024 = 5
                    status_1224 = 1
                    status_1440 = 0
                    current_resolution = 0
                    screen_scaler = 0.7
                    global_variables.set_global_scaler(screen_scaler)
                    width, height = resolutions_4_3[current_resolution]
                    screen = pygame.display.set_mode((width, height))
                    return options_menu()

                if resolution_1224.checkForInput(mouse_pos):
                    status_1024 = 2
                    status_1224 = 4
                    status_1440 = 0
                    current_resolution = 1
                    screen_scaler = 0.85
                    global_variables.set_global_scaler(screen_scaler)
                    width, height = resolutions_4_3[current_resolution]
                    screen = pygame.display.set_mode((width, height))
                    return options_menu()

                if resolution_1440.checkForInput(mouse_pos):
                    status_1024 = 2
                    status_1224 = 1
                    status_1440 = 3
                    current_resolution = 2
                    screen_scaler = 1
                    global_variables.set_global_scaler(screen_scaler)
                    width, height = resolutions_4_3[current_resolution]
                    screen = pygame.display.set_mode((width, height))
                    return options_menu()
        
        for button in [back_button, resolution_1024, resolution_1224, resolution_1440]:
            button.changeColor(mouse_pos)
            button.update(screen)

        pygame.display.update()

# ------------------------------------------------ BENCHMARK 1 ------------------------------------------------
def game_select_n_circles_timed():
    circle_sizes = [global_variables.images["1x_size_unselected"], global_variables.images["2x_size_unselected"], global_variables.images["3x_size_unselected"],
                    global_variables.images["1x_size_selected"], global_variables.images["2x_size_selected"], global_variables.images["3x_size_selected"]]
    
    # default size
    circle_size_1 = 0
    circle_size_2 = 4
    circle_size_3 = 2
    passed_circle_size = 1
    
    number_of_circles = [global_variables.images["5_circles_unselected"], global_variables.images["10_circles_unselected"], global_variables.images["20_circles_unselected"],
                         global_variables.images["5_circles_selected"], global_variables.images["10_circles_selected"], global_variables.images["20_circles_selected"]]

    # default number of circles
    n_circles_5 = 0
    n_circles_10 = 4
    n_circles_20 = 2 
    passed_n_number = 10

    circles_passed = [global_variables.images["circle_1x"], global_variables.images["circle_2x"], global_variables.images["circle_3x"]]

    # game shown
    game_shown = 1

    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(global_variables.images["level_select_background"], (0, 0))
        screen.blit(global_variables.images["n_circles_timed"], (0, 0))

        back_button_blue = Button(image=global_variables.images["back_button_blue"], pos=(80*screen_scaler, 80*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        back_button_blue.update(screen) 

        # ------------------ LEVEL DIFFICULTIES ------------------
        circle_number_5 = Button(image=number_of_circles[n_circles_5], pos=(234*screen_scaler, 605*screen_scaler), text_input="", 
                            font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        circle_number_5.update(screen) 

        circle_number_10 = Button(image=number_of_circles[n_circles_10], pos=(324*screen_scaler, 605*screen_scaler), text_input="", 
                            font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        circle_number_10.update(screen) 

        circle_number_20 = Button(image=number_of_circles[n_circles_20], pos=(418*screen_scaler, 605*screen_scaler), text_input="", 
                            font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        circle_number_20.update(screen) 


        size_1x = Button(image=circle_sizes[circle_size_1], pos=(235*screen_scaler, 705*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        size_1x.update(screen) 

        size_2x = Button(image=circle_sizes[circle_size_2], pos=(334*screen_scaler, 705*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        size_2x.update(screen) 

        size_3x = Button(image=circle_sizes[circle_size_3], pos=(432*screen_scaler, 705*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        size_3x.update(screen) 

        # --------------------------------------------------------

        play_button = Button(image=global_variables.images["menu_play_button"], pos=(1106*screen_scaler, 885*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        play_button.update(screen)  

        arrow_right_button = Button(image=global_variables.images["arrow_right"], pos=(1377*screen_scaler, 540*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        arrow_right_button.changeColor(mouse_pos)
        arrow_right_button.update(screen)  

        arrow_left_button = Button(image=global_variables.images["arrow_left"], pos=(58*screen_scaler, 540*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        arrow_left_button.changeColor(mouse_pos)
        arrow_left_button.update(screen) 

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    nCirclesTimed.circles_numbers_timed(screen, passed_n_number, circles_passed[passed_circle_size], screen_scaler)
                if arrow_left_button.checkForInput(mouse_pos):
                    game_select_circles_in_time()
                if arrow_right_button.checkForInput(mouse_pos):
                    game_select_circles_in_time()
                if back_button_blue.checkForInput(mouse_pos):
                    main_menu()

                if size_1x.checkForInput(mouse_pos):
                    circle_size_1 = 3
                    circle_size_2 = 1
                    circle_size_3 = 2
                    passed_circle_size = 0
                if size_2x.checkForInput(mouse_pos):
                    circle_size_1 = 0
                    circle_size_2 = 4
                    circle_size_3 = 2
                    passed_circle_size = 1
                if size_3x.checkForInput(mouse_pos):
                    circle_size_1 = 0
                    circle_size_2 = 1
                    circle_size_3 = 5
                    passed_circle_size = 2

                if circle_number_5.checkForInput(mouse_pos):
                    n_circles_5 = 3
                    n_circles_10 = 1
                    n_circles_20 = 2
                    passed_n_number = 5
                if circle_number_10.checkForInput(mouse_pos):
                    n_circles_5 = 0
                    n_circles_10 = 4
                    n_circles_20 = 2
                    passed_n_number = 10
                if circle_number_20.checkForInput(mouse_pos):
                    n_circles_5 = 0
                    n_circles_10 = 1
                    n_circles_20 = 5
                    passed_n_number = 20

        pygame.display.flip()

# ------------------------------------------------ BENCHMARK 2 ------------------------------------------------
def game_select_circles_in_time():
    circle_sizes = [global_variables.images["1x_size_unselected"], global_variables.images["2x_size_unselected"], global_variables.images["3x_size_unselected"],
                    global_variables.images["1x_size_selected"], global_variables.images["2x_size_selected"], global_variables.images["3x_size_selected"]]
    
    # default size
    circle_size_1 = 0
    circle_size_2 = 4
    circle_size_3 = 2
    passed_circle_size = 1

    time_limit = [global_variables.images["5s_limit_unselected"], global_variables.images["10s_limit_unselected"], global_variables.images["20s_limit_unselected"],
                  global_variables.images["5s_limit_selected"], global_variables.images["10s_limit_selected"], global_variables.images["20s_limit_selected"]]

    # default time limit
    time_limit_5 = 0
    time_limit_10 = 4
    time_limit_20 = 2
    time_limit_passed = 10

    circles_passed = [global_variables.images["circle_1x"], global_variables.images["circle_2x"], global_variables.images["circle_3x"]]

    running = True

    while running:
        screen.blit(global_variables.images["level_select_background"], (0, 0))
        screen.blit(global_variables.images["circles_in_time_desc"], (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        events = pygame.event.get()

        back_button_blue = Button(image=global_variables.images["back_button_blue"], pos=(80*screen_scaler, 80*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        back_button_blue.update(screen) 

        # DIFFICULTY SETTINGS
        time_limit_5s = Button(image=time_limit[time_limit_5], pos=(210*screen_scaler, 605*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        time_limit_5s.update(screen) 

        time_limit_10s = Button(image=time_limit[time_limit_10], pos=(324*screen_scaler, 605*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        time_limit_10s.update(screen) 

        time_limit_20s = Button(image=time_limit[time_limit_20], pos=(448*screen_scaler, 605*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        time_limit_20s.update(screen) 

        size_1x = Button(image=circle_sizes[circle_size_1], pos=(235*screen_scaler, 705*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        size_1x.update(screen) 

        size_2x = Button(image=circle_sizes[circle_size_2], pos=(334*screen_scaler, 705*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        size_2x.update(screen) 

        size_3x = Button(image=circle_sizes[circle_size_3], pos=(432*screen_scaler, 705*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(5*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        size_3x.update(screen) 
        # DIFFICULTY SETTINGS

        play_button = Button(image=global_variables.images["menu_play_button"], pos=(1106*screen_scaler, 885*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        play_button.update(screen)  

        arrow_right_button = Button(image=global_variables.images["arrow_right"], pos=(1377*screen_scaler, 540*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        arrow_right_button.changeColor(mouse_pos)
        arrow_right_button.update(screen)  

        arrow_left_button = Button(image=global_variables.images["arrow_left"], pos=(58*screen_scaler, 540*screen_scaler), text_input="", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        arrow_left_button.changeColor(mouse_pos)
        arrow_left_button.update(screen) 

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    circlesInTIme.circles_in_time(screen, time_limit_passed, circles_passed[passed_circle_size], screen_scaler)
                if arrow_left_button.checkForInput(mouse_pos):
                    game_select_n_circles_timed()
                if arrow_right_button.checkForInput(mouse_pos):
                    game_select_n_circles_timed()
                if back_button_blue.checkForInput(mouse_pos):
                    main_menu()

                if size_1x.checkForInput(mouse_pos):
                    circle_size_1 = 3
                    circle_size_2 = 1
                    circle_size_3 = 2
                    passed_circle_size = 0
                if size_2x.checkForInput(mouse_pos):
                    circle_size_1 = 0
                    circle_size_2 = 4
                    circle_size_3 = 2
                    passed_circle_size = 1
                if size_3x.checkForInput(mouse_pos):
                    circle_size_1 = 0
                    circle_size_2 = 1
                    circle_size_3 = 5
                    passed_circle_size = 2

                if time_limit_5s.checkForInput(mouse_pos):
                    time_limit_5 = 3
                    time_limit_10 = 1
                    time_limit_20 = 2
                    time_limit_passed = 5
                if time_limit_10s.checkForInput(mouse_pos):
                    time_limit_5 = 0
                    time_limit_10 = 4
                    time_limit_20 = 2
                    time_limit_passed = 10
                if time_limit_20s.checkForInput(mouse_pos):
                    time_limit_5 = 0
                    time_limit_10 = 1
                    time_limit_20 = 5
                    time_limit_passed = 20

        pygame.display.flip()

def new_cricle_x():
    circle_pos_x = random.randint(160, 1270)*screen_scaler
    return circle_pos_x

def new_cricle_y():
    circle_pos_y = random.randint(150, 940)*screen_scaler
    return circle_pos_y

main_menu()