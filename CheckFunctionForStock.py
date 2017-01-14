import time

#from Prod import WorldTimesToSG, GoogleReq, ReadShareStockConfig

import WorldTimesToSG
import GoogleReq
import ReadShareStockConfig

def _scriptData_(_scriptName_, _minute_):
    GoogleReq.fileCreator("BOM", _scriptName_, _minute_)

#wholeShareList = allShareNames.wholeShareList()
#print(wholeShareList[0])

_ScriptFullList_=["INFY","HDFCBANK","MARUTI","SBI","ABB","TCS","RELCAPITAL","RELINFRA","RCOM","RPOWER","TATAPOWER","IDBI","KOTAKBANK","DENABANK","ICICIBANK","CORPBANK","INDUSINDBK","SYNDIBANK","PNB"]


while WorldTimesToSG.getNowIndiaTimeFromSG()< WorldTimesToSG.getIndiaMarketStartTime():
    print("i am waiting to start")
    time.sleep(20)

sequence_count = 0
while WorldTimesToSG.getNowIndiaTimeFromSG() < WorldTimesToSG.getIndiaMarketEndTime():
    sequence_count += 1
    for item_in_list in range(0,len(_ScriptFullList_)):
        _scriptData_(_ScriptFullList_[item_in_list],sequence_count)
    time.sleep(ReadShareStockConfig.getWaitBetweenCycle())

