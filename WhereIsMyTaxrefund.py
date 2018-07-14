
from selenium import webdriver
import  time
import  csv
import requests,json
import urllib.parse

from selenium.common.exceptions import NoSuchElementException

LINE_ACCESS_TOKEN="LQNe4sqZ5ouBgWjJpSOFO9FLpGxUB4WIvyTE0t0hAiR"
url = "https://notify-api.line.me/api/notify"

def linenotify (botmessage) :
      message ="botmessage  # ข้อความที่ต้องการส่ง
      msg = urllib.parse.urlencode({"message":message})
      LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
      session = requests.Session()
      a=session.post(url, headers=LINE_HEADERS, data=msg)
      print(a.text)

browser =  webdriver.Chrome()

browser.get('https://sa.www4.irs.gov/irfof/lang/en/irfofgetstatus.jsp')

browser.switch_to.alert.accept()

TIN3 = browser.find_element_by_id('TIN3')
TIN2 = browser.find_element_by_id('TIN2')
TIN5 = browser.find_element_by_id('TIN5')

Single = browser.find_element_by_id('filingStatus1')
Refund = browser.find_element_by_id('refundAmount')
Submit = browser.find_element_by_id('Submit2')

socialFile = open('social.csv')
rowReader = csv.reader(socialFile)

socialFile = open('social.csv')
rowReader = csv.reader(socialFile)

for row in rowReader :
      TIN3.send_keys(row[0].split('-')[0])
      TIN2.send_keys(row[0].split('-')[1])
      TIN5.send_keys(row[0].split('-')[2])
      Single.click()
      Refund.send_keys(row[1])
      time.sleep(2)
      # TIN3.clear()
      # TIN2.clear()
      # TIN5.clear()
      Submit.click()
      outputFile = open('report.csv', 'w')
      try :
            element = browser.find_element_by_id("contentpage_lesswhitespace")
      except NoSuchElementException :
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow([row[2] + ' have to wait'])

      if element.is_displayed():
            result = browser.find_element_by_id("contentpage_lesswhitespace").text
            outputWriter = csv.writer(outputFile)
            outputWriter.writerow([row[2]+' receive'+ result])


      browser.find_element_by_id('getrefundstatus1').click()

browser.close()









