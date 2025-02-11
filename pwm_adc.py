from machine import Pin, ADC, PWM
from utime import sleep

pot = ADC(26)
led = Pin(15, Pin.IN, Pin.PULL_UP)
led_pwm = PWM(led)
led_pwm.freq(1000)

while True:
  pot_val = pot.read_u16()
  led_pwm.duty_16(pot_val)
  sleep(0.1)
