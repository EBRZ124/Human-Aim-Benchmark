import pygame
pygame.init()
pygame.mixer.init()

global_scaler = 0.85

original_images = {}

images = {}

def load_assets():
    global original_images

    if original_images:
        return
    
    original_images = {
        # ------------------------ HOME SCREEN ASSETS ------------------------
        "main_menu_bg": pygame.image.load("../human_benchmark/graphics/main_bg.png"),
        "play_button": pygame.image.load("../human_benchmark/graphics/play_button.png"),
        "options_button": pygame.image.load("../human_benchmark/graphics/options_button.png"),
        "exit_button_mm": pygame.image.load("../human_benchmark/graphics/exit_button.png"),

        # ------------------------ MENU SCREEN ASSETS ------------------------
        "level_select_background": pygame.image.load("../human_benchmark/graphics/level_select_background.png"),
        "circle_numbers_timed_bg": pygame.image.load("../human_benchmark/graphics/circle_numbers_timed_bg.png"),
        "circles_in_time_bg": pygame.image.load("../human_benchmark/graphics/circles_int_time_bg.png"),
        "background_dimmer": pygame.image.load("../human_benchmark/graphics/background_dimmer.png"),
        "playing_area": pygame.image.load("../human_benchmark/graphics/playing_area.png"),
        "n_circles_timed": pygame.image.load("../human_benchmark/graphics/n_circles_timed.png"),
        "circles_in_time_desc": pygame.image.load("../human_benchmark/graphics/circles_in_time_desc.png"),
        "start_button": pygame.image.load("../human_benchmark/graphics/start_level_button.png"),
        "arrow_right": pygame.image.load("../human_benchmark/graphics/arrow_right.png"),
        "arrow_left": pygame.image.load("../human_benchmark/graphics/arrow_left.png"),
        "back_button_blue": pygame.image.load("../human_benchmark/graphics/back_button_blue.png"),
        "menu_play_button": pygame.image.load("../human_benchmark/graphics/level_play_button.png"),

        # ------------------------ OPTIONS SCREEN ASSETS ------------------------
        "options_menu_screen": pygame.image.load("../human_benchmark/graphics/options_menu_screen.png"),
        "back_button": pygame.image.load("../human_benchmark/graphics/back_button.png"),
        "1440res":pygame.image.load("../human_benchmark/graphics/1440res.png"),
        "1224res":pygame.image.load("../human_benchmark/graphics/1224res.png"),
        "1024res":pygame.image.load("../human_benchmark/graphics/1024res.png"),
        "1440res_selected": pygame.image.load("../human_benchmark/graphics/1440res_selected.png"),
        "1224res_selected": pygame.image.load("../human_benchmark/graphics/1224res_selected.png"),
        "1024res_selected": pygame.image.load("../human_benchmark/graphics/1024res_selected.png"),
        
         # ------------------------ CIRCLE OPTION ASSETS ------------------------      
        "5_circles_unselected": pygame.image.load("../human_benchmark/graphics/5_circles_unselected.png"),
        "10_circles_unselected": pygame.image.load("../human_benchmark/graphics/10_circles_unselected.png"),
        "20_circles_unselected": pygame.image.load("../human_benchmark/graphics/20_circles_unselected.png"),
        "1x_size_unselected": pygame.image.load("../human_benchmark/graphics/1x_size_unselected.png"),
        "2x_size_unselected": pygame.image.load("../human_benchmark/graphics/2x_size_unselected.png"),
        "3x_size_unselected": pygame.image.load("../human_benchmark/graphics/3x_size_unselected.png"),
        "5_circles_selected": pygame.image.load("../human_benchmark/graphics/5_circles_selected.png"),
        "10_circles_selected": pygame.image.load("../human_benchmark/graphics/10_circles_selected.png"),
        "20_circles_selected": pygame.image.load("../human_benchmark/graphics/20_circles_selected.png"),
        "1x_size_selected": pygame.image.load("../human_benchmark/graphics/1x_size_selected.png"),
        "2x_size_selected": pygame.image.load("../human_benchmark/graphics/2x_size_selected.png"),
        "3x_size_selected": pygame.image.load("../human_benchmark/graphics/3x_size_selected.png"),
        "5s_limit_unselected": pygame.image.load("../human_benchmark/graphics/5s_limit_unselected.png"),   
        "10s_limit_unselected": pygame.image.load("../human_benchmark/graphics/10s_limit_unselected.png"),
        "20s_limit_unselected": pygame.image.load("../human_benchmark/graphics/20s_limit_unselected.png"),
        "5s_limit_selected": pygame.image.load("../human_benchmark/graphics/5s_limit_selected.png"),
        "10s_limit_selected": pygame.image.load("../human_benchmark/graphics/10s_limit_selected.png"),
        "20s_limit_selected": pygame.image.load("../human_benchmark/graphics/20s_limit_selected.png"),

        # ------------------------ LEVEL ASSETS ------------------------      
        "circle_1x": pygame.image.load("../human_benchmark/graphics/circle_1x.png"),
        "circle_2x": pygame.image.load("../human_benchmark/graphics/circle_2x.png"),
        "circle_3x": pygame.image.load("../human_benchmark/graphics/circle_3x.png"),
        "3": pygame.image.load("../human_benchmark/graphics/3.png"),
        "2": pygame.image.load("../human_benchmark/graphics/2.png"),
        "1": pygame.image.load("../human_benchmark/graphics/1.png"),
        "result_screen": pygame.image.load("../human_benchmark/graphics/result_screen.png"),
        "exit_button": pygame.image.load("../human_benchmark/graphics/exit-result-button.png"),
    }

def apply_scaling():
    global images, global_scaler

    images = {}
    for key, img in original_images.items():
        images[key] = pygame.transform.scale_by(img, global_scaler)

def set_global_scaler(value: float):
    global global_scaler
    global_scaler = value
    apply_scaling()

# ------------------------ FONTS ------------------------
def get_main_menu_font(size):
    return pygame.font.Font("../human_benchmark/fonts/Heavitas.ttf", size)

def result_screen_font(size):
    return pygame.font.Font("../human_benchmark/fonts/capitolcity.ttf", size)