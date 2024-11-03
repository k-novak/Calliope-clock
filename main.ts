input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    hrs += 1
    if (hrs == 24) {
        hrs = 0
    }
    update()
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    b += 1
    if (b == 8) {
        b = 0
    }
    _4digit.set(b)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    sec = 0
    min += 1
    if (min == 60) {
        min = 0
        hrs += 1
    }
    update()
})
function update () {
    _4digit.bit(Math.idiv(hrs, 10), 0)
    _4digit.bit(hrs % 10, 1)
    _4digit.bit(Math.idiv(min, 10), 2)
    _4digit.bit(min % 10, 3)
}
let hrs = 0
let min = 0
let sec = 0
let b = 0
let _4digit: grove.TM1637 = null
_4digit = grove.createDisplay(DigitalPin.C16, DigitalPin.C17)
b = 7
_4digit.set(b)
sec = 0
min = 0
hrs = 0
basic.clearScreen()
basic.forever(function () {
    basic.pause(1000)
    sec += 1
    if (sec == 60) {
        sec = 0
        min += 1
    }
    if (min == 60) {
        min = 0
        hrs += 1
    }
    if (hrs == 24) {
        hrs = 0
    }
    update()
})
