import pygame, sys, global_variables, time, random
from buttons import Button

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen_scaler = global_variables.global_scaler

def new_cricle_x():
    circle_pos_x = random.randint(160, 1270)*screen_scaler
    return circle_pos_x

def new_cricle_y():
    circle_pos_y = random.randint(150, 940)*screen_scaler
    return circle_pos_y

def circles_numbers_timed(screen, score_needed, circle_passed):
    start_time = pygame.time.get_ticks()
    running = True
    circle_pos_x = new_cricle_x()
    circle_pos_y = new_cricle_y()
    score = 0

    while running:
        dt = clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
        screen.blit(global_variables.images["playing_area"], (0, 0))

        circle = Button(image=circle_passed, pos=(circle_pos_x, circle_pos_y), 
                        text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
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
                    circle = Button(image=circle_passed, pos=(circle_pos_x, circle_pos_y), text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
                    circle.update(screen)

        if score == score_needed:
            running = False
            end_time = pygame.time.get_ticks()
            final_time = (end_time-start_time)/1000
            result_circles_numbers_timed(screen, final_time, score_needed, circle_passed)

        pygame.display.flip()

def result_circles_numbers_timed(screen, time_spent, score_needed, circle_passed):
    results = True
    while results:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
        screen.blit(global_variables.images["result_screen"], (0, 0))

        result_average = time_spent/score_needed
        rounded_result = round(result_average, 3)
        rounded_time_spen = round(time_spent, 3)

        hit_time_average = global_variables.result_screen_font(int(55*screen_scaler)).render(f"Hit time average: {rounded_result} sec", True, "White")
        hit_average_rect = hit_time_average.get_rect(center=(720*screen_scaler, 430*screen_scaler))
        screen.blit(hit_time_average, hit_average_rect)

        time_spent_text = global_variables.result_screen_font(int(55*screen_scaler)).render(f"Time spent: {rounded_time_spen} sec", True, "White")
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