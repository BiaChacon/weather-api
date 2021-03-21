import time
from selenium import webdriver
from bs4 import BeautifulSoup as soup


class Temperature:
    def get_temperature():
        # Fazer a raspagem dos dados
        url = 'https://portal.inmet.gov.br/'
        driver = webdriver.Firefox()
        driver.get(url)

        # tempo para página carregar
        time.sleep(5)

        body = driver.find_element_by_tag_name('body')
        html = body.get_attribute('innerHTML')
        soupPage = soup(html, 'html5lib')
        noticiasList = soupPage.findAll( "a", class_='blue-link')
                
        temperature = soupPage.find("div", class_='temp-min font-dados pb-sm-1')
        tempformat = temperature.get_text().split("º")
        temp = float(tempformat[0])

        humidity = soupPage.find("div", class_='prob-color font-dados pb-sm-1')
        humformat = humidity.get_text().split("%")
        hum = float(humformat[0])

        driver.close()

        return [temp,hum]
