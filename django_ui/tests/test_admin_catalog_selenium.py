import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from shop.models import Item


class TestUpdateQualityButton(StaticLiveServerTestCase):
    """
    Test fonctionnel Selenium : clic sur le bouton "Mettre à jour la qualité"
    et vérification que les valeurs Quality ont changé.
    """
    fixtures = ["tests/fixtures/test_data_catalog_update_quality.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Configuration Chrome Headless (facultatif)
        chrome_options = Options()
#        chrome_options.add_argument("--headless=new")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_update_quality_button(self):
        driver = self.driver
        url = f"{self.live_server_url}/shop_admin/catalog/"
        driver.get(url)

        # Vérifie que la page affiche les articles initiaux
        rows = driver.find_element(By.ID, "shop_admin_catalog_table").find_elements(By.TAG_NAME, "tr")

        assert len(rows) == 3
        assert "20" in rows[0].text

        time.sleep(5.0)

        # --- Action : clic sur le bouton ---
        update_button = driver.find_element(By.ID, "shop_admin_update_quality_button")
        print ("bouton : ", update_button.text)
        update_button.click()

        # L’action redirige vers la même page : attendre un petit délai
        time.sleep(5.0)
        driver.refresh()  # au cas où la redirection n’est pas automatique

        # --- Vérification : valeurs de qualité mises à jour ---
        updated_rows = driver.find_element(By.ID, "shop_admin_catalog_table").find_elements(By.TAG_NAME, "tr")
        updated_texts = [r.text for r in updated_rows]

        # Vérifie qu’elles ont décru selon la logique de votre vue
        for old, row_text in zip([20, 7, 1], updated_texts):
            expected_new_quality = max(0, old - 1)
            assert str(expected_new_quality) in row_text, f"Qualité non mise à jour pour {row_text}"

        print("✅ Test Selenium : bouton 'Mettre à jour la qualité' fonctionne correctement.")