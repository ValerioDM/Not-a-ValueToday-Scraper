from contextlib import nullcontext
from warnings import catch_warnings
import scrapy
from scrapy.loader import ItemLoader

from valuetoday.items import CompanyItem

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ValueTodaySpider(scrapy.Spider):
    name = "valuetoday"
    allowed_domains = ["value.today"]
    start_urls = ['https://www.value.today/world/world-top-1000-companies?page=0']

    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))

        # getting all the companies on the page
        companies = response.css('div.views-field.views-field-title > h2 > a')

        self.logger.info('CYCLING COMPANIES ON THE PAGE')

        for company in companies:

            # get company url
            company_valuetoday_url = company.css('a::attr(href)').get()                             ##errore qui se non prende le singole compagnie        

            # go to the company page
            yield response.follow(company_valuetoday_url, self.parse_company)

        # go to Next page with companies
        for a in response.css('li.pager__item.pager__item--next > a'):                              ##errore qui se non trova l'ultima pagina/non termina
            yield response.follow(a, self.parse)

    def parse_company(self, response):

        path = 'valuetoday\driver\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        desired_capabilities = options.to_capabilities()
        driver = webdriver.Chrome(executable_path=path, desired_capabilities=desired_capabilities)

        driver.get(response.request.url)

        # Implicit wait
        driver.implicitly_wait(10)
        # Explicit wait
        wait = WebDriverWait(driver, 10)


        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.field.field--name-node-title.field--type-ds.field--label-hidden.field--item > h1 > a")))
            companyName = driver.find_elements_by_css_selector("div.field.field--name-node-title.field--type-ds.field--label-hidden.field--item > h1 > a")
            companyName = CompanyName[0].get_attribute('outerText')
        except:
            companyName = ''


        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-6.field.field--name-field-world-rank-sep-01-2021-.field--type-integer.field--label-above > div.field--item")))
            worldRank = driver.find_elements_by_css_selector("div.clearfix.col-sm-6.field.field--name-field-world-rank-sep-01-2021-.field--type-integer.field--label-above > div.field--item")
            worldRank = worldRank[0].get_attribute('outerText')
        except:
            worldRank = ''

        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-6.field.field--name-field-market-value-jan012021.field--type-float.field--label-above > div.field--item")))
            marketValue = driver.find_elements_by_css_selector("div.clearfix.col-sm-6.field.field--name-field-market-value-jan012021.field--type-float.field--label-above > div.field--item")
            marketValue = marketValue[0].get_attribute('outerText')
        except:
            marketValue = ''


        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-revenue-in-usd.field--type-float.field--label-inline > div.field--item")))
            annualRevenueUSD = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-revenue-in-usd.field--type-float.field--label-inline > div.field--item")
            annualRevenueUSD = annualRevenueUSD[0].get_attribute('outerText')
        except:
            annualRevenueUSD = ''

        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-headquarters-of-company.field--type-entity-reference.field--label-inline > div.field--items > div > a")))
            headquartersCountry = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-headquarters-of-company.field--type-entity-reference.field--label-inline > div.field--items > div > a")
            headquartersCountry = headquartersCountry[0].get_attribute('outerText')
        except:
            headquartersCountry = ''


        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-company-category-primary.field--type-entity-reference.field--label-inline > div.field--items > div")))
            company_Business = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-company-category-primary.field--type-entity-reference.field--label-inline > div.field--items > div")
            companBusiness = ""
            for c in company_Business:
                companBusiness = companBusiness + s.get_attribute('outerText') + ', '
        except:
            companyBusiness = ''

        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-company-sub-category-.field--type-entity-reference.field--label-above > div.field--items > div")))
            business_Sector = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-company-sub-category-.field--type-entity-reference.field--label-above > div.field--items > div")
            businessSector = ""
            for s in business_Sector:
                businessSector = businessSector + s.get_attribute('outerText') + ', '
        except:
            businessSector = ''


        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-ceo.field--type-entity-reference.field--label-above > div.field--items > div > a")))
            CEO = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-ceo.field--type-entity-reference.field--label-above > div.field--items > div > a")
            CEO = CEO[0].get_attribute('outerText')
        except:
            CEO = ''        


        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-founders.field--type-entity-reference.field--label-above > div.field--items > div")))
            founders_ = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-founders.field--type-entity-reference.field--label-above > div.field--items > div")
            founders = ""
            for s in founders_:
                founders = founders + s.get_attribute('outerText') + ', '
        except:
            founders = ''


        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-founded-year.field--type-integer.field--label-inline > div.field--item")))
            foundedYear = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-founded-year.field--type-integer.field--label-inline > div.field--item")
            foundedYear = foundedYear[0].get_attribute('outerText')
        except:
            foundedYear = ''

        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-employee-count.field--type-integer.field--label-inline > div.field--item")))
            nEmployees = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-employee-count.field--type-integer.field--label-inline > div.field--item")
            nEmployees = nEmployees[0].get_attribute('outerText')
        except:
            nEmployees = ''

        
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.clearfix.col-sm-12.field.field--name-field-employee-count.field--type-integer.field--label-inline > div.field--item")))
            webSite = driver.find_elements_by_css_selector("div.clearfix.col-sm-12.field.field--name-field-employee-count.field--type-integer.field--label-inline > div.field--item")
            webSite = webSite[0].get_attribute('origin')
        except:
            webSite = ''

            


    ##GLI STATICI NON CI SONO
        loader = ItemLoader(item=CompanyItem(), response=response)
        loader.add_value('companyName', companyName)
        loader.add_value('worldRank', worldRank)
        loader.add_value('marketValue', marketValue)
        loader.add_value('annualRevenueUSD', annualRevenueUSD)
        loader.add_value('headquartersCountry', headquartersCountry)
        loader.add_value('companyBusiness', companyBusiness)
        loader.add_value('businessSector', businessSector)
        loader.add_value('CEO', CEO)
        loader.add_value('founders', founders)
        loader.add_value('foundedYear', foundedYear)
        loader.add_value('nEmployees', nEmployees)
        loader.add_value('webSite', webSite)

        yield loader.load_item()