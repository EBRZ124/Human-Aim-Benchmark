import pygame, sys, global_variables, time, random
from buttons import Button

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

def new_cricle_x(screen_scaler):
    circle_pos_x = random.randint(160, 1270)*screen_scaler
    return circle_pos_x

def new_cricle_y(screen_scaler):
    circle_pos_y = random.randint(150, 940)*screen_scaler
    return circle_pos_y

def circles_in_time(screen, time_limit, circle_passed, screen_scaler):
    level_start_time = pygame.time.get_ticks()
    running = True
    circle_pos_x = new_cricle_x(screen_scaler)
    circle_pos_y = new_cricle_y(screen_scaler)
    score = 0

    while running:
        dt = clock.tick(60)
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
        screen.blit(global_variables.images["playing_area"], (0, 0))

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - level_start_time) / 1000

        circle = Button(image=circle_passed, pos=(circle_pos_x, circle_pos_y), 
                        text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
        circle.update(screen)

        font = pygame.font.Font(None, int(60*screen_scaler))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (121*screen_scaler, 30*screen_scaler))

        displayed_time = round(elapsed_time, 1)

        time_text = font.render(f"Time: {displayed_time}s", True, (255, 255, 255))
        screen.blit(time_text, (1100*screen_scaler, 30*screen_scaler))

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
                    circle_pos_x= new_cricle_x(screen_scaler)
                    circle_pos_y= new_cricle_y(screen_scaler)
                    circle = Button(image=circle_passed, pos=(circle_pos_x, circle_pos_y), text_input="", font=global_variables.get_main_menu_font(2), base_color="White", hovering_color="White")
                    circle.update(screen)

        if elapsed_time >= time_limit:
            running = False
            result_circles_numbers_timed(screen, score, time_limit, circle_passed, screen_scaler)

        pygame.display.flip()

def result_circles_numbers_timed(screen, score, time_limit, circle_passed, screen_scaler):
    results = True
    while results:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(global_variables.images["circle_numbers_timed_bg"], (0, 0))
        screen.blit(global_variables.images["result_screen"], (0, 0))

        result_average = score

        hit_time_average = global_variables.result_screen_font(int(55*screen_scaler)).render(f"Your score: {result_average} hits", True, "White")
        hit_average_rect = hit_time_average.get_rect(center=(720*screen_scaler, 430*screen_scaler))
        screen.blit(hit_time_average, hit_average_rect)

        time_spent_text = global_variables.result_screen_font(int(55*screen_scaler)).render(f"Time limit: {time_limit} sec", True, "White")
        time_spen_rect = time_spent_text.get_rect(center=(720*screen_scaler, 550*screen_scaler))
        screen.blit(time_spent_text, time_spen_rect)

        hit_average_score = round(score/time_limit, 2)
        
        hits_per_second = global_variables.result_screen_font(int(55*screen_scaler)).render(f"Hits per second: {hit_average_score}", True, "White")
        hits_per_second_rect = hits_per_second.get_rect(center=(720*screen_scaler, 680*screen_scaler))
        screen.blit(hits_per_second, hits_per_second_rect)

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