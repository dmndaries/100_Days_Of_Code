def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Steps with a FOR Loop
# for step in range(6):
#     hurdle()

#Steps with a WHILE Loop

number_of_hurdles = 6
while number_of_hurdles > 0:
    hurdle()
    number_of_hurdles -= 1
    print(number_of_hurdles)

#Performing a WHILE Loop and you do not know the end:

while not at_goal(): 
    hurdle()