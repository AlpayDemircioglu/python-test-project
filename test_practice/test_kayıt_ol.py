import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestKayitOl:
    def test_kayitol(self):
        # driver seç siteyi aç ve 2sn bekle
        driver = webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        time.sleep(2)

        # kayıt ol butonuna tıklama
        driver.find_element(By.CLASS_NAME,"ico-register").click()

        # kayıt olmak için boşlukları doldur
        driver.find_element(By.ID,"gender-male").click()
        driver.find_element(By.ID,"FirstName").send_keys("Alpay")
        driver.find_element(By.ID,"LastName").send_keys("Demircioğlu")
        driver.find_element(By.ID,"Email").send_keys("serseribella03@gmail.com")
        driver.find_element(By.ID,"Password").send_keys("123a123")
        driver.find_element(By.ID,"ConfirmPassword").send_keys("123a123")

        # kayıt ol butonuna tıkla
        driver.find_element(By.ID,"register-button").click()

        assert "Your registration completed" in driver.find_element(By.CLASS_NAME,"result").text

        driver.quit()

