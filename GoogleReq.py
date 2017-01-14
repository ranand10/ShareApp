import datetime
import re

import requests
from bs4 import BeautifulSoup

#from Prod import ReadShareStockConfig
import ReadShareStockConfig

def fileCreator(_exch_,_script_,seq):
    for i in range(1,2):
        textFilename= _script_+ '_' + str(seq)+'.txt'
        url = 'http://finance.google.com/finance/info?client=ig&q='+_exch_+':'+_script_
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,"html.parser")

        xys = soup.prettify()
        print(xys)
        for j in range(1,len(xys)):
            if xys[j] =='{' :
                firstCut= j+1
                j =len(xys)
                #print(i)
        for k in range(len(xys)-1,-1,-1):
            if xys[k]== '}':
                lastCut = k
                k=-1

        trimString = xys[firstCut:lastCut]

        for l in range(1,len(trimString)):
            if(trimString[l])==',':
                print(l)
                break

        finalString = list(filter(None,re.split(r'["]|[:]\s(1)?|[,]["](1)?|\n',trimString)))

        toFile =''
        for inCount in range(0,len(finalString)):
            if finalString[inCount] not in (" " ,":") :
                toFile = toFile + finalString[inCount]+'|'

        toFile = '|' + toFile + "time" + '|' + str(datetime.datetime.now())
        print(toFile)
        # file_write = open(fullPathName,"w",encoding='utf-8')
        file_write = open(ReadShareStockConfig.getRunningDataPath() + textFilename, "w", encoding='utf-8')
        file_write.write(toFile)
        # seq_file_write = open(seqFileFullPath,"a",encoding='utf-8')
        seq_file_write = open(ReadShareStockConfig.getSequenceFilePath() + ReadShareStockConfig.getSequenceFileName(), "a", encoding='utf-8')
        seq_file_write.writelines(_script_ + '_' + str(seq) + '\n')
        file_write.close()


