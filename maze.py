# Make sure you download pygame library and all qskit libraries in the file QRandom.py

import pygame
import QRandom

# set the size of screen and the size of the cell and the thickness
res= Width , Height = 1202,802
tile=5
cols,rows=Width//tile , Height//tile
thickness=1

pygame.init()
# sc=pygame.display.set_mode(res)
sc = pygame.display.set_mode(res)
clock=pygame.time.Clock()

# variables needed to make the player moves in tangible speed
move_delay = 90  # Delay in milliseconds between moves
last_move_time = pygame.time.get_ticks()  # Track the time of the last move

# variables needed to set the time when the target moves random
move_random_delay = 750 # Delay in milliseconds between random moves
last_random_move_time = pygame.time.get_ticks()  # Track the time of the last random move

# set the player size , speed (so that the players moves one cell in each press on keyboard)
player_radius = tile // 2 - thickness
player_x, player_y = tile // 2, tile // 2  # Start player at the top-left corner
player_speed = tile 

#variables needed to change the color randomly between two ranges in a smooth way
case=0
rangeI=60
rangeF=200
num = rangeI

PlayerCellX=0
PlayerCellY=0
mazefinished = False

# window when player cannot click on the button
def run_button_catch_game(sc):
    global num
    global case
    global rangeI 
    global rangeF
    rangeI = 180
    rangeF = 255

    # the number of choclates 
    choclates = QRandom.random_int(1,1000000)

    # fill the screen with random color
    sc.fill(pygame.Color((47, 79,  num)))

    # Screen size
    screen_width, screen_height = 1202, 802
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    # Text settings
    width_Text, height_Text = 1100, 50
    x_Text, y_Text = 15, 20
    rect_Text = pygame.Rect(x_Text, y_Text, width_Text, height_Text)

    # Text settings
    width_Text2, height_Text2 = 1100, 50
    x_Text2, y_Text2 = 15, 20 + height_Text
    rect_Text2 = pygame.Rect(x_Text2, y_Text2, width_Text2, height_Text2)

    # Button setting
    button_width, button_height = 100, 50
    button_x, button_y = (Width-button_width)//2 , screen_height//2
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Font settings
    font = pygame.font.Font(None, 36)
    button_Ok= font.render("Claim!", True, "black")
    text = font.render("You Have Won " + str(choclates) + " Chocolates !!" , True, "white")
    text2= font.render("Click Claim To Get Your Choclates :)", True, "white")


    # Main game loop for the button catch game
    running = True
    while running:
        #change the color of screen
        sc.fill((63, 64, 68))
        changeColor(50)

        # Event handling , not very useful in our code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the button is clicked
                if button_rect.collidepoint(event.pos):    #user cannot reach here
                    check_password(QRandom.random_password(10),choclates)  # Action when button is clicked
                    quit()

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check if mouse is over the button
        if button_rect.collidepoint(mouse_x, mouse_y):
            # Move the button to a new random location
            button_x = QRandom.random_int(0, screen_width - button_width - 1)
            button_y = QRandom.random_int(150, screen_height - button_height - 1)
            button_rect.topleft = (button_x, button_y)

        # Draw the button and the text on it
        # and draw the text at the top
        pygame.draw.rect(sc, (255,209,1), button_rect)
        sc.blit(button_Ok, (button_rect.x + (button_width - button_Ok.get_width()) // 2,
                            button_rect.y + (button_height - button_Ok.get_height()) // 2))
        sc.blit(text, (rect_Text.x + (width_Text - text.get_width()) // 2,
                       rect_Text.y + (height_Text - text.get_height()) // 2))
        sc.blit(text2, (rect_Text2.x + (width_Text2 - text2.get_width()) // 2,
                       rect_Text2.y + (height_Text2 - text2.get_height()) // 2))

        # Update the display
        pygame.display.flip()
        clock.tick(12)

    # Quit Pygame after the button game loop ends
    pygame.quit()


def check_password(correct_password,num_Of_chocolates, max_attempts=10):
    SCREEN_WIDTH, SCREEN_HEIGHT = 650, 350
    BG_COLOR = (63, 64, 68)
    TEXT_COLOR = (255, 209, 1)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    INPUT_BOX_COLOR = (255, 255, 255)
    CURSOR_COLOR = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Claim Your Reward")
    font = pygame.freetype.SysFont(None, 24)

    input_text = ""
    attempts = max_attempts
    message = "Write the password to claim your chocolates :)"
    message_color = TEXT_COLOR

    input_box_rect = pygame.Rect((SCREEN_WIDTH - 180) // 2, (SCREEN_HEIGHT - 30) // 2, 180, 30)
    cursor_visible = True
    cursor_timer = 0

    def draw_text(text, pos, color=(0,0,0)):
        font.render_to(screen, pos, text, color)

    final_message_shown = False
    while True:
        screen.fill(BG_COLOR)
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and not final_message_shown:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 10:
                        input_text += event.unicode

        # Automatically check password if 8 characters are entered
        if len(input_text) == 10 and not final_message_shown:
            if input_text == correct_password:
                message = f"Congratulations! You Won {num_Of_chocolates} Chocolates!"
                message_color = GREEN
                final_message_shown = True
            else:
                attempts -= QRandom.random_int(1,3)
                if attempts > 0:
                    message = f"Wrong Password, Please Try Again. {attempts} Attempts Left."
                    message_color = RED
                else:
                    message = "Sorry, You Cannot Get Your Chocolates :("
                    message_color = RED
                    final_message_shown = True
            input_text = ""  # Clear input text for the next attempt if needed

      # Calculate the y position of the input box and place the message 40 pixels above it
        input_box_y = (SCREEN_HEIGHT - 30) // 2
        text_rect = font.get_rect(message)
        text_x = (SCREEN_WIDTH - text_rect.width) // 2
        text_y = input_box_y - 60  # Position message 40 pixels above the input box
        draw_text(message, (text_x, text_y), message_color)
        draw_text("", (20, 200))

        pygame.draw.rect(screen, INPUT_BOX_COLOR, input_box_rect, border_radius=5)
        draw_text(input_text, (input_box_rect.x + 5, input_box_rect.y + 5))

        if not final_message_shown:
            if current_time - cursor_timer >= 0.5:
                cursor_visible = not cursor_visible
                cursor_timer = current_time

            if cursor_visible:
                cursor_x = input_box_rect.x + 5 + font.get_rect(input_text).width
                cursor_y = input_box_rect.y + 5
                pygame.draw.line(screen, CURSOR_COLOR, (cursor_x, cursor_y), (cursor_x, cursor_y + 20), 2)

        pygame.display.flip()

# function to change the color of the screen randomely in smooth way
def changeColor(slowlness):
    global num
    global case
    global rangeI
    global rangeF
    # as slowlness increases , the chance that luck = 1 or 2 decreases
    luck = QRandom.random_int(1, slowlness)
    if luck==1 or luck==2:
        if case==0:
            if num<rangeF:
                num=num+1
            else:
                num=num-1
                case=1
        else:
            if num>rangeI:
                num=num-1
            else:
                num=num+1
                case=0


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw(self):
        # Calculate pixel position
        x, y = self.x * tile, self.y * tile

        # Fill the cell if it is visited
        if self.visited:
            pygame.draw.rect(sc, pygame.Color((0,0,0)), (x, y, tile, tile))
            #black color

        # Draw walls
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y), (x + tile, y), thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + tile, y), (x + tile, y + tile), thickness)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x + tile, y + tile), (x, y + tile), thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'), (x, y + tile), (x, y), thickness)

    def drawCurrentCell(self):
        x,y=self.x*tile,self.y*tile
        pygame.draw.rect(sc, pygame.Color('green'), (x+2,y+2,tile-2,tile-2))

    # check if cell is valid to visit or not. It valid, returns the cell
    def checkCell(self,x,y):
        findIndex=lambda x,y: x+y*cols
        if x<0 or x>cols-1 or y<0 or y>rows-1:
            return False
        return grid_cells[findIndex(x,y)]

    # see which neighbor cell we can visit, and choose one of them randomly
    def checkNeighbor(self):
        neighbors=[]
        top=self.checkCell(self.x,self.y-1)
        right=self.checkCell(self.x+1,self.y)
        bottom=self.checkCell(self.x,self.y+1)
        left=self.checkCell(self.x-1,self.y)
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return QRandom.random_choice(neighbors) if neighbors else False

    # the target moves randomly after finishing the maze
    def moveRandomly(self):
        neighbors = []
        top = self.checkCell(self.x, self.y - 1)
        right = self.checkCell(self.x + 1, self.y)
        bottom = self.checkCell(self.x, self.y + 1)
        left = self.checkCell(self.x - 1, self.y)
        if top:
            neighbors.append(top)
        if right:
            neighbors.append(right)
        if bottom:
            neighbors.append(bottom)
        if left:
            neighbors.append(left)
        return QRandom.random_choice(neighbors) if neighbors else False
    
# remove the wall between the current cell and next cell
def removeWalls(current,next):
    dx=current.x-next.x
    dy=current.y-next.y
    if dx==1:
        current.walls['left']=False
        next.walls['right']=False
    elif dx==-1:
        current.walls['right']=False
        next.walls['left']=False
    if dy==1:
        current.walls['top']=False
        next.walls['bottom']=False
    elif dy==-1:
        current.walls['bottom']=False
        next.walls['top']=False


grid_cells= [Cell(col,row) for row in range(rows) for col in range(cols)]
currentCell=grid_cells[0]
stack=[]


while True:
    # set the color of the screen randomly and smoothly
    sc.fill(pygame.Color((47,79,num)))
    changeColor(10)

    current_time = pygame.time.get_ticks()  # Get current time
    keys = pygame.key.get_pressed() #take input from keyboard

    if current_time - last_move_time > move_delay:
        if keys[pygame.K_LEFT] and not grid_cells[PlayerCellY*cols+PlayerCellX].walls['left']:
            player_x -= player_speed
            PlayerCellX -= 1
        elif keys[pygame.K_RIGHT] and not grid_cells[PlayerCellY*cols+PlayerCellX].walls['right']:
            player_x += player_speed
            PlayerCellX += 1
        elif keys[pygame.K_UP] and not grid_cells[PlayerCellY*cols+PlayerCellX].walls['top']:
            player_y -= player_speed
            PlayerCellY -= 1
        elif keys[pygame.K_DOWN] and not grid_cells[PlayerCellY*cols+PlayerCellX].walls['bottom']:
            player_y += player_speed
            PlayerCellY += 1

        last_move_time = current_time
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    # draw each cell in the maze
    [cell.draw() for cell in grid_cells]
    currentCell.visited=True
    currentCell.drawCurrentCell()

    # take random next cell
    nextCell=currentCell.checkNeighbor()
    if nextCell:
        nextCell.visited=True
        stack.append(currentCell) # bfs traversing
        removeWalls(currentCell,nextCell)
        currentCell=nextCell
    else: # we have reached a closed loop
        if stack: # if there are still cells that must be traversed
            currentCell=stack.pop(0)
        elif current_time - last_random_move_time > move_random_delay: # we only reach here if we have finished the maze
            # change the position of the target randomly
            mazefinished = True
            nextCellMovingRandomily=currentCell.moveRandomly()
            currentCell=nextCellMovingRandomily
            last_random_move_time=pygame.time.get_ticks()


    # draw the player
    pygame.draw.circle(sc, pygame.Color((255,255,255)), (player_x, player_y), player_radius)

    # if the player reached the target , then make a new window where he user can take his/her prize
    if(currentCell.x==PlayerCellX and currentCell.y==PlayerCellY and mazefinished):
        run_button_catch_game(sc)
        exit()

    pygame.display.flip()
    clock.tick(60)