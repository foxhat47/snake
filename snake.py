from snake_utils import Direction


#---------------------------------------------------------------------------------------------------

class Board():
    """
    """
    def __init__(self, sizeRow, sizeCol):
        self.board = [[None for col in range(sizeCol)] for row in range(sizeRow)]

    @property
    def rowSize(self):
        return len(self.board)

    @property
    def colSize(self):
        return len(self.board[0])



#---------------------------------------------------------------------------------------------------

class Snake():
    """
    """
    MOVE = 0
    GROW = 1

    def __init__(self, direction, startPosX, startPosY):
        self.body = []
        self.body.append((startPosX, startPosY))
        self.direction = direction
        self.new_dir   = direction
        self.status    = self.MOVE

    @property
    def head(self):
        """
        tuple of board position (x,y)
        """
        return self.body[0]

    @property
    def size(self):
        return len(self.body)

    @property
    def tail(self):
        return self.body[1:]

    def move(self, direction):
        self.status  = self.MOVE
        self.new_dir = direction


    def grow(self, direction):
        self.status  = self.GROW
        self.new_dir = direction


    def display(self):
        """
        Console Debug print
        """
        msg=[]
        msg.append("Snake =")
        for bodyPart in self.body:
            msg.append((" " + str(bodyPart)))

        print(''.join(msg))

    def update(self):
        """
        """
        currPos = ()

        if not self.opositeDirecton(self.direction) == self.new_dir:
            self.direction = self.new_dir

        if self.status == self.GROW:
            self.body.insert(0, (self.head[0] + self.direction[0], self.head[1] + self.direction[1]))
        else:
            currPos = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])

            #for index, prevPos in enumerate(self.body):
            #    self.body[index] = currPos
            #    currPos          = prevPos
            
            # Didn't need to iterate entire list, just push new front position
            # and pop last, still dealing with list insertion of O(n)
            # Note: consider doublely linked list
            self.body.insert(0, currPos)
            self.body.pop()

    def opositeDirecton(self, direction):
        """
        """
        if (direction == Direction.UP   ): return Direction.DOWN
        if (direction == Direction.LEFT ): return Direction.RIGHT
        if (direction == Direction.RIGHT): return Direction.LEFT
        if (direction == Direction.DOWN ): return Direction.UP

class Food():
    def __init__(self, startPosX, startPosY):
        self.position = [startPosX, startPosY]
        self.eaten    = False
        
    def update(self):
        if (self.eaten):
            self.position = [10,10]
            self.eaten = False
            
        