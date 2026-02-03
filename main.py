import pygame, sys, global_variables, time, random
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

def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["main_menu_bg"], (0, 0))
        PLAY_BUTTON = Button(image=None, pos=(720*screen_scaler, 540*screen_scaler),
                        text_input="PLAY", font=global_variables.get_main_menu_font(int(75*screen_scaler)), base_color="White", hovering_color="White")
        
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
    circle_pos_x = random.randint(160, 1270)*screen_scaler
    return circle_pos_x

def new_cricle_y():
    circle_pos_y = random.randint(150, 940)*screen_scaler
    return circle_pos_y

def circles_numbers_timed():
    ShowStartScreen = True
    running = False
    wait = False
    score = 0

    while ShowStartScreen:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
        screen.blit(global_variables.images["background_dimmer"], (0, 0))
        screen.blit(global_variables.images["n_circles_timed"], (0, 0))

        start_button = Button(image=global_variables.images["start_button"], pos=(720*screen_scaler, 900*screen_scaler), text_input="START LVL", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        start_button.changeColor(mouse_pos)
        start_button.update(screen)  

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkForInput(mouse_pos):
                    ShowStartScreen = False
                    running = True
                    circle_pos_x = new_cricle_x()
                    circle_pos_y = new_cricle_y()                

        pygame.display.flip()

    start_time = pygame.time.get_ticks()
    while running:
        dt = clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
        screen.blit(global_variables.images["playing_area"], (0, 0))

        circle = Button(image=global_variables.images["circle"], pos=(circle_pos_x, circle_pos_y), text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
        circle.update(screen)

        font = pygame.font.Font(None, int(60*screen_scaler))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (121*screen_scaler, 30*screen_scaler))

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
                    score += 1
                    circle_pos_x= new_cricle_x()
                    circle_pos_y= new_cricle_y()
                    circle = Button(image=global_variables.images["circle"], pos=(circle_pos_x, circle_pos_y), text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
                    circle.update(screen)

        if score == 20:
            running = False
            end_time = pygame.time.get_ticks()
            final_time = (end_time-start_time)/1000
            result_circles_numbers_timed(final_time)

        pygame.display.flip()

def result_circles_numbers_timed(time_spent):
    results = True
    while results:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
        screen.blit(global_variables.images["result_screen"], (0, 0))

        result_average = time_spent/20

        hit_time_average = global_variables.result_screen_font(int(55*screen_scaler)).render(f"Hit time average: {result_average} sec", True, "White")
        hit_average_rect = hit_time_average.get_rect(center=(720*screen_scaler, 430*screen_scaler))
        screen.blit(hit_time_average, hit_average_rect)

        time_spent_text = global_variables.result_screen_font(int(55*screen_scaler)).render(f"Time spent: {time_spent} sec", True, "White")
        time_spen_rect = time_spent_text.get_rect(center=(720*screen_scaler, 620*screen_scaler))
        screen.blit(time_spent_text, time_spen_rect)

        exit_button = Button(image=global_variables.images["exit_button"], pos=(720*screen_scaler, 860*screen_scaler), text_input="Exit level", 
                             font = global_variables.get_main_menu_font(int(50*screen_scaler)), base_color="White", hovering_color="#D3FCFE")
        exit_button.changeColor(mouse_pos)
        exit_button.update(screen)  

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    results = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.checkForInput(mouse_pos):
                    results = False

        pygame.display.flip()

main_menu()