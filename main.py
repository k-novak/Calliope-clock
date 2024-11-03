def on_button_a():
    global hrs
    hrs += 1
    if hrs == 24:
        hrs = 0
    update()
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_ab():
    global b
    b += 1
    if b == 8:
        b = 0
    _4digit.set(b)
input.on_button_event(Button.AB, input.button_event_click(), on_button_ab)

def on_button_b():
    global sec, min2, hrs
    sec = 0
    min2 += 1
    if min2 == 60:
        min2 = 0
        hrs += 1
    update()
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def update():
    _4digit.bit(Math.idiv(hrs, 10), 0)
    _4digit.bit(hrs % 10, 1)
    _4digit.bit(Math.idiv(min2, 10), 2)
    _4digit.bit(min2 % 10, 3)
hrs = 0
min2 = 0
sec = 0
b = 0
_4digit: grove.TM1637 = None
_4digit = grove.create_display(DigitalPin.C16, DigitalPin.C17)
b = 7
_4digit.set(b)
sec = 0
min2 = 0
hrs = 0
basic.clear_screen()

def on_forever():
    global sec, min2, hrs
    basic.pause(1000)
    sec += 1
    if sec == 60:
        sec = 0
        min2 += 1
    if min2 == 60:
        min2 = 0
        hrs += 1
    if hrs == 24:
        hrs = 0
    update()
basic.forever(on_forever)
