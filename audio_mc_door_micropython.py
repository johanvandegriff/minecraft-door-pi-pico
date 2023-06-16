from wavePlayer import wavePlayer
import machine

player = wavePlayer(leftPin=machine.Pin(0),rightPin=machine.Pin(1))
door_switch = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)

#repeat until Ctrl-C is pressed
try:
    while True:
        while door_switch.value() == 0: #wait until door is opened
            pass
        player.play('mc-door-open.wav')
        while door_switch.value() == 1: #wait until door is closed
            pass
        player.play('mc-door-close.wav')
except KeyboardInterrupt:
    player.stop()
    print("wave player terminated")

