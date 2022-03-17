class Rover(object):

    def __init__(self, start_x=0, start_y=0, orientation='N'):
        self.x, self.y = start_x, start_y
        self.orientation = orientation
        self.left_side = {'N': 'W', 'W':'S', 'S': 'E', 'E':'N'}
        self.right_side = {'N': 'E', 'E':'S', 'S': 'W', 'W':'N'}
        self.Plateau_WIDTH = 3
        self.Plateau_HEIGHT = 3
        self.obstacle_x, self.obstacle_y = 2,2 # We have 1 obstacle at (2,2) position
        
        
    def turn(self, side):
        if side == 'l':
            self.orientation = self.left_side[self.orientation]
        else:
            self.orientation = self.right_side[self.orientation]
            
    def going_forward(self):
        if self.orientation == "N":
            self.y =  (self.y + 1) % self.Plateau_HEIGHT
            
        elif self.orientation == "S":
            self.y = (self.y - 1) % self.Plateau_HEIGHT
                
        elif self.orientation == "E":
            self.x = (self.x + 1) % self.Plateau_WIDTH
                
        elif self.orientation == "W":
            self.x = (self.x - 1) % self.Plateau_WIDTH
    
            
    def going_backward(self):
        if self.orientation == "N":
            self.y = (self.y -1) % self.Plateau_HEIGHT

        elif self.orientation == "S":
            self.y = (self.y + 1) % self.Plateau_HEIGHT

        elif self.orientation == "E":
            self.x = (self.x - 1) % self.Plateau_WIDTH

        elif self.orientation == "W":
            self.x = (self.x + 1) % self.Plateau_WIDTH

            
    def apply_command(self, m):
        if m =='l' or m== 'r':
            self.turn(m)
        elif m == 'f':
            self.going_forward()
        elif m == 'b':
            self.going_backward()
        else:
            raise ValueError('Unrecognized command')
            
    def move(self, movs):
        for i in movs:
            prev_x, prev_y = self.x, self.y
            self.apply_command(i)
            if (self.x, self.y) == (self.obstacle_x, self.obstacle_y):
                self.x, self.y = prev_x, prev_y
                raise ValueError(f'Look out! There is an obstacle at {self.obstacle_x, self.obstacle_y}')
        return 'All commands executed successfully!'
