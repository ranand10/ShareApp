import datetime

#from Prod import ReadShareStockConfig

import ReadShareStockConfig

def getNowIndiaTimeFromSG():
    now_sing_time = datetime.datetime.now()
    india_time_now = now_sing_time - datetime.timedelta(seconds=ReadShareStockConfig.getTimeDiffSec())
    return india_time_now.time()


def getIndiaMarketStartTime():
    india_open_time=datetime.datetime.now().replace(hour=ReadShareStockConfig.getStartTimeHours(),
                                                    minute=ReadShareStockConfig.getStartTimeMin(),
                                                    second=ReadShareStockConfig.getStartTimeSec(),
                                                    microsecond=ReadShareStockConfig.getStartTimeMicSec())
    return india_open_time.time()

def getIndiaMarketEndTime():
    india_end_time=datetime.datetime.now().replace(hour=ReadShareStockConfig.getEndTimeHrs(),
                                                   minute=ReadShareStockConfig.getEndTimeMin(),
                                                   second=ReadShareStockConfig.getEndTimeSec(),
                                                   microsecond=ReadShareStockConfig.getEndTimeMicSec())
    return india_end_time.time()



