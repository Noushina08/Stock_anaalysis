import pandas as pd
from nsetools import Nse
from datetime import date
import common_fun
from common_fun import *


def get_histoy_Details():
    start_date=date(2022,1,1)
    end_date=date(2023,2,5)
    nse=Nse()
    symbols=list(nse.get_stock_codes().keys())[1:]
    print(symbols)
    for i in symbols:
        data=get_historycal_data(i,start_date,end_date)
        data.to_csv(i+".csv",)
        common_fun.upload_to_s3(i+'.csv','History/'+i+'.csv','tst-23')
        common_fun.remove_file(i+'.csv')


