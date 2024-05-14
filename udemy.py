import time


def count_down(seconds):
    while seconds >= 0:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        print(timer, end="\r") 
        time.sleep(1) 

        seconds -= 1

    print("Süre Bitti!")



hours = int(input("Saat: "))
minutes = int(input("Dakika: "))
seconds = int(input("Saniye: "))


total_seconds = (hours * 3600) + (minutes * 60) + seconds


count_down(total_seconds)
