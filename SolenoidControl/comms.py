from machine import Pin,UART

uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17), bits=8, parity=None, stop=1)
led_onboard = Pin(22, Pin.OUT)
led_onboard.value(1)
uart.write('abc')
while True:
    # print('checking BT')
    if uart.any():
        command = uart.readline()
        print(command)
    
