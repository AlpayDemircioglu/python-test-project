from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUrunSecmeiki:
    def test_secim(self):
        # driver başlatma
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")

        # computers seçeneğine tıkla 2sn bekle
        driver.find_element(By.LINK_TEXT, "Computers").click()
        time.sleep(2)

        # assert ile doğru mu diye kontrol yap
        assert "Computers" in driver.title

        # desktops seçeneğine tıkla 2sn bekle
        driver.find_element(By.LINK_TEXT, "Desktops").click()
        time.sleep(2)

        # assert ile doğru mu diye kontrol et
        assert "Desktops" in driver.title

        driver.quit()

        """     fiyatı uygun olanı seç      """

    def test_uygun_urunu_sec(self):
        # driver başlatma ve siteye gitme
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/desktops")

        # fiyatı uygun ürünü seç
        driver.find_element(By.LINK_TEXT, "Desktop PC with CDRW").click()
        time.sleep(2)
        assert "Desktop PC with CDRW" in driver.title

        driver.quit()









