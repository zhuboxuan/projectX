# -*- coding:utf-8 -*-
import requests
import re

import sys
reload(sys)
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from bs4 import BeautifulSoup
sys.setdefaultencoding('utf-8')

def main():
    session=requests.Session()
    headers = {
            'User-Agent': 'Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML,likeGecko) Chrome / 56.0.2924.87Safari / 537.36',
        }
    url ='http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t=TWTR&reportType=is&period=3&dataType=A&order=asc&columnYear=10&number=3'
    
    page = session.get(url,headers=headers).content.decode('utf-8')

    print page
    soup=BeautifulSoup(page,'html.parser')
    
    with open('/Users/apple/Downloads/dd/aa.csv', 'wb') as f:
        f.write(page)



if __name__ == '__main__':
    main()

