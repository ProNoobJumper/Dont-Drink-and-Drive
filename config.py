# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

# Player car settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 80
PLAYER_MAX_SPEED = 10

# Obstacle settings
OBSTACLE_SPEED = 5

# Score update interval (ms) - lower value updates score more frequently
SCORE_TICK_MS = 250

# Optional image paths for sprites. Set to None or a path string.
PLAYER_IMAGE = r"assets\player sprite.png"
CAR_IMAGE = r"assets\enemy_car sprite.png"
TRUCK_IMAGE = r"assets\truck_sprite.png"
BUS_IMAGE = r"assets\school_bus sprite.png"
ROAD_IMAGE = r"assets\road sprite.png"

# Ratio used to shrink collision rectangles for more forgiving hitboxes.
# 1.0 = full image rect, <1.0 = smaller hitbox. Adjust to taste.
HITBOX_RATIO = 0.65

# Road / lane configuration
# Number of lanes drawn on the road image (use an integer >= 1)
LANE_COUNT = 3
# Left and right margins (in pixels) where obstacles should not spawn —
# this should roughly match the non-road edges in your road sprite.
ROAD_LEFT_MARGIN = 100
ROAD_RIGHT_MARGIN = 100

# Spawn-safe percent: fraction of screen width at left and right which are
# NOT available for spawning obstacles (e.g., 0.2 means first 20% and last
# 20% are off-limits).
SPAWN_SAFE_PERCENT = 0.2

# Difficulty scaling
# Every DIFFICULTY_INTERVAL_MS milliseconds the game becomes harder
DIFFICULTY_INTERVAL_MS = 10000
# How much to increase obstacle/road speed each difficulty step
SPEED_INCREMENT = 1
# Score per passive tick and how it increases per difficulty step
SCORE_PER_TICK_BASE = 1
SCORE_PER_TICK_INCREMENT = 1
# Optionally reduce the score tick interval (multiply by this factor each step)
SCORE_TICK_DECREASE_FACTOR = 0.9
# Minimal allowed score tick interval in ms
SCORE_TICK_MIN_MS = 100

# Keep a copy of the initial obstacle speed so we can reset on restart
INITIAL_OBSTACLE_SPEED = OBSTACLE_SPEED

# Mutable current obstacle speed (updated by GameManager for difficulty scaling)
CURRENT_OBSTACLE_SPEED = INITIAL_OBSTACLE_SPEED

# Spawn count controls how many obstacles to spawn each obstacle event
INITIAL_SPAWN_COUNT = 1
# How much to increase the spawn count every difficulty step
SPAWN_COUNT_INCREMENT = 1

# Configurable sprite sizes (except road which is scaled to screen)
# Player size (can be tuned)
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 160

# Obstacle sizes (defaults similar to previous values but configurable)
CAR_WIDTH = 100
CAR_HEIGHT = 160
TRUCK_WIDTH = 120
TRUCK_HEIGHT = 240
BUS_WIDTH = 140
BUS_HEIGHT = 300