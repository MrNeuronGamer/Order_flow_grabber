import datetime
import os
import wget

Data = datetime.date.today()
days_back = 60
dir_path = os.getcwd()

Symbols = ['Si-3.20','RTS-3.20','SBRF-3.20']

for symbol in Symbols:
    if not os.path.isdir(os.sep.join([dir_path] + [symbol])):
        os.mkdir(os.sep.join([dir_path] + [symbol]))


web_base_path = 'ftp://ftp.zerich.com/pub/Terminals/QScalp/History/'

for symbol in Symbols:
    for i in range(days_back):
        target = web_base_path + str(Data - datetime.timedelta(days=i))+ '/' + symbol + '.' +  str(Data - datetime.timedelta(days=i)) + '.OrdLog.qsh'

        try:

            wget.download(target, os.sep.join([dir_path] +[symbol] + [ symbol + '.' +  str(Data - datetime.timedelta(days=i)) + '.OrdLog.qsh']) )
        except : pass


# ftp://ftp.zerich.com/pub/Terminals/QScalp/History/2019-12-11/Si-12.19.2019-12-11.OrdLog.qsh
