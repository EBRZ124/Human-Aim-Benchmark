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