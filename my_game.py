#Name: Manzi Fabrice Niyigaba
#Date: March 5th 2024
#Purpose: Creating fruit catch game(FruitFall Fiesta)

#Description:
# This code execute the fruit catch game where the fruit are being drawn randomly.
# The key to move the cart are "k" and "m"
# it also records the score if the fruit is caught and reduce the score if the fruit is missed
# when the score reaches a certain point the speed and the rate of falling of the fruit starts to gradually increase
# however, there is the limit for this increase to make the game possible to play


from cs1lib import *
from cgame import Move
from random import randint

#loading the images of the fruits
img1= load_image("avocado.png")
img2= load_image("pineapple.png")
img3= load_image("papaya.png")
img4= load_image("apple.png")
img5= load_image("jack.png")
img6= load_image("mango.png")
img7= load_image("grape.png")
img8= load_image("orange.png")

#load the image of the background
img9=load_image("background.jpg")

#loading the image of the cart
cart= load_image("cart.png")

# list of the dictionary from which we import randomly
fruits=[img4,img5,img8,img7,img6,img2,img3,img1]

fruit_size= 20

#setting the size of the window
W_H = 700
W_W = 500

WID = 150
HEI = 100
xbox = 0

#setting the movement of the cart as the key is pressed
CHANGE = 20

#setting the key determining the motion
MOVE_LEFT = 'm'
MOVE_RIGHT = 'k'

#setting the flags directing the key press
k_pressed = False
m_pressed = False

#setting the speed of the fruit
fruit_speed = 15  # Consider adjusting speed as the game progresses

myfruits = []  # List to hold the dictionary of the information of the fruit

# Timing for fruit generation
fruit_timer = 0
fruit_interval = 4  # control how long does it take to generate a fruit


score = 0  # Initialize score

#creating a move object "cart"
box = Move(cart,xbox, W_H - HEI, CHANGE)

# this function is responsible for randomly generating a fruit
def generate_fruit():

    x_position = randint(0, W_W-80)#x_range for generating the fruit

    fruit_image = fruits[randint(0, len(fruits) - 1)]  # Select a random fruit image

    #creating a dictionay containing the information of the fruit
    #I choose to use dictionary to reduce the number of the high number of operations that can arise from using lists
    myfruits.append({'image': fruit_image, 'x': x_position, 'y': -2, 'vy': fruit_speed})

# this function is responsible for drawing the fruit
def draw_fruits():
    for fruit in myfruits: # goes over every key in myfruits
        draw_image(fruit['image'], fruit['x'], fruit['y'])

# function responsible for checking collision with the cart
def check_collisions():
    global score
    for char in myfruits[:]:
        # I struggled with making the fruit disappear
        # I used this website to learn about shallow copy https://docs.python.org/3/library/copy.html
        # I learned that you can create a shallow copy of the list and remove items from it always
        # This help us to mimic the disappearing of the fruit without affection our overall list

        if char['y'] + fruit_size >= box.y and char['x'] >= box.x and char['x'] <= box.x + WID:
            score += 1
            myfruits.remove(char)
        elif char['y'] + fruit_size >= W_H:
            score -= 1
            myfruits.remove(char)

# This function is responsible to detect the key pressed
def key_pressed(key):
    global m_pressed, k_pressed
    if key == MOVE_RIGHT:
        m_pressed = True
    elif key == MOVE_LEFT:
        k_pressed = True

#This function is responsible for detecting the key release
def key_released(key):
    global m_pressed, k_pressed
    if key == MOVE_RIGHT:
        m_pressed = False
    elif key == MOVE_LEFT:
        k_pressed = False
# This function is responsible for clearing the screen


def move_fruit():
    for item in myfruits: # goes over every dictionary in myfruits list
        item['y'] += item['vy']
def main_draw():
    clear()
    global fruit_timer, score, fruit_speed,fruit_interval
    draw_image(img9,0,0)

    # Increment fruit timer and generate new fruit if the interval has passed
    fruit_timer += 1
    if fruit_timer >= fruit_interval:
        generate_fruit()
        fruit_timer = 0  # Reset timer

    move_fruit()
    draw_fruits()
    check_collisions()

    if m_pressed and box.x < W_W - WID:
        box.x += CHANGE
    if k_pressed and box.x > 0:
        box.x -= CHANGE

    box.draw_image()

    #Drawing the score on the cart
    set_stroke_color(1, 1, 1)
    set_font_size(15)  # Set font size
    draw_text(f"Score: {score}", box.x , box.y + HEI )

    #Increase the difficulty of the game
    if score>= 25:
        if fruit_interval>=5:
            fruit_interval -= 0.01
        if fruit_speed<= 30:
            fruit_speed += 0.01


    else:
        fruit_speed= 15
        fruit_interval=20



start_graphics(main_draw, width=W_W, height=W_H, key_press=key_pressed, key_release=key_released)
