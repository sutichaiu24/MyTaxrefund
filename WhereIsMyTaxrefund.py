
from selenium import webdriver
import  time
import  csv
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

for row in rowReader :
      TIN3.send_keys(row[0].split('-')[0])
      TIN2.send_keys(row[0].split('-')[1])
      TIN5.send_keys(row[0].split('-')[2])
      Single.click()
      Refund.send_keys(row[1])
      time.sleep(3)


Submit.click()

browser.close()


