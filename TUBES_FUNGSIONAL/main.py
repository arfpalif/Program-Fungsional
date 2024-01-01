import sys
import random
import pygame
from pygame.locals import *
import time

pygame.init()

player_ship = 'plyship.png'
enemy_ship = 'enemyship.png'
ufo_ship = 'ufo.png'
player_bullet = 'pbullet.png'
enemy_bullet = 'enemybullet.png'
ufo_bullet = 'enemybullet.png'

BULLET_VEL = 5  # You can adjust the value as needed
BULLET_WIDTH = 5  # You can adjust the value as needed
STAR_WIDTH = 20  # You can adjust the value as needed
STAR_HEIGHT = 20



screen = pygame.display.set_mode((0, 0), FULLSCREEN)
s_width, s_height = screen.get_size()

clock = pygame.time.Clock()
FPS = 60

background_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
ufo_group = pygame.sprite.Group()
playerbullet_group = pygame.sprite.Group()
enemybullet_group = pygame.sprite.Group()
ufobullet_group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()


def create_lives(lives):
    live_img = pygame.image.load(player_ship)
    live_img = pygame.transform.scale(live_img, (30, 30))
    n = 0
    for i in range(lives):
        screen.blit(live_img, (0 + n, s_height - 60))
        n += 80

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([x, y])
        self.image.fill('white')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1
        self.rect.x += 1
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(-400, s_width)


class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')

    def update(self):
        mouse = pygame.mouse.get_pos()
        self.rect.x = mouse[0]
        self.rect.y = mouse[1]

    def shoot(self):
        bullet = create_bullet(player_bullet, self.rect.x + self.rect.width // 2 - BULLET_WIDTH // 2, self.rect.y, BULLET_VEL)
        return bullet


class Enemy(Player):
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = random.randrange(0, s_width)
        self.rect.y = random.randrange(-500, 0)

    def update(self):
        self.rect.y += 1
        if self.rect.y > s_height:
            self.rect.x = random.randrange(0, s_width)
            self.rect.y = random.randrange(-2000, 0)
        self.shoot()

    def shoot(self):
        if self.rect.y in (0, 30, 50, 70, 300, 700):
            enemybullet = create_bullet(enemy_bullet, self.rect.x + 20, self.rect.y + 50, BULLET_VEL)
            sprite_group.add(enemybullet)
            enemybullet_group.add(enemybullet)


class Ufo(Enemy):
    def __init__(self, img):
        super().__init__(img)
        self.rect.x = -200
        self.rect.y = 200
        self.move = 1

    def update(self):
        self.rect.x += self.move
        if self.rect.x > s_width + 200:
            self.move *= -1
        elif self.rect.x < -200:
            self.move *= -1
        self.shoot()

    def shoot(self):
        if self.rect.x % 50 == 0:
            ufobullet = create_bullet(ufo_bullet, self.rect.x + 50, self.rect.y + 70, BULLET_VEL)
            sprite_group.add(ufobullet)
            ufobullet_group.add(ufobullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0 or self.rect.y > s_height:
            self.kill()


def create_bullet(img, x, y, speed=5):
    bullet = Bullet(img, x, y, speed)
    sprite_group.add(bullet)
    if "player" in img:
        playerbullet_group.add(bullet)
    elif "enemy" in img:
        enemybullet_group.add(bullet)
    elif "ufo" in img:
        ufobullet_group.add(bullet)
    return bullet


def create_background(x, y, size_x, size_y):
    return [Background(size_x, size_y) for _ in range(20)]


def create_player():
    return Player(player_ship)


def create_enemy():
    return [Enemy(enemy_ship) for _ in range(10)]


def create_ufo():
    return [Ufo(ufo_ship) for _ in range(2)]


def run_update():
    sprite_group.draw(screen)
    sprite_group.update()


def playerbullet_hits_enemy(playerbullets, enemies):
    hits = pygame.sprite.groupcollide(enemies, playerbullets, False, True)
    for i in hits:
        if "enemy" in i.image.get_at((0, 0)):
            i.rect.x = random.randrange(0, s_width)
            i.rect.y = random.randrange(-3000, -100)


def playerbullet_hits_ufo(playerbullets, ufos):
    hits = pygame.sprite.groupcollide(ufos, playerbullets, False, True)
    for i in hits:
        if "ufo" in i.image.get_at((0, 0)):
            i.rect.x = -199


def enemybullet_hits_player(player, enemybullets):
    hits = pygame.sprite.spritecollide(player, enemybullets, True)
    if hits:
        return True
    return False


def ufobullet_hits_player(player, ufobullets):
    hits = pygame.sprite.spritecollide(player, ufobullets, True)
    if hits:
        return True
    return False



def game_over(score, start_time, lives):
    screen.fill('black')
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, 'red')
    screen.blit(text, (s_width // 2 - 200, s_height // 2 - 100))

    font = pygame.font.Font(None, 40)
    score_text = font.render(f"Score: {score}", True, 'white')
    screen.blit(score_text, (s_width // 2 - 100, s_height // 2))

    elapsed_time = round(time.time() - start_time)
    time_text = font.render(f"Time: {elapsed_time}s", True, 'white')
    screen.blit(time_text, (s_width // 2 - 100, s_height // 2 + 50))

    pygame.display.flip()
    pygame.time.wait(3000)


def calculate_rating(score, elapsed_time):
    if score >= 30 and elapsed_time > 20:
        return 10
    else:
        return max(0, score - elapsed_time // 2)


def main():
    run = True
    start_time = time.time()
    elapsed_time = 0
    score = 0
    lives = 3

    backgrounds = create_background(40, 40, STAR_WIDTH, STAR_HEIGHT)
    player = create_player()
    enemies = create_enemy()
    ufos = create_ufo()

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                break
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                elif event.key == K_SPACE:
                    bullet = player.shoot()
                    if bullet:
                        sprite_group.add(bullet)

        keys = pygame.key.get_pressed()
        player.update()

        playerbullet_hits_enemy(playerbullet_group, enemy_group)
        playerbullet_hits_ufo(playerbullet_group, ufo_group)

        enemybullet_hits_player(player, enemybullet_group)
        ufobullet_hits_player(player, ufobullet_group)

        run_update()

        if enemybullet_hits_player(player, enemybullet_group) or ufobullet_hits_player(player, ufobullet_group):
            lives -= 1
            if lives < 0:
                run = False

        create_lives(lives)

        pygame.display.update()
        clock.tick(FPS)

    game_over(score, start_time, 3)

    rating = calculate_rating(score, elapsed_time)
    print(f"Rating: {rating}/10")

    pygame.quit()


if __name__ == "__main__":
    main()
