import pygame

def main():
    pygame.init()

    # Set up the screen
    screen_width, screen_height = 900, 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('2 Player Rectangle Game')

    # Define colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    # Player 1 (red rectangle) variables
    player1_x, player1_y = 100, 100
    player1_width, player1_height = 60, 60
    player1_speed = 5

    # Player 2 (blue rectangle) variables
    player2_x, player2_y = 700, 500
    player2_width, player2_height = 100, 100
    player2_speed = 10

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player 1 controls (arrow keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1_x -= player1_speed
        if keys[pygame.K_RIGHT]:
            player1_x += player1_speed
        if keys[pygame.K_UP]:
            player1_y -= player1_speed
        if keys[pygame.K_DOWN]:
            player1_y += player1_speed

        # Player 2 controls (WASD keys)
        if keys[pygame.K_a]:
            player2_x -= player2_speed
        if keys[pygame.K_d]:
            player2_x += player2_speed
        if keys[pygame.K_w]:
            player2_y -= player2_speed
        if keys[pygame.K_s]:
            player2_y += player2_speed

        # Prevent rectangles from leaving the screen
        player1_x = max(0, min(screen_width - player1_width, player1_x))
        player1_y = max(0, min(screen_height - player1_height, player1_y))
        player2_x = max(0, min(screen_width - player2_width, player2_x))
        player2_y = max(0, min(screen_height - player2_height, player2_y))

        # Draw everything
        screen.fill((0, 0, 0))  # Black background
        pygame.draw.rect(screen, red, (player1_x, player1_y, player1_width, player1_height))
        pygame.draw.rect(screen, blue, (player2_x, player2_y, player2_width, player2_height))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
