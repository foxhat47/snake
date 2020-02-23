#---------------------------------------------------------------------------------------------------
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __add__(self, obj):
        return Point(self.x + obj.x, self.y + obj.y)
        
    def __sub__(self, obj):
        return Point(self.x - obj.x, self.y - obj.y)
        
    def toTuple(self):
        return (self.x, self.y)
        
    def toList(self):
        return [self.x, self.y]
        
class Direction():
    """
    """
    DOWN  = ( 0,  1)
    RIGHT = ( 1,  0)
    UP    = ( 0, -1)
    LEFT  = (-1,  0)
  