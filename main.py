import time
import pyautogui
from PIL import ImageGrab
from PIL import ImageFilter
import keyboard


def modul(numar):
    if numar < 0:
        return -numar
    else:
        return numar


def current_milli_time():
    return round(time.time() * 1000)


# left arrow - x:578 y:760
# right arrow - x:778 y:760

time.sleep(6)

while True:
    # screenFrame = ImageGrab.grab((492, 175, 872, 825))
    sliver = ImageGrab.grab((492, 175, 502, 825))

    sliver = sliver.convert('L')

    sliver = sliver.filter(ImageFilter.BLUR)
    sliver = sliver.filter(ImageFilter.MinFilter(9))

    # sliver.show()

    tempBool = False
    tempPos = 0
    barPositions = [0, 0]
    index = 0
    for i in range(1, 400):
        pixel = int(sliver.getpixel((5, i)))

        if pixel >= 100:
            if not tempBool:
                tempBool = True
                tempPos = i

        else:
            if tempBool:
                tempBool = False
                barPositions[index] = int(round((i - tempPos) / 2) + tempPos)
                index = index + 1
    index = 0

    cut = []
    slotPositions = [0, 0]
    index = 0
    for i in barPositions:
        if i != 0:
            pos = i + 173
            imagine = ImageGrab.grab((492, pos, 872, pos + 20))

            imagine = imagine.convert('L')

            imagine = imagine.filter(ImageFilter.BLUR)

            tempBool = False
            tempPos = 0
            for j in range(5, 370):
                pixel = int(imagine.getpixel((j, 10)))
                if pixel < 90:
                    if not tempBool:
                        tempBool = True
                        tempPos = j
                else:
                    if tempBool:
                        tempBool = False
                        slotPositions[index] = int(round((j - tempPos) / 2) + tempPos)
        index = index + 1

    print(slotPositions[1])

    # Todo: Track player position and PID control

    if keyboard.is_pressed('esc'):
        break
