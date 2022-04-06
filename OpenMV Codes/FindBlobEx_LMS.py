'''
LEGO EV3 with openMV, Find Ball Example
LPF2 class made by Tufts Center for Engineering Education and Outreach
Example made by OFDL Anthony Hsu (https://ofdl.tw)
Date: 2022/04/06, v1.0b, next version will optimize the LPF2 class performance
'''
import sensor, image, time
import gc,utime
import micropython
import LPF2
from machine import Pin
micropython.alloc_emergency_exception_buf(200)

##LUMP Define
modes = [
LPF2.mode('OpenMV-ALL',size = 8, type = LPF2.DATA16, format = '3.0'),
]

DataToSend = [0, 0, 0, 0, 0, 0, 0, 0] #X, Y, W, H, ID, state, 0, 0
max_idx = -1

lpf2 = LPF2.EV3_LPF2(3, 'P4', 'P5', modes, 85, timer = 4, freq = 5) #ID 85 to match our block
lpf2.initialize()

##Camera Define

ball_threshold   = (   80,   105,  -40,   10,   40,   80) # Middle L, A, B values.

sensor.reset()
sensor.set_pixformat(sensor.RGB565) # Format: RGB565.
sensor.set_framesize(sensor.QQVGA) # Size: QQVGA (120x160)
sensor.skip_frames(time = 2000) # Wait for settings take effect.
sensor.set_auto_gain(False) # Close auto gain (must be turned off for color tracking)
sensor.set_auto_whitebal(False) # Close white balance (must be turned off for color tracking)
clock = time.clock() # Create a clock object to track the FPS.

while(True):
    #If EV3 not connect
    if not lpf2.connected:
        lpf2.sendTimer.deinit()
        utime.sleep_ms(50)
        lpf2.initialize()
    else:
        clock.tick() # Track elapsed milliseconds between snapshots().
        img = sensor.snapshot() # Take a snapshot
        blobs = img.find_blobs([ball_threshold]) # Find Blobs

        #If blobs found
        if blobs:
            max_size=0
            i = 0
            for b in blobs:
                #Draw all blobs with ID
                img.draw_string(b.x()-6, b.y()+3, str(i)) # Draw ID
                img.draw_rectangle(b[0:4]) #Draw a rectangle
                #Find largest blob
                if b.area() > max_size:
                    max_blob = b
                    max_size = b.area()
                    max_idx = i
                i += 1
            DataToSend = [max_blob.cx(), max_blob.cy(), max_blob.w(), max_blob.h(), max_idx, 1, 0, 0]
        #If no blobs found
        else:
            max_idx = -1
            DataToSend = [0, 0, 0, 0, 0, 7, 0, 0]

        #Send Data to EV3
        mode=lpf2.current_mode
        if mode==0:
             lpf2.load_payload('Int16',DataToSend)

        #print(clock.fps())
        #print(DataToSend)
        #utime.sleep_ms(1)
