# Steuert den rechten Motor des Roboters. Die Geschwindigkeit liegt zwischen -100 (rückwärts) und 100 (vorwärts). Bei der Geschwindigkeit 0 steht der Roboter.
def Motor_rechts(Geschwindigkeit: number):
    if Geschwindigkeit > 0:
        pins.analog_write_pin(AnalogPin.P12,
            Math.map(min(Geschwindigkeit, 100), 0, 100, 0, 1023))
        pins.analog_write_pin(AnalogPin.P13, 0)
    else:
        pins.analog_write_pin(AnalogPin.P12, 0)
        pins.analog_write_pin(AnalogPin.P13,
            Math.map(min(Geschwindigkeit * -1, 100), 0, 100, 0, 1023))
# Hier werden die Signale für das Steuern der Motorentreiber vorbereitet.
def motoren_vorbereiten():
    pins.analog_set_period(AnalogPin.P12, 256)
    pins.analog_set_period(AnalogPin.P13, 256)
    pins.analog_set_period(AnalogPin.P15, 256)
    pins.analog_set_period(AnalogPin.P16, 256)
    pins.analog_write_pin(AnalogPin.P12, 0)
    pins.analog_write_pin(AnalogPin.P13, 0)
    pins.analog_write_pin(AnalogPin.P15, 0)
    pins.analog_write_pin(AnalogPin.P16, 0)
# Steuert den linken Motor des Roboters. Die Geschwindigkeit liegt zwischen -100 (rückwärts) und 100 (vorwärts). Bei der Geschwindigkeit 0 steht der Roboter. 
def Motor_links(Geschwindigkeit2: number):
    if Geschwindigkeit2 > 0:
        pins.analog_write_pin(AnalogPin.P15,
            Math.map(min(Geschwindigkeit2, 100), 0, 100, 0, 1023))
        pins.analog_write_pin(AnalogPin.P16, 0)
    else:
        pins.analog_write_pin(AnalogPin.P15, 0)
        pins.analog_write_pin(AnalogPin.P16,
            Math.map(min(Geschwindigkeit2 * -1, 100), 0, 100, 0, 1023))
motoren_vorbereiten()

def on_forever():
    Motor_links(0)
    Motor_rechts(0)
    basic.pause(2000)
    Motor_links(70)
    Motor_rechts(-70)
    basic.pause(2000)
    Motor_links(0)
    Motor_rechts(0)
    basic.pause(2000)
    Motor_links(-70)
    Motor_rechts(70)
    basic.pause(2000)
basic.forever(on_forever)
