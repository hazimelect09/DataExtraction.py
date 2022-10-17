from TestingConnection import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
class framewk:
  def __init__(self,ChromePATH):
    s = setup(ChromePATH)
    self.driver = s.driver
  def getSocIns(self):
    WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.value")))
    SocialnumInsurance = self.driver.find_elements(By.CSS_SELECTOR,'span.value')[0].text
    return SocialnumInsurance
  def goto_Page(self, pagenum):
    #self.driver.find_element(By.ID, 'allContributor-link').click()
    #time.sleep(4)
    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@mask='0*']")))
    self.driver.find_elements(By.XPATH,"//input[@mask='0*']")[0].clear()
    self.driver.find_elements(By.XPATH,"//input[@mask='0*']")[0].send_keys(pagenum)
    element =self.driver.find_element(By.CLASS_NAME,"goto-page")
    self.driver.execute_script("arguments[0].click();", element)
    time.sleep(2)

  def getNationality(self):
    WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "nationality")))
    Nationality = self.driver.find_element(By.ID,'nationality').text
    return Nationality

  def getNationalID(self,nationality):
   if nationality == 'Saudi Arabia':
      WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.ID, "ninNumber")))
      NationalID=self.driver.find_element(By.ID,'ninNumber').text
      return NationalID
   else:
      WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.ID, "iqamaNumber")))
      NationalID = self.driver.find_element(By.ID, 'iqamaNumber').text
      return NationalID

  def getGender(self):
    Gender= self.driver.find_element(By.ID,'gender').text
    return Gender


  def getDob(self):
    DoB = self.driver.find_element(By.ID,'personDOB').text
    return DoB

  def getBordNum(self,nationality):
    if nationality != 'Saudi Arabia':
      BorderNumber=self.driver.find_element(By.ID, 'borderNumber').text
      return BorderNumber
    else:
      return " "

  def getPassNum(self, nationality):
    if nationality != 'Saudi Arabia':
      PassportNum = self.driver.find_element(By.ID, 'passportNumber').text
      return PassportNum
    else:
      return " "
  def open_request(self, number):
    WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "table")))
    element =self.driver.find_elements(By.TAG_NAME,'table')[0]
    WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "contributor-name")))
    print(len(element.find_elements(By.CLASS_NAME,'contributor-name')))
    elm=element.find_elements(By.CLASS_NAME,'contributor-name')[number].find_element(By.TAG_NAME,'a')

    elm.click()
    return  elm.text
  # raws.nth(number).click()

  def gettabledata(self):
    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    elements = self.driver.find_elements(By.CSS_SELECTOR, '.wage-table.table-responsive.gosi-scrollbar')[1].find_elements(By.TAG_NAME, 'td')
    TblOccupation = elements[0].text
    Tblbscwage = elements[1].text
    Tblhousing = elements[2].text
    Tblcommision = elements[3].text
    Tblotherallwnce = elements[4].text
    Tbltotalwage = elements[5].text
    return TblOccupation, Tblbscwage, Tblhousing, Tblcommision, Tblotherallwnce, Tbltotalwage

  def getEmpID(self):
    EmpId = self.driver.find_element(By.XPATH,'//div[@id="employeeId"]').text
    return EmpId


  def getContrStatus(self):
    if len(self.driver.find_elements(By.CSS_SELECTOR,'div#contractStatus')) > 0:
      Cntrctstatus = self.driver.find_element(By.CSS_SELECTOR,'div#contractStatus').text  # depends on the nationality
      return Cntrctstatus
    else:
      return " "
  def getEndreason(self,status):
    if status == 'Inactive':
      reason =self.driver.find_element(By.ID, 'leavingReason').text
      return reason
    else:
      return " "

  def getEngagementstatus(self):
    if len(self.driver.find_elements(By.CSS_SELECTOR,'div#engagementStatus div')) > 0:
      Engagementstatus = self.driver.find_element(By.CSS_SELECTOR,'div#engagementStatus div').text
      return Engagementstatus
    else:
      return " "

  def getStatus(self):
    Status = self.driver.find_element(By.ID,'status').text
    return Status
  def back(self):
    self.driver.back()