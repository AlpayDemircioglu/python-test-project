from selenium import webdriver
from selenium.webdriver.common.by import By

"""

TR

Bu Testimiz'de demowebshop web sitesinin ana menü çubuğunda bulunan çeşitli sekmelerin doğruluğunu kontrol edeceğiz
 
İNG

in this test , we will check the items on the main menu bar

"""


class TestDemesne():

    def test_home_page(self):
        driver = webdriver.Chrome()
        driver.get("https://demowebshop.tricentis.com/")
        driver.maximize_window()

        expected = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS", "JEWELRY", "GIFT CARDS"]

        elements = driver.find_elements(By.CSS_SELECTOR, "ul.top-menu>li>a")

        actual = []

        for i in elements:
            actual.append(i.text)

        for i in range(len(expected)):
            assert expected[i] == actual[i]

        driver.quit()












