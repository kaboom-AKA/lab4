import time
from time import sleep
from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led():
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(1)

    led.set_output(0, 0)
    time.sleep(1)

    led.set_output(0, 1)
    time.sleep(1)

    led.set_output(0, 0)
    time.sleep(1)
    
    led.set_output(0, 1)
    time.sleep(1)

    led.set_output(0, 0)
    time.sleep(1)

    led.set_output(0, 1)
    time.sleep(1)

    led.set_output(0, 0)
    time.sleep(1)
    
    led.set_output(0, 1)
    time.sleep(1)

    led.set_output(0, 0)
    time.sleep(1)

def main():
    switch.init()
    while(True) :
        if switch.read_slide_switch() == 0:
            blink_led()

# Main entry point
if __name__ == "__main__":
    main()

