# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from itemloaders.processors import MapCompose, TakeFirst



class CompanyItem(Item):
    companyName  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    worldRank  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    marketValue  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    annualRevenueUSD  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    headquartersCountry  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    companyBusiness  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    businessSector  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    CEO  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    founders  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    foundedYear  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    nEmployees  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
    webSite  = Field(
        input_processor = MapCompose(str.strip),
        output_processor = TakeFirst()
    )
