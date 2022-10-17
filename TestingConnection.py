from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
class setup:
 def __init__(self,chromepath):
  Opt= Options()
  PATH = chromepath
  Opt.add_experimental_option('debuggerAddress','localhost:8989')
  self.driver = webdriver.Chrome(executable_path=PATH,options=Opt)
  #self.driver = webdriver.Chrome(PATH,Opt)
  self.driver.implicitly_wait(4)
 def close(self):
  self.driver.quit()

