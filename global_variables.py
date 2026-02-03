import pygame
pygame.init()
pygame.mixer.init()

global_scaler = 1

original_images = {}

images = {}

def load_assets():
    global original_images

    if original_images:
        return
    
    original_images = {
        # ------------------------ MENU ASSETS ------------------------
        "main_menu_bg": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/main_bg.png"),
        "circle_numbers_timed_bg": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/circle_numbers_timed_bg.png"),
        "background_dimmer": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/background_dimmer.png"),
        "playing_area": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/playing_area.png"),
        "n_circles_timed": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/n_circles_timed.png"),
        "circle": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/circle.png"),
        "3": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/3.png"),
        "2": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/2.png"),
        "1": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/1.png"),
        "result_screen": pygame.image.load("/Users/evaldsberzins/pygame/human_benchmark/graphics/result_screen.png")
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