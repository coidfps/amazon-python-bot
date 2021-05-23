from selenium import webdriver
from time import sleep

class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def checkAndBuyPS5(self):
        self.driver.get('https://www.amazon.com/gp/product/B08WM28PVH/ref=ox_sc_saved_title_1?smid=&psc=1')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            buyNow.click()
            sleep(2)
            buyNow2 = self.driver.find_element_by_xpath('//*[@id="hlb-ptc-btn"]')
            buyNow2.click()
            sleep(2)
            buyNow3 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input')  
            buyNow3.click()
            sleep(1)
            self.driver.close()
        except Exception as e:
            print(e)
            sleep(1.5)
            self.checkAndBuyPS5()

