import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestuyelikGiris:
    def test_uyeslik_giris(self):
        driver = webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()
        time.sleep(1)

        # giriş yap butonuna tıklama
        driver.find_element(By.CLASS_NAME,"ico-login").click()
        time.sleep(1)

        # kullanıcı bilgileri doldurma
        driver.find_element(By.ID,"Email").send_keys("serseribella02@gmail.com")
        driver.find_element(By.ID,"Password").send_keys("123a123")

        # kullanıcı bilgilerini girdikten sonra giriş yap butonuna tıklama
        driver.find_element(By.CLASS_NAME,"login-button").click()
        time.sleep(2)

        # assert ile kullanıcı girişi yapılmış mı kontrol et burada log out yani çıkış yap yazıyorsa olumlu bunu görüntülemek için .is_displayed() kullanırız
        assert driver.find_element(By.CLASS_NAME,"ico-logout").is_displayed() == True

