"""
book sekmesşne tıklayınca çıkan ilk ürünün listelerdeki isim ve fiyatı ürünü açınca da doğru mu kontrol et
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver


from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUrunSayfasiniAcma:

    def test_secilen_urun_kontrolu(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")

        driver.find_element(By.LINK_TEXT, "Books").click()

        baslik = driver.find_element(By.TAG_NAME, "h1")
        assert baslik.text == "Books"

        driver.quit()

    def test_ilk_urunu_sec(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/books")

        ilk_urun = driver.find_element(By.CSS_SELECTOR, "h2.product-title a")
        ilk_urun_ismi = ilk_urun.text.strip()

        ilk_urun_fiyat = driver.find_element(By.CSS_SELECTOR, "span.price.actual-price")
        ilk_urun_fiyati = ilk_urun_fiyat.text.strip()

        ilk_urun.click()

        secilen_urun_isim = driver.find_element(By.CSS_SELECTOR, "div.product-name h1").text.strip()
        secilen_urun_fiyat = driver.find_element(By.CSS_SELECTOR, "span.price-value-13").text.strip()

        assert ilk_urun_ismi == secilen_urun_isim
        assert ilk_urun_fiyati == secilen_urun_fiyat

        driver.quit()







