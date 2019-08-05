import sys, pygame, random
pygame.init()
size = width, height = 200, 600
frame_size = width, height = 10, 30
block_size = 0, 0, 20, 20
screen = pygame.display.set_mode(size)

# STATE OBJECT OF GAME
state = { 
        'frame': [[0 for w in range(frame_size[0])] for h in range(frame_size[1])],
        'shapes': [
                [1, 3, 5, 7], # I
                [1, 2, 3, 4], # Z
                [0, 2, 3, 5], # Z'
                [1, 3, 2, 5], # T
                [1, 3, 4, 5], # L'
                [0, 2, 4, 5], # L
                [0, 1, 2, 3] # O
                ],
        'colors': {
                'black':  (0, 0, 0),
                'blue':   (0, 0, 255),
                'green':  (0, 255, 0),
                'yellow': (0, 255, 255),
                'red':    (255, 0, 0),
                'purple': (255, 0, 255),
                'orange': (255, 255, 0),
                'white':  (255, 255, 255)
            },
        'current_shape': None 
        }


randint = random.randint(1,6)
state['current_shape'] = randint

def add_shape():
    f = state['frame']
    shapes = state['shapes']
    s_index = state['current_shape']
    offset = 3; # to add the shape in center
    for cell in shapes[s_index]:
        height = cell // 2
        width  = offset + cell % 2
        f[height][width] = s_index # sign for block
    return f


def render(screen):
    f = state['frame']
    colors = state['colors']
    colors_key = list(state['colors'])
    # Render frame 
    for index_h, h in enumerate(f):
        for index_w, w in enumerate(h):
            rect = pygame.Rect(block_size)           # Create rect
            rect.move_ip(index_w * 20, index_h * 20) # Move to correct place
            col = colors[colors_key[w]]
            pygame.draw.rect(screen, col, rect)
            
# TODO
def move_shape(direction):
    f = state['frame']
    #if direction == "DOWN":
    #    f.insert(0, [0 for w in range(frame_size[0])])
    #    f = f[:-1]
    #if direction == "LEFT":
    for h in range(len(f)):
        for w in range(len(f[0])):
            if f[h][w] > 0:
                if direction is "LEFT" and w - 1 >= 0:
                    f[h][w], f[h][w - 1] = f[h][w - 1], f[h][w]
                if direction is "RIGHT" and w + 1 <= frame_size[0]:
                    f[h][w], f[h][w + 1] = f[h][w + 1], f[h][w]
                if direction is "DOWN" and h + 1 < frame_size[1]:
                    f[h][w], f[h+1][w] = f[h+1][w], f[h][w]
                    print(f[h][w], f[h+1][w])

    for row in f:
        print(row)
    return f

def new_and_cool_function():
    return "This is really important!"


def key_controller(key):
    f = state['frame']
    if key == pygame.K_DOWN:
        f = move_shape("DOWN")
    if key == pygame.K_LEFT:
        f = move_shape("LEFT")
    if key == pygame.K_RIGHT:
        f = move_shape("RIGHT")
    return f

state['frame'] = add_shape()
# Render Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: state['frame'] = key_controller(event.key)

    screen.fill(state['colors']['black']) 
    render(screen)
    pygame.display.flip()
