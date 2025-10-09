import pygame
import random
import sys
import config
from player import PlayerCar
from obstacles import Car, Truck, Bus


class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("2D Car Racing Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 55)
        self.is_running = True
        self.game_over = False

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()

        # Difficulty state
        self.current_obstacle_speed = config.INITIAL_OBSTACLE_SPEED
        self.current_score_tick_ms = config.SCORE_TICK_MS
        self.current_score_per_tick = config.SCORE_PER_TICK_BASE
        self.current_spawn_count = config.INITIAL_SPAWN_COUNT

        # Road background
        self.road_image = None
        if config.ROAD_IMAGE:
            try:
                loaded = pygame.image.load(config.ROAD_IMAGE)
                self.road_image = pygame.transform.scale(loaded, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)).convert()
                self.road_y1 = 0
                self.road_y2 = -config.SCREEN_HEIGHT
            except Exception:
                print(f"Warning: Failed to load road image from {config.ROAD_IMAGE}")

        self.reset()

    def reset(self):
        """Reset game objects and difficulty state."""
        self.all_sprites.empty()
        self.obstacles.empty()
        self.player = PlayerCar(config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT - 100)
        self.all_sprites.add(self.player)
        self.game_over = False

        # Reset difficulty
        self.current_obstacle_speed = config.INITIAL_OBSTACLE_SPEED
        self.current_score_tick_ms = config.SCORE_TICK_MS
        self.current_score_per_tick = config.SCORE_PER_TICK_BASE
        self.current_spawn_count = config.INITIAL_SPAWN_COUNT

        # Update shared config speed
        config.CURRENT_OBSTACLE_SPEED = config.INITIAL_OBSTACLE_SPEED

    def display_message(self, text, color=config.RED):
        message = self.font.render(text, True, color)
        rect = message.get_rect(center=(config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2))
        self.screen.blit(message, rect)
        pygame.display.flip()

    def spawn_obstacles(self, count):
        """Spawn up to `count` obstacles inside the safe center region without overlap.

        This function avoids the leftmost and rightmost SPAWN_SAFE_PERCENT of the
        screen and attempts multiple placements per obstacle to avoid overlap with
        existing on-screen obstacles and with other obstacles spawned in this call.
        """
        placed_rects = [obs.rect.copy() for obs in self.obstacles]

        safe_px = int(config.SPAWN_SAFE_PERCENT * config.SCREEN_WIDTH)
        left = safe_px
        right = config.SCREEN_WIDTH - safe_px

        attempts_per_spawn = 20
        spawned = 0

        for _ in range(count):
            obstacle_type = random.choice([Car, Truck, Bus])
            temp_ob = obstacle_type(0, -150)
            ob_w = temp_ob.rect.width
            ob_h = temp_ob.rect.height

            placed = False
            for attempt in range(attempts_per_spawn):
                if right - left <= ob_w:
                    x_pos = left
                else:
                    x_pos = random.randint(left, right - ob_w)

                candidate = pygame.Rect(x_pos, -150, ob_w, ob_h)
                if not any(candidate.colliderect(r) for r in placed_rects):
                    obstacle = obstacle_type(x_pos, -150)
                    self.obstacles.add(obstacle)
                    self.all_sprites.add(obstacle)
                    placed_rects.append(obstacle.rect.copy())
                    spawned += 1
                    placed = True
                    break

            # If not placed after attempts, skip to avoid overlap
        return spawned

    def run(self):
        obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(obstacle_timer, 1500)

        score_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(score_timer, int(self.current_score_tick_ms))

        difficulty_timer = pygame.USEREVENT + 3
        pygame.time.set_timer(difficulty_timer, config.DIFFICULTY_INTERVAL_MS)

        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type == obstacle_timer and not self.game_over:
                    # Spawn multiple obstacles per tick depending on current_spawn_count
                    self.spawn_obstacles(self.current_spawn_count)

                if event.type == score_timer and not self.game_over:
                    self.player.score += self.current_score_per_tick

                if event.type == difficulty_timer and not self.game_over:
                    # Increase difficulty
                    self.current_obstacle_speed += config.SPEED_INCREMENT
                    config.CURRENT_OBSTACLE_SPEED = self.current_obstacle_speed
                    self.current_spawn_count = min(self.current_spawn_count + config.SPAWN_COUNT_INCREMENT, config.SCREEN_WIDTH)
                    self.current_score_tick_ms = max(int(self.current_score_tick_ms * config.SCORE_TICK_DECREASE_FACTOR), config.SCORE_TICK_MIN_MS)
                    self.current_score_per_tick += config.SCORE_PER_TICK_INCREMENT
                    pygame.time.set_timer(score_timer, int(self.current_score_tick_ms))

                if event.type == pygame.KEYDOWN and self.game_over:
                    if event.key == pygame.K_r:
                        self.reset()
                    if event.key == pygame.K_q:
                        self.is_running = False

            if not self.game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.player.move_left()
                if keys[pygame.K_RIGHT]:
                    self.player.move_right()
                if keys[pygame.K_UP]:
                    self.player.accelerate()
                if keys[pygame.K_DOWN]:
                    self.player.decelerate()

                self.all_sprites.update()
                self.player.check_collision(self.obstacles)
                if not self.player.is_alive:
                    self.game_over = True

                for obstacle in list(self.obstacles):
                    if not obstacle.passed and self.player.rect.top < obstacle.rect.top:
                        self.player.score += 10
                        obstacle.passed = True

            # Draw road background if available, otherwise clear with BLACK
            if self.road_image:
                # Stop moving the road if the game is over
                dy = self.current_obstacle_speed if not self.game_over else 0
                self.road_y1 += dy
                self.road_y2 += dy

                if self.road_y1 >= config.SCREEN_HEIGHT:
                    self.road_y1 = self.road_y2 - config.SCREEN_HEIGHT
                if self.road_y2 >= config.SCREEN_HEIGHT:
                    self.road_y2 = self.road_y1 - config.SCREEN_HEIGHT

                self.screen.blit(self.road_image, (0, self.road_y1))
                self.screen.blit(self.road_image, (0, self.road_y2))
            else:
                self.screen.fill(config.BLACK)

            self.all_sprites.draw(self.screen)

            score_text = self.font.render(f"Score: {self.player.score}", True, config.WHITE)
            self.screen.blit(score_text, (10, 10))

            if self.game_over:
                self.display_message("Game Over! Press R to restart or Q to quit.")

            pygame.display.flip()
            self.clock.tick(config.FPS)

        pygame.quit()
        sys.exit()