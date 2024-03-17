from datetime import datetime
from khayyam import JalaliDatetime


class Time:
    def time_now(self):
        now = datetime.now()
        # print(now)
        now_p = JalaliDatetime(now).strftime('%Y-%A-%d %H:%M')
        print(now_p)

