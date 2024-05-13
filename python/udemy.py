import time


def count_down(seconds):
    while seconds >= 0:
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        print(timer, end="\r")  # Aynı satırda süreyi güncelleyerek göstermek için 'end="\r"' kullanılır
        time.sleep(1)  # 1 saniye bekletme

        seconds -= 1

    print("Süre Bitti!")


# Kullanıcıdan süreyi alınır
hours = int(input("Saat: "))
minutes = int(input("Dakika: "))
seconds = int(input("Saniye: "))

# Süreyi saniyeye çevirilir
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# Sayma işlemi başlatılır
count_down(total_seconds)
