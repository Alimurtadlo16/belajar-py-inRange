import pygame
import time
import random

# Inisialisasi pygame
pygame.init()

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Ukuran layar
display_width = 500
display_height = 250

# Membuat layar
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game Ular Sederhana')

clock = pygame.time.Clock()

# Ukuran ular dan kecepatan
snake_block = 10
snake_speed = 15

# Font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Fungsi untuk menampilkan skor
def your_score(score):
    value = score_font.render("Skor Anda: " + str(score), True, black)
    dis.blit(value, [0, 0])

# Fungsi untuk menggambar ular
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Fungsi untuk menampilkan pesan
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

# Fungsi utama game
def gameLoop():
    game_over = False
    game_close = False

    # Posisi awal ular
    x1 = display_width / 2
    y1 = display_height / 2

    # Perubahan posisi
    x1_change = 0
    y1_change = 0

    # Inisialisasi ular
    snake_List = []
    Length_of_snake = 1

    # Posisi makanan
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("Anda Kalah! Tekan Q-Quit atau C-Play Again", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Jika menabrak batas layar
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update posisi ular
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        
        # Gambar makanan
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        # Update tubuh ular
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Cek apakah ular menabrak diri sendiri
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        # Jika ular makan makanan
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Jalankan game
gameLoop()
