import RPi.GPIO as GPIO
import time
from time import localtime, strftime

# Variable fuer Counter definieren
wcount_1 = 0
wcount_2 = 0
wcount_3 = 0
wcountbck_1 = 0
wcountbck_2 = 0
wcountbck_3 = 0

# Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO initialisieren
GPIO.setup(26, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup( 4, GPIO.IN)

# Pins als Input deklarieren und Pull-Up Widerstand aktivieren
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup( 4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Interrupt WCount_1 ADD +1 to counter
def interrupt_1(channel):
        global wcount_1
        wcount_1 +=1

# Interrupt WCount_2 ADD +1 to counter
def interrupt_2(channel):
        global wcount_2
        wcount_2 +=1

# Interrupt WCount_3 ADD +1 to counter
def interrupt_3(channel):
        global wcount_3
        wcount_3 +=1

# Interrupt Event hinzufuegen. Pin auf fallende Flanke reagieren
GPIO.add_event_detect(26, GPIO.FALLING, callback = interrupt_1)
GPIO.add_event_detect(12, GPIO.FALLING, callback = interrupt_2)
GPIO.add_event_detect( 4, GPIO.FALLING, callback = interrupt_3)

# Endlosschleife
while True:

        time.sleep(5)

        if wcount_1 > 0:
                wcountbck_1 = wcount_1
                wcount_1 = 0

        if wcount_2 > 0:
                wcountbck_2 = wcount_2
                wcount_2 = 0

        if wcount_3 > 0:
                wcountbck_3 = wcount_3
                wcount_3 = 0

        if wcountbck_1 > 0:
                csvfile = open("wcount1.csv","a")
                csvfile.write(time.strftime("%Y-%m-%d %H:%M:%S", localtime())+","+str(wcountbck_1 * 10)+"\n")
                csvfile.close()
                wcountbck_1 = 0

        if wcountbck_2 > 0:
                csvfile = open("wcount2.csv","a")
                csvfile.write(time.strftime("%Y-%m-%d %H:%M:%S", localtime())+","+str(wcountbck_2 * 10)+"\n")
                csvfile.close()
                wcountbck_2 = 0

        if wcountbck_3 > 0:
                csvfile = open("wcount3.csv","a")
                csvfile.write(time.strftime("%Y-%m-%d %H:%M:%S", localtime())+","+str(wcountbck_3 * 10)+"\n")
                csvfile.close()
                wcountbck_3 = 0
