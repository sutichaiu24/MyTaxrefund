from selenium import webdriver
import time
import csv
import requests
import urllib.parse

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LINE_ACCESS_TOKEN="zX9fLdqjb8pGxiLxQ8hvB2Uc3JHvEAm7UkaXzIkf1DQ"
url = "https://notify-api.line.me/api/notify"
wait_message= 'tax refund has not come yet'
def linenotify (botmessage) :
      message = botmessage
      msg = urllib.parse.urlencode({"message":message})
      LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
      session = requests.Session()
      a=session.post(url, headers=LINE_HEADERS, data=msg)
      print(a.text)
browser =  webdriver.Chrome("/Users/sudhichaiungsuthornrungsi/Documents/Webdriver/chromedriver")
browser.get('https://sa.www4.irs.gov/irfof/lang/en/irfofgetstatus.jsp')
time.sleep(2)
browser.switch_to.alert.accept()

TIN3 = browser.find_element_by_id('TIN3')
TIN2 = browser.find_element_by_id('TIN2')
TIN5 = browser.find_element_by_id('TIN5')

Single = browser.find_element_by_id('filingStatus1')
Refund = browser.find_element_by_id('refundAmount')
Submit = browser.find_element_by_id('Submit2')

socialFile = open('social.csv')
rowReader = csv.reader(socialFile)
def autotax ():
      for row in rowReader :
            staleElement = True
            try:
                  WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                                  'Timed out waiting for PA creation ' +
                                                  'confirmation popup to appear.')

                  alert = browser.switch_to.alert
                  alert.accept()
                  print("alert accepted")
            except TimeoutException:
                  print("no alert")
            while (staleElement):
                  try:
                        TIN3 = browser.find_element_by_id('TIN3')
                        TIN2 = browser.find_element_by_id('TIN2')
                        TIN5 = browser.find_element_by_id('TIN5')
                        Single = browser.find_element_by_id('filingStatus1')
                        Refund = browser.find_element_by_id('refundAmount')
                        Submit = browser.find_element_by_id('Submit2')
                        staleElement = False
                  except StaleElementReferenceException:
                        staleElement = True
            print('คนที่'+ str(rowReader.line_num))
            TIN3.send_keys(row[0].split('-')[0])
            TIN2.send_keys(row[0].split('-')[1])
            TIN5.send_keys(row[0].split('-')[2])
            Single.click()
            Refund.send_keys(row[1])
            time.sleep(2)
            Submit.click()
            outputFile = open('report.csv', 'w')
            try :
                  element = browser.find_element_by_id("contentpage_lesswhitespace")
                  if element.is_displayed():
                        result = browser.find_element_by_id("contentpage_lesswhitespace").text
                        outputWriter = csv.writer(outputFile)
                        outputWriter.writerow([row[2] + ' receive' + result])
                        print(row[2]+'receive'+ result)
                        linenotify(row[2] + result)
            except NoSuchElementException :
                  outputWriter = csv.writer(outputFile)
                  outputWriter.writerow([row[2] + wait_message])
                  linenotify(row[2]+ wait_message )
                  print(row[2]+wait_message)
            browser.find_element_by_id('getrefundstatus1').click()

while (True):
      print ("HI I AM SOMSAK I AM HERE FOR HELP")
      command = input('<')
      if command == 'CHECK' :
            print ('SOMSAK is checking the tax')
            autotax()
            continue
      if command == 'DONE':
            print ('Thank you')
            browser.close()
            break











