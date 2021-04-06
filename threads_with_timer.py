from threading import Thread
import time
SLEEP_TIME = 3  # sleep 3 seconds

def my_alarm(n):
    time.sleep(n)
    print("DING DING")

t_alarm = Thread(target=my_alarm, args=(SLEEP_TIME,))
t_alarm.start()
for i in range(100):
    if not t_alarm.is_alive():
        break
    print("doing something....")
    time.sleep(.2)
print("PROGRAM END")