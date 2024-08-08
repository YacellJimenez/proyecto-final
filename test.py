from selenium import webdriver
import unittest

class TestHolaMundo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_hola_mundo(self):
        self.driver.get("file:///C:/Users/PC/Desktop/Ansible%20proyecto/pag_holamundo/index.html")
        self.assertIn("Hola Mundo", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
