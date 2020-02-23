
import os
import pygame
from pathlib import Path
from snake_utils import Direction

BLOCK_SIZE  = (32,32)

path = Path(__file__).parent

IMG_SNAKE_WINNER     = pygame.image.load(str(path.joinpath("images/snake_winner.png")))
IMG_SNAKE_GAMEOVER   = pygame.image.load(str(path.joinpath("images/snake_gameover.png")))
IMG_SNAKE_BACKGROUND = pygame.image.load(str(path.joinpath("images/snake_bg.png")))

IMG_SNAKE_HEAD_UP    = pygame.image.load(str(path.joinpath("images/snake_head_up.png")))
IMG_SNAKE_HEAD_RIGHT = pygame.image.load(str(path.joinpath("images/snake_head_right.png")))
IMG_SNAKE_HEAD_DOWN  = pygame.image.load(str(path.joinpath("images/snake_head_down.png")))
IMG_SNAKE_HEAD_LEFT  = pygame.image.load(str(path.joinpath("images/snake_head_left.png")))
IMG_SNAKE_BODY_HORZ  = pygame.image.load(str(path.joinpath("images/snake_body_horizontal.png")))
IMG_SNAKE_BODY_VERT  = pygame.image.load(str(path.joinpath("images/snake_body_vertical.png")))
IMG_SNAKE_BODY_0     = pygame.image.load(str(path.joinpath("images/snake_body_turn_0.png")))
IMG_SNAKE_BODY_90    = pygame.image.load(str(path.joinpath("images/snake_body_turn_90.png")))
IMG_SNAKE_BODY_180   = pygame.image.load(str(path.joinpath("images/snake_body_turn_180.png")))
IMG_SNAKE_BODY_270   = pygame.image.load(str(path.joinpath("images/snake_body_turn_270.png")))
IMG_SNAKE_TAIL_UP    = pygame.image.load(str(path.joinpath("images/snake_tail_up.png")))
IMG_SNAKE_TAIL_RIGHT = pygame.image.load(str(path.joinpath("images/snake_tail_right.png")))
IMG_SNAKE_TAIL_DOWN  = pygame.image.load(str(path.joinpath("images/snake_tail_down.png")))
IMG_SNAKE_TAIL_LEFT  = pygame.image.load(str(path.joinpath("images/snake_tail_left.png")))

IMG_FOOD             = pygame.image.load(str(path.joinpath("images/red_square.png")))


class SnakeSprite():
    """
    """
    def __init__(self, snake):
        """
        """
        self.snake       = snake
        self.snake_image = []
        self.image_head = {}
        self.image_body = {}
        self.image_tail = {}

    def update(self):
        """
        Sets the snake sprite list to the current shape of the snake body
        """
        self.snake_image = self.renderSnakeImage(self.snake)

    def draw(self, board, surface):
        """
        Draws the snake body onto the window using the snake sprite list
        """
        rowLen = board.rowSize
        colLen = board.colSize



        for row in range(rowLen):
            for col in range(colLen):
                if (row,col) in self.snake.body:
                    index = self.snake.body.index((row,col))
                    surface.blit(self.snake_image[index], (BLOCK_SIZE[0]*row ,BLOCK_SIZE[1]*col))


    def renderSnakeImage(self, snake):
        """
        Returns a list of pygame images based on the shape of the snake body
        """
        renderedSnake=[]
        snakeSize = snake.size

        renderedSnake.append(self.getSnakeHeadImage(snake))

        if (snakeSize > 1):
            if (snakeSize >= 3):
                for index in range(1,snakeSize-1):
                    renderedSnake.append(self.getSnakeBodyImage(snake.body[index-1:index+2]))
            renderedSnake.append(self.getSnakeTailImage(snake.body[snake.size-2:]))

        return renderedSnake

    def getSnakeHeadImage(self, snake):
        """
        """
        if snake.direction == Direction.UP   : return IMG_SNAKE_HEAD_UP
        if snake.direction == Direction.RIGHT: return IMG_SNAKE_HEAD_RIGHT
        if snake.direction == Direction.DOWN : return IMG_SNAKE_HEAD_DOWN
        if snake.direction == Direction.LEFT : return IMG_SNAKE_HEAD_LEFT

    def getSnakeTailImage(self, list):
        """
        """
        b  = list[0] # body
        t  = list[1] # tail

        if (b[0] == t[0]) and (b[1] <  t[1]): return IMG_SNAKE_TAIL_UP
        if (b[0] >  t[0]) and (b[1] == t[1]): return IMG_SNAKE_TAIL_RIGHT
        if (b[0] == t[0]) and (b[1] >  t[1]): return IMG_SNAKE_TAIL_DOWN
        if (b[0] <  t[0]) and (b[1] == t[1]): return IMG_SNAKE_TAIL_LEFT

    def getSnakeBodyImage(self, list):
        """
        """
        h  = list[0] # Body Nearest head
        m  = list[1] #
        t  = list[2] # Body Nearest tail

        if (h[0] == m[0]) and (m[0] == t[0]): return IMG_SNAKE_BODY_VERT
        if (h[1] == m[1]) and (m[1] == t[1]): return IMG_SNAKE_BODY_HORZ

        # Clock Wise
        if (h[0] >  m[0]) and (h[1] == m[1]) and (m[0] == t[0]) and (m[1] >  t[1]): return IMG_SNAKE_BODY_0
        if (h[0] == m[0]) and (h[1] <  m[1]) and (m[0] >  t[0]) and (m[1] == t[1]): return IMG_SNAKE_BODY_90
        if (h[0] <  m[0]) and (h[1] == m[1]) and (m[0] == t[0]) and (m[1] <  t[1]): return IMG_SNAKE_BODY_180
        if (h[0] == m[0]) and (h[1] >  m[1]) and (m[0] <  t[0]) and (m[1] == t[1]): return IMG_SNAKE_BODY_270

        # Counter Clock Wise
        if (h[0] >  m[0]) and (h[1] == m[1]) and (m[0] == t[0]) and (m[1] <  t[1]): return IMG_SNAKE_BODY_270
        if (h[0] == m[0]) and (h[1] >  m[1]) and (m[0] >  t[0]) and (m[1] == t[1]): return IMG_SNAKE_BODY_180
        if (h[0] <  m[0]) and (h[1] == m[1]) and (m[0] == t[0]) and (m[1] >  t[1]): return IMG_SNAKE_BODY_90
        if (h[0] == m[0]) and (h[1] <  m[1]) and (m[0] <  t[0]) and (m[1] == t[1]): return IMG_SNAKE_BODY_0

        return IMG_FOOD

class FoodSprite():
    """
    """
    def __init__(self, food):
        self.food     = food
        self.position = food.position
        self.image    = IMG_FOOD

    def update(self):

        self.position = self.food.position


    def draw(self, board, surface):
        """
        """
        rowLen = board.rowSize
        colLen = board.colSize
        surface.blit(self.image, (BLOCK_SIZE[0]*self.position[0] ,BLOCK_SIZE[1]*self.position[1]))
