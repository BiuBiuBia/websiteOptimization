import datetime
import random
import numpy as np

class princeple:
    def rule(self):
        # 获取当前时间
        now = datetime.datetime.now()
        #0-星期一，1-星期二，以此类推
        weekday=now.weekday()
        hour=now.hour
        # randNumList表示不同星期日子下的不同时间段的返回值的范围
        #第一行表示星期一的，往后以此类推
        randNumList=[
            [[0,5],[10,20],[20,30],[10,20]],
            [[0, 5], [10, 20], [20, 30], [10, 20]],
            [[0, 5], [10, 20], [20, 30], [10, 20]],
            [[0, 5], [10, 20], [20, 30], [10, 20]],
            [[0, 5], [10, 20], [20, 30], [10, 20]],
            [[0, 5], [5,8], [20, 30], [10, 20]],
            [[0, 5], [10, 20], [20, 30], [10, 20]],
        ]
        shape=np.array(randNumList).shape
        # 根据当前星期日子weekday、时间段hour，获取对应的返回值
        for i in range(shape[0]):
            if weekday==i:
                if (hour >= 0 and hour < 8):
                    randNum = random.randint(randNumList[i][0][0], randNumList[i][0][1])
                elif hour >= 8 and hour < 13:
                    randNum = random.randint(randNumList[i][1][0], randNumList[i][1][1])
                elif hour >= 13 and hour < 19:
                    randNum = random.randint(randNumList[i][2][0], randNumList[i][2][1])
                else:
                    randNum = random.randint(randNumList[i][3][0], randNumList[i][3][1])
        return randNum//4+1,randNum//4+1,randNum//4-1,randNum//4-1

