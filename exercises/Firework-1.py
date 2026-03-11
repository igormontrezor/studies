import datetime
import time
import emoji


timex = int(input('What the time: '))
for t in range(timex,0,-1):
    print(datetime.time(second=t))
    time.sleep(1.0)
print(f'Fireworks!!!{emoji.emojize(':fireworks:')}')