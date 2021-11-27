import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

stars = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/darren/Desktop/Class127")
browser.get(stars)
time.sleep(10)

def scrap():
    headers = ["Name","Light-Years From Earth","Planet Mass","Stellar Magnitude","Discovery Date"]
    planetData = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parster")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            tempList = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    tempList.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        tempList.append(li_tag.contents[0])
                    except:
                        tempList.append("")
            planetData.append(tempList)
        browser.find_element_by_xpath("//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[1]/a").click()
    with open("Scrap.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)

scrap()