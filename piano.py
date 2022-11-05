import machine
import time

#cancion de prueba:

# note_freq = {
#   "A4": 440,
#   "C5": 523,
#   "D5": 587,
#   "E5": 659,
#   "R": 100
# }
# tune = [["D5", 0.5], ["C5", 0.5], ["D5", 0.5], ["R", 0.5], ["D5", 0.5], ["C5", 0.5], ["D5", 0.5],
#          ["R", 0.5], ["D5", 0.5], ["C5", 0.5], ["A4", 0.5], ["C5", 0.5], ["E5", 0.5], ["C5", 0.5], ["D5", 2]]
# def play_note(note_name, duration):
#     frequancy = note_freq[note_name]
#     if note_name == "R":
#         speaker.duty_u16(0)
#     else:
#         speaker.duty_u16(int(65535/2))
#     
#     speaker.freq(frequancy)
#     time.sleep(duration)


#variables:

speaker = machine.PWM(machine.Pin(0))

#example = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)

do_tres = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
do_tres_sostenido = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)

re_tres = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)
re_tres_sostenido = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)

mi_tres = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_DOWN)

fa_tres = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
fa_tres_sostenido = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)

sol_tres = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
sol_tres_sostenido = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)

la_tres = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
la_tres_sostenido = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

si_tres = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

do_cuatro = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
do_cuatro_sostenido = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

re_cuatro = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
re_cuatro_sostenido = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

mi_cuatro = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)

fa_cuatro = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
fa_cuatro_sostenido = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)

sol_cuatro = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
sol_cuatro_sostenido = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)

la_cuatro = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)
la_cuatro_sostenido = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_DOWN)

si_cuatro = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:

#     if example.value():
#         for note in tune:
#             play_note(note[0], note[1])
#         speaker.duty_u16(0)
    
    if do_tres.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(131)
        
    elif do_tres_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(139)
        
    elif re_tres.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(147)
        
    elif re_tres_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(156)
        
    elif mi_tres.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(165)
        
    elif fa_tres.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(175)
        
    elif fa_tres_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(185)
        
    elif sol_tres.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(196)
        
    elif sol_tres_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(208)
        
    elif la_tres.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(220)
        
    elif la_tres_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(233)
        
    elif si_tres.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(247)
        
    elif do_cuatro.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(262)
        
    elif do_cuatro_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(277)
    
    elif re_cuatro.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(294)
    
    elif re_cuatro_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(311)
        
    elif mi_cuatro.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(330)
        
    elif fa_cuatro.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(349)
        
    elif fa_cuatro_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(370)
        
    elif sol_cuatro.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(392)
    
    elif sol_cuatro_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(415)
        
    elif la_cuatro.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(440)
        
    elif la_cuatro_sostenido.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(466)

    elif si_cuatro.value():
        time.sleep(0.1)
        speaker.duty_u16(int(65535/2))
        speaker.freq(494)

    else:
        speaker.duty_u16(0)