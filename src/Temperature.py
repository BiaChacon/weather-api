import time
from selenium import webdriver
from bs4 import BeautifulSoup as soup


class Temperature:
    def get_temperature():
        # Fazer a raspagem dos dados
        url = 'https://weather.com/weather/today/l/-15.83,-47.92?par=google&temp=c'
        driver = webdriver.Firefox()
        driver.get(url)

        # tempo para página carregar
        time.sleep(5)

        contentTemp = driver.find_elements_by_css_selector(
            "span[class='CurrentConditions--tempValue--3KcTQ']")
        valueT = contentTemp[0].get_attribute('innerHTML')
        tempValue = valueT.replace("°", "")
        temp = float(tempValue)

        contentHum = driver.find_elements_by_css_selector(
            "span[data-testid='PercentageValue']")
        valueT = contentHum[0].get_attribute('innerHTML')
        print(valueT)
        humValue = valueT.replace("%", "")
        hum = float(humValue)

        driver.close()

        return [temp,hum]
