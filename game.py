#!/usr/bin/python
"""
Python Snake Game
"""
import sys
import pygame

from snake import Snake, Food, Board
from snake_utils import Direction
from snake_sprites import SnakeSprite, FoodSprite
from snake_sprites import IMG_FOOD, IMG_SNAKE_BACKGROUND, IMG_SNAKE_GAMEOVER

WINDOW_SIZE = (640, 480)
BOARD_SIZE  = ((WINDOW_SIZE[0]//32), (WINDOW_SIZE[1]//32))

class SnakeGameState():
    """
    SnakeGameState
    """
    def __init__(self, row_size=10, col_size=10):
        self.gameBoard    = Board(row_size, col_size)
        self.player1      = Snake(Direction.LEFT, row_size//2, col_size//2)
        self.food         = Food(1, 1, self.gameBoard, self.player1)
        self.all_sprites  = [SnakeSprite(self.player1), FoodSprite(self.food)]
        self.frame_count  = 0
        self.player1Alive = True
        self.grow         = False
        self.move         = Direction.LEFT

    def update(self):
        """
        update
        """
        self.update_frame_count()

        # Update fame state if update frame count == 0 (i.e on frame_count rollover)
        if not self.frame_count:
            if (self.player1.head[0] == self.food.position[0] and
                self.player1.head[1] == self.food.position[1]):
                self.grow = True
                self.food.eaten = True

            if self.grow:
                self.grow = False
                self.player1.grow(self.move)
            else:
                self.player1.move(self.move)

            self.player1.update()
            self.food.update()

            for sprite in self.all_sprites:
                sprite.update()


    def validMove(self):
        if (self.player1.head in self.player1.tail or
                self.player1.head[0] == -1 or
                self.player1.head[1] == -1 or
                self.player1.head[0] == self.gameBoard.rowSize or
                self.player1.head[1] == self.gameBoard.colSize):
            self.player1Alive = False

    def update_frame_count(self):
        self.frame_count = (self.frame_count + 1) % 10


def main():
    """
    main
    """
    pygame.init()

    logo = IMG_FOOD

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    screen = pygame.display.set_mode(WINDOW_SIZE)

    gameState = SnakeGameState(BOARD_SIZE[0], BOARD_SIZE[1])
    for sprite in gameState.all_sprites:
        sprite.update()

    clock = pygame.time.Clock()

    # Testing out Point class
    #a = Point(0,1)
    #b = Point(1,2)
    #c = a + b
    #c = a - b


    while True:

        #clock.tick(60)
        clock.tick(60) # Testing

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    gameState.move = Direction.UP
                if event.key == pygame.K_DOWN:
                    gameState.move = Direction.DOWN
                if event.key == pygame.K_LEFT:
                    gameState.move = Direction.LEFT
                if event.key == pygame.K_RIGHT:
                    gameState.move = Direction.RIGHT
                if event.key == pygame.K_g:
                    gameState.grow = True
                if event.key == pygame.K_x:
                    sys.exit()
                if event.key == pygame.K_y:
                    gameState = SnakeGameState(BOARD_SIZE[0], BOARD_SIZE[1])
                    for sprite in gameState.all_sprites:
                        sprite.update()

        # Update game
        gameState.update()

        # Draw background
        if gameState.player1Alive:
            screen.blit(IMG_SNAKE_BACKGROUND, (0,0))



            # Draw Sprites
            for sprite in gameState.all_sprites:
                sprite.draw(gameState.gameBoard, screen)

            # Render frame
            gameState.validMove()
        else:
            screen.blit(IMG_SNAKE_GAMEOVER, (0,0))

        pygame.display.flip()


#---------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
