# Untitled - By: pooya - Sat Jan 7 2023

import sensor, image, time, mjpeg, pyb
import micropython , json
import machine, os
from tb6612 import Stepper

sensor.reset()

#sensor setting
sensor.set_contrast(3)
sensor.set_gainceiling(16)

sensor.set_framesize(sensor.HQVGA)
sensor.set_pixformat(sensor.GRAYSCALE)


# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
cat_cascade = image.HaarCascade("haarcascade_frontalcatface", stages=25)
print(cat_cascade)

stepper = Stepper() # default rpm=2, power=50
stepper.set_speed(1) # rpm = 1
stepper.set_power(80) #set pwm

#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)
#sensor.skip_frames(time = 2000)

json_writ = {}
action_id = 0
rtc = machine.RTC()

clock = time.clock()

while(True):
    pyb.LED(RED_LED_PIN).on()
    print("About to start detecting faces...")
    sensor.skip_frames(time = 2000) # Give the user time to get ready.

    pyb.LED(RED_LED_PIN).off()
    sensor.snapshot().save("temp/bg.bmp")
    print("Now detecting faces!")
    pyb.LED(BLUE_LED_PIN).on()

    diff = 10 # We'll say we detected a face after 10 frames.
    while(diff):
        img = sensor.snapshot()
        img.difference("temp/bg.bmp")
        stats = img.statistics()
        #if (stats[5] > 20):
        #    diff -= 1
        # Threshold can be between 0.0 and 1.0. A higher threshold results in a
        # higher detection rate with more false positives. The scale value
        # controls the matching scale allowing you to detect smaller faces.
        faces = img.find_features(cat_cascade, threshold=0.5, scale_factor=1.5)

        if faces and (stats[5] > 20) :
            diff -= 1
            for r in faces:
                img.draw_rectangle(r)
            stepper.step(100) # motor rotates 1/2 circle
            time.sleep_ms(1000)
            timedate = rtc.now()
            print(timedate)
            json_writ['actionid'] = action_id + 1
            json_writ['Date'] = timedate[0]+timedate[1]+timedate[2]
            json_writ['timein'] = timedate[3]+timedate[4]+timedate[5]



    m = mjpeg.Mjpeg("example-%d.mjpeg" % pyb.rng())
    video_name = "example-%d.mjpeg" % pyb.rng()

    clock = time.clock() # Tracks FPS.
    print("You're on camera!")
    for i in range(200):
        clock.tick()
        m.add_frame(sensor.snapshot())
        print(clock.fps())

    m.close(clock.fps())
    pyb.LED(BLUE_LED_PIN).off()
    json_writ['picturpath'] = os.getcwd()+video_name
    json_writ['timeout'] = rtc.now()[3]+rtc.now()[4]+rtc.now()[5]

    json_string = json.dumps(json_writ)
    with open(os.getcwd()+"rcordit.json",'w') as f:
        f.write(json_string)
    print("Restarting...")
