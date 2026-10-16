from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PopulationPage():
    URL = "https://www.theworldcounts.com/humanity/populations/world-population"
    POPULATION = "(//div[@class='hero-cine__counter'])"


    def __init__(self,driver):
        #store the selenium driver inside this page object
        self.driver = driver

        #create an explicit of 10 seconds
        self.wait = WebDriverWait(driver, 20)
        #xpath for the population count
        #POPULATION = "(//div[@class='hero-cine__counter'])"
    def open_page(self):
        #open the world population page
        self.driver.get(self.URL)

    def get_population(self):
        #wait untill the population element is present in the DOM

         population_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.POPULATION)))
        # get the text displayed by the element
         population =  population_element.text

         #Return the population value
         return population


