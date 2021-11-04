// Steuert den rechten Motor des Roboters. Die Geschwindigkeit liegt zwischen -100 (rückwärts) und 100 (vorwärts). Bei der Geschwindigkeit 0 steht der Roboter.
function Motor_rechts (Geschwindigkeit: number) {
    if (Geschwindigkeit > 0) {
        pins.analogWritePin(AnalogPin.P12, Math.map(Math.min(Geschwindigkeit, 100), 0, 100, 0, 1023))
        pins.analogWritePin(AnalogPin.P13, 0)
    } else {
        pins.analogWritePin(AnalogPin.P12, 0)
        pins.analogWritePin(AnalogPin.P13, Math.map(Math.min(Geschwindigkeit * -1, 100), 0, 100, 0, 1023))
    }
}
// Hier werden die Signale für das Steuern der Motorentreiber vorbereitet.
function motoren_vorbereiten () {
    pins.analogSetPeriod(AnalogPin.P12, 256)
    pins.analogSetPeriod(AnalogPin.P13, 256)
    pins.analogSetPeriod(AnalogPin.P15, 256)
    pins.analogSetPeriod(AnalogPin.P16, 256)
    pins.analogWritePin(AnalogPin.P12, 0)
    pins.analogWritePin(AnalogPin.P13, 0)
    pins.analogWritePin(AnalogPin.P15, 0)
    pins.analogWritePin(AnalogPin.P16, 0)
}
// Steuert den linken Motor des Roboters. Die Geschwindigkeit liegt zwischen -100 (rückwärts) und 100 (vorwärts). Bei der Geschwindigkeit 0 steht der Roboter. 
function Motor_links (Geschwindigkeit: number) {
    if (Geschwindigkeit > 0) {
        pins.analogWritePin(AnalogPin.P15, Math.map(Math.min(Geschwindigkeit, 100), 0, 100, 0, 1023))
        pins.analogWritePin(AnalogPin.P16, 0)
    } else {
        pins.analogWritePin(AnalogPin.P15, 0)
        pins.analogWritePin(AnalogPin.P16, Math.map(Math.min(Geschwindigkeit * -1, 100), 0, 100, 0, 1023))
    }
}
motoren_vorbereiten()
basic.forever(function () {
    Motor_links(0)
    Motor_rechts(0)
    basic.pause(2000)
    Motor_links(70)
    Motor_rechts(-70)
    basic.pause(2000)
})
