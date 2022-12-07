from machine import Pin,UART

uart = UART(0, 9600)
led_onboard = Pin(22, Pin.OUT)
led_onboard.value(1)

while True:
    # print('checking BT')
    if uart.any():
        command = uart.readline()
        print(command)
    
