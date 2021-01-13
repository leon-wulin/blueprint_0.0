# -*- coding: UTF-8 -*-
import random
class data_class:
    def __init__(self):
        self.id=random.randint(0,9999999)
        self.subid=0
        self.type=0
        self.name='init event name'
        self.fm=''
        self.to=''
        self.remind=''
        self.motified=''

        self.every_day=0
        self.every_week_day=-1
        self.week_day='0'
        self.month_day=0
        return
