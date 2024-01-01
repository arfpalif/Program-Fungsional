import pygame
import time
import random
from functools import wraps

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SAYA SUKA SAYA SUKA")

BG = pygame.transform.scale(pygame.image.load("jeremy-perkins-uhjiu8FjnsQ-unsplash.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60  
PLAYER_VEL = 5
STAR_WIDTH = 20
STAR_HEIGHT = 30
STAR_VEL = 5
BULLET_WIDTH = 10
BULLET_HEIGHT = 10
BULLET_VEL = 10

FONT = pygame.font.SysFont("Poppins", 30)
BIG_FONT = pygame.font.SysFont("Poppins", 50)

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} executed in {elapsed_time} seconds")
        return result
    return wrapper

@timing_decorator
def draw_background():
    return BG

@timing_decorator
def draw_player(player_rect):
    pygame.draw.rect(WIN, (255, 0, 0), player_rect)

@timing_decorator
def draw_star(star):
    pygame.draw.rect(WIN, (0, 0, 255), star)

@timing_decorator
def draw_bullet(bullet):
    pygame.draw.rect(WIN, (255, 255, 0), bullet)

@timing_decorator
def draw_text(elapsed_time, score):
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (0, 0, 255))
    score_text = FONT.render(f"Score: {score}", 1, (0, 0, 255))
    WIN.blit(time_text, (10, 10))
    WIN.blit(score_text, (10, 40))

@timing_decorator
def draw_game(player, elapsed_time, stars, bullets, score):
    WIN.blit(draw_background(), (0, 0))
    draw_text(elapsed_time, score)
    list(map(draw_star, stars))
    list(map(draw_bullet, bullets))
    draw_player(player)
    pygame.display.update()

@timing_decorator
def draw_game_over_screen(score, elapsed_time):
    WIN.fill((0, 0, 0))
    game_over_text = BIG_FONT.render("Game Over", 1, (255, 0, 0))
    score_text = FONT.render(f"Score: {score}", 1, (255, 255, 255))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))

    WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    WIN.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 + 40))
    pygame.display.update()

@timing_decorator
def move_player(keys, player_rect):
    if keys[pygame.K_LEFT] and player_rect.x - PLAYER_VEL >= 0:
        player_rect.x -= PLAYER_VEL
    if keys[pygame.K_RIGHT] and player_rect.x + PLAYER_VEL <= WIDTH - PLAYER_WIDTH:
        player_rect.x += PLAYER_VEL

@timing_decorator
def move_bullets(bullets):
    list(map(lambda b: b.move_ip(0, -BULLET_VEL), bullets))

@timing_decorator
def is_collision(obj1, obj2):
    return obj1.colliderect(obj2)


def calculate_rating(score, elapsed_time):
    return max(0, score - elapsed_time // 2) if score < 30 or elapsed_time <= 20 else 10

@timing_decorator
def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    score = 0

    stars = []
    bullets = []

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            stars += [pygame.Rect(random.randint(0, WIDTH - STAR_WIDTH), -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT) for _ in range(3)]
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(
                        player.x + player.width // 2 - BULLET_WIDTH // 2,
                        player.y,
                        BULLET_WIDTH,
                        BULLET_HEIGHT
                    ))

        keys = pygame.key.get_pressed()
        move_player(keys, player)
        move_bullets(bullets)

        stars = [star for star in stars if star.y <= HEIGHT]
        bullets = [bullet for bullet in bullets if bullet.y > 0]

        for star in stars:
            star.y += STAR_VEL
            if is_collision(star, player):
                run = False
            elif star.y > player.y + player.height:
                score += 1

        bullets_to_remove = [bullet for bullet in bullets for star in stars if is_collision(bullet, star)]
        stars = [star for star in stars if not any(is_collision(bullet, star) for bullet in bullets_to_remove)]
        bullets = [bullet for bullet in bullets if bullet not in bullets_to_remove]

        draw_game(player, elapsed_time, stars, bullets, score)

        if not run:
            draw_game_over_screen(score, elapsed_time)
            pygame.time.delay(3000)

    rating = calculate_rating(score, elapsed_time)
    print(f"Rating: {rating}/10")

    pygame.quit()

if __name__ == "__main__":
    main()
