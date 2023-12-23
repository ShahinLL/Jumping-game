import pygame
import sys
import pdb

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame")

image_path = "background.png"
image = pygame.image.load(image_path)
print("Loaded Image")

image_x, image_y = 0, 0

player_path = "player.png"
player_image = pygame.image.load(player_path)
print("Loaded Player")

item_path = "ball.png"
item_image = pygame.image.load(item_path)
print("Item Loaded")

start_image_path = "start.png"
start_image = pygame.image.load(start_image_path)
print("Start Display Loaded")

start_image_x, start_image_y = 0, 0

white = (255,255,255)
black = (0,0,0)

pygame.mouse.set_visible(False)

font = pygame.font.Font(None,36)

player_width = 40
player_height = 40
player_x = 0
player_y = 130
player_speed = 5
jump_height = 5
is_jumping = False
jump_count = 10
is_all_moving = True
item_speed = 10
item_x = 400
item_y = 175
item_width = 40 
item_height = 40

start_time = pygame.time.get_ticks()

hit = False

def start_menu():
    while True:
        screen.blit(start_image, (start_image_x, start_image_y))
        text = font.render("Press space to start", True, white)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

def display_time(text, x, y):
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)          

def run():

    global player_x, player_y, is_jumping, jump_count, item_x, item_y, hit

    running = True
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if not is_jumping:
            if keys[pygame.K_UP]:
                print("Player Jumps")
                is_jumping = True

        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg -= 1
                player_y -= (jump_count ** 2) * 0.3 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10
                player_y = 130

        if player_y < 130:
            player_y += 1

        item_x += item_speed
        if item_x > WIDTH:
            item_x = -400
        
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

        if not is_jumping and item_y + item_height >= player_y and player_x <= item_x <= player_x + player_width:
            hit = True

        elapsed_time = (pygame.time.get_ticks() - start_time) // 2000

        screen.blit(image, (image_x, image_y))

        screen.blit(player_image, (player_x, player_y))

        screen.blit(item_image, (item_x, item_y))

        display_time(f"Time: {elapsed_time}", WIDTH // 2, 20)

        pygame.display.flip()

        if hit:
            lost_text = font.render("You lost!", True, "black")
            lost_text_rect = lost_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(lost_text, lost_text_rect)
            pygame.display.flip()
            pygame.time.delay(5000)
            break

    pygame.quit()
    sys.exit()

if __name__=="__main__":
    start_menu()
    run()
