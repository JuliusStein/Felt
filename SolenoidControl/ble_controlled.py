from machine import Pin, Timer, UART
import time

led_onboard = Pin("LED", Pin.OUT)
led1 = Pin(9, Pin.OUT)
led2 = Pin(18, Pin.OUT)
led3 = Pin(11, Pin.OUT)
led4 = Pin(20, Pin.OUT)
led5 = Pin(14, Pin.OUT)
led6 = Pin(17, Pin.OUT)
led7 = Pin(6, Pin.OUT)
led8 = Pin(19, Pin.OUT)
heat_pad = Pin(21, Pin.OUT)

def reset():
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)
    led8.value(0)
    
def allBlink():
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)
    led8.value(0)
    time.sleep(1)
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    led5.value(1)
    led6.value(1)
    led7.value(1)
    led8.value(1)
    time.sleep(1)
    
def happy(delay):
    for i in range(2):
        led3.value(1)
        time.sleep(delay)
        led3.value(0)
        led4.value(1)
        time.sleep(delay)
        led4.value(0)
        
def sad(delay):
    for i in range(2):
        led1.value(1)
        led2.value(1)
        time.sleep(delay)
        led1.value(0)
        led2.value(0)
        led3.value(1)
        led4.value(1)
        time.sleep(delay)
        led3.value(0)
        led4.value(0)
        led5.value(1)
        led6.value(1)
        time.sleep(delay)
        led5.value(0)
        led6.value(0)
        led7.value(1)
        led8.value(1)
        time.sleep(delay)
        led7.value(0)
        led8.value(0)
        
def surprise(delay):
    for i in range(2):
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
        led5.value(1)
        led6.value(1)
        led7.value(1)
        led8.value(1)
        time.sleep(delay)
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led7.value(0)
        led8.value(0)
        time.sleep(delay)

def nervous(delay):
    for i in range(2):
        led1.value(1)
        led3.value(1)
        led5.value(1)
        led7.value(1)
        time.sleep(delay)
        led1.value(0)
        led3.value(0)
        led5.value(0)
        led7.value(0)
        time.sleep(delay)
        led2.value(1)
        led4.value(1)
        led6.value(1)
        led8.value(1)
        time.sleep(delay)
        led2.value(0)
        led4.value(0)
        led6.value(0)
        led8.value(0)
        time.sleep(delay)
        
def fear(delay):
    for i in range(2):
        led1.value(1)
        led2.value(1)
        time.sleep(delay)
        led1.value(0)
        led2.value(0)
        led3.value(1)
        led4.value(1)
        time.sleep(delay)
        led3.value(0)
        led4.value(0)
        led5.value(1)
        led6.value(1)
        time.sleep(delay)
        led5.value(0)
        led6.value(0)
        led7.value(1)
        led8.value(1)
        time.sleep(delay)
        led7.value(0)
        led8.value(0)
        
def anger(delay):
    for i in range(4):
        led3.value(1)
        led4.value(1)
        led5.value(1)
        led6.value(1)
        time.sleep(delay)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led1.value(1)
        led2.value(1)
        led7.value(1)
        led8.value(1)
        time.sleep(delay)
        led1.value(0)
        led2.value(0)
        led7.value(0)
        led8.value(0)
        
def excitement(delay):
    for i in range(2):
        led1.value(1)
        time.sleep(delay)
        led1.value(0)
        led8.value(1)
        time.sleep(delay)
        led8.value(0)
        led3.value(1)
        time.sleep(delay)
        led3.value(0)
        led6.value(1)
        time.sleep(delay)
        led6.value(0)
        
def disgust(delay):
    for i in range(2):
        led1.value(1)
        time.sleep(delay)
        led1.value(0)
        led3.value(1)
        time.sleep(delay)
        led3.value(0)
        led5.value(1)
        time.sleep(delay)
        led5.value(0)
        led7.value(1)
        time.sleep(delay)
        led7.value(0)
        led8.value(1)
        time.sleep(delay)
        led8.value(0)
        led6.value(1)
        time.sleep(delay)
        led6.value(0)
        led4.value(1)
        time.sleep(delay)
        led4.value(0)
        led2.value(1)
        time.sleep(delay)
        led2.value(0)
    
    
uart = UART(0, 9600)
led_onboard = Pin(22, Pin.OUT)
led_onboard.value(1)

command = b'x'
while True:
    # print('checking BT')  
    if uart.any():
        heat_pad.value(1)
        new_command = uart.readline()
        print(new_command)
        command = new_command
    else:
        #heat_pad.value(0)
        continue
        
    if command==b'0':
        happy(0.4)  
    elif command==b'1':
        sad(0.2)
    elif command==b'2':
        surprise(0.6)
    elif command==b'3':
        nervous(0.4)
    elif command==b'4':
        fear(0.3)
    elif command==b'5':
        excitement(0.8)
    elif command==b'6':
        anger(0.3)
    elif command==b'7':
        disgust(0.2)
    
    
        

