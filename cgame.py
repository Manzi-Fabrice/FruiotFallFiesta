# Purpose: This class is responsible for moving the cart 
from cs1lib import *

W_H = 700
W_W = 500

# The size of the cart
WID = 150
HEI = 100

class Move:
    def __init__(self, image, x, y, vx):
        self.image = image  # Image to be drawn
        self.x = x
        self.y = y
        self.vx = vx  # Velocity in x-direction

    #Method for updating the position of the cart
    def update_box(self):

        # Ensuring that image stays within the screen
        if 0 <= self.x <= W_W - WID:
            self.x += self.vx
    #Method for drawing the cart
    def draw_image(self):
        draw_image(self.image, self.x, self.y - HEI)

