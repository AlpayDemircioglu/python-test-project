"""
TR

Ana sayfada bulunan Seçtiğimiz bir ürünün ana sayfasında ve ürünü açınca gelen ürün sayfasında ki isim ve fiyat aynı mı bunu test edeceğiz

İNG

in this test , when we select one product  is the product name and price same or not ? we will test

"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUrunler:

    def test_urune_tiklayinca_fiyat_ve_isim_kontrol(self):
        driver = webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()

        anasayfa_urun_linki = driver.find_element(By.CSS_SELECTOR, "h2.product-title a")
        anasayfa_urun_ismi = anasayfa_urun_linki.text.strip()

        anasayfa_urun_fiyati = driver.find_element(By.CSS_SELECTOR, "span.price.actual-price").text.strip()

        anasayfa_urun_linki.click()

        urun_sayfasi_ismi = driver.find_element(By.CSS_SELECTOR, "div.product-name h1").text.strip()

        urun_sayfasi_fiyati = driver.find_element(By.CSS_SELECTOR, "div.product-price span").text.strip()

        assert anasayfa_urun_ismi == urun_sayfasi_ismi
        assert anasayfa_urun_fiyati == urun_sayfasi_fiyati

        driver.quit()
