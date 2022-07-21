from controller import Robot
from controller import Keyboard
from controller import DistanceSensor


robot=Robot()
keyboard = Keyboard()
timestep=64

autoMode= False

wheel1_left=robot.getDevice("wheel1_left")
wheel1_left.setPosition(float('inf'))
wheel1_left.setVelocity(0.0)

wheel1_right=robot.getDevice("wheel1_right")
wheel1_right.setPosition(float('inf'))
wheel1_right.setVelocity(0.0)

wheel2_left=robot.getDevice("wheel2_left")
wheel2_left.setPosition(float('inf'))
wheel2_left.setVelocity(0.0)

wheel2_right=robot.getDevice("wheel2_right")
wheel2_right.setPosition(float('inf'))
wheel2_right.setVelocity(0.0)

ds1= robot.getDevice("ds1")
ds2= robot.getDevice("ds2")
ds1.enable(timestep)
ds2.enable(timestep)


keyboard.enable(timestep)

position=0

speed=4
number_of_turns=0


prev_key = 0
key_pressed = -1

while (robot.step(timestep) !=-1):
    
    prev_key=key_pressed
    key_pressed = keyboard.getKey()
 

    # 79 is "o" key
    if(prev_key == -1  and  key_pressed==79):
        autoMode= not autoMode
            
    if(autoMode):      
        ds1_value = ds1.getValue()
        ds2_value = ds2.getValue()
        
        # number_of_turns varible is set to 5 when any obstacle is detected
        if(ds1_value<1000 or ds2_value<1000):
            number_of_turns=5
        
        # the rover turns until number_of_turns variable is 0
        # this helps to make almost a 90 degree turn
        if(number_of_turns>0):
            number_of_turns = number_of_turns - 1
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(speed)
        else:
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(speed)
         
    
    if(not autoMode):
    
        # 65 is "a" key
        if(key_pressed== 65):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(speed)
            
        # 68 is "d" key    
        if(key_pressed== 68):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(-speed)
            
        # 87 is "w" key
        if(key_pressed== 87):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(speed)
            
        # 83 is "s" key    
        if(key_pressed== 83):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(-speed)
            
        # if nothing is pressed    
        if(key_pressed== -1):
            wheel1_left.setVelocity(0)
            wheel1_right.setVelocity(0)
            wheel2_left.setVelocity(0)
            wheel2_right.setVelocity(0)
        