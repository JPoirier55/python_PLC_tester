import RPi.GPIO as GPIO
import time


def setup():
    """
    Sets up gpios, only happens at start up
    of django app once, or if called manually
    :return: None
    """
    GPIO.setmode(GPIO.BCM)

    gpio_input_pinlist = [4, 17, 18, 27, 22, 23, 24, 25]
    gpio_output_pinlist = [5, 6, 12, 13, 19, 16, 26, 20, 21]

    for pin in gpio_input_pinlist:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    for pin in gpio_output_pinlist:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


def read_input(pin_num):
    return GPIO.input(pin_num)


def send_output(pin_num, value):
    GPIO.output(pin_num, value)


if __name__ == '__main__':
    setup()
    print('setting up..')
    time.sleep(1)
    print('input 4 : ' + read_input(4))
    time.sleep(1)
    print('output 5 as 1')
    time.sleep(1)
    print('output 5 as 0')
    time.sleep(1)
    print('output 5 as 1')
