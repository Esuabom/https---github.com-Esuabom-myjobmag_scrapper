from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait 


""" Arguments to be passed to scrape_jobs function:
1. Keyword: The particular job role you want to search for and scrape
2. no_jobs: The number of jobs you want to run
3. path: The path where Chrome driver is installed on your system
 """

def scrape_jobs(keyword= "data analyst", no_jobs= 10, path ="C:/Program Files (x86)/chromedriver_win32/chromedriver.exe"):
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path= path, options=options)
    driver.set_window_size(1120, 1000)    
    url = "https://www.myjobmag.com/"

    #Navigating to webpage
    driver.get(url)
    time.sleep(5)
 
    #Running your search query using keyword passed to function    
    search_element =  driver.find_element(By.ID, "search-key")
    search_element.send_keys(keyword)
    search_element1= driver.find_element(By.ID, "search-but")
    search_element1.click()
    time.sleep(5)
   
    #Scrapping jobs based on the no_jobs passed to function
    job_list = []
    for x in range(no_jobs):
        loop_no = driver.find_elements(By.XPATH, "//*/h2/a")
        element_no = 1
        for i in range (len(loop_no)):
            #scrapping data from each job returned by the search query
            try:
                search_results = driver.find_elements(By.XPATH, "//*/h2/a")[element_no].click()
                time.sleep(3)
            
                print("done")
                job_company_name= driver.find_element(By.XPATH, '//ul[@class="read-h1"]/li/h1').text
                subjob = driver.find_element(By.CLASS_NAME, "subjob-title").text
                print (subjob)
                job_by_type = driver.find_element(By.XPATH, '//a[contains(@href, "/jobs-by-type")]').text
                job_by_education = driver.find_element(By.XPATH, '//a[contains(@href, "/jobs-by-ed")]').text
                job_by_experience = driver.find_elements(By.XPATH, '//span[@class="jkey-info"]')[2].text
                job_by_field = driver.find_element(By.CSS_SELECTOR, "#printable > ul > li:nth-child(5) > span.jkey-info > a").text
                job_by_location= driver.find_element(By.CSS_SELECTOR, "#printable > ul > li:nth-child(4) > span.jkey-info > a").text
                job_by_qualification = driver.find_element(By.CSS_SELECTOR, "#printable > ul > li:nth-child(2) > span.jkey-info > a").text
                method_of_application= driver.find_element(By.CSS_SELECTOR, "#printable > div.mag-b.bm-b-30").text
            except:
                pass
            print(method_of_application + job_by_education + job_by_experience + job_by_field + job_by_location + job_by_qualification + job_by_type + job_company_name)
            job_list.append({"Job Type": job_by_type, "Qualification": job_by_qualification, "Experience": job_by_experience, "Location": job_by_location,
            "Job Field": job_by_field, "Job Title": subjob, "Name of Company": job_company_name, "Method of Application": method_of_application})
            print (job_list)
            element_no += 1
            driver.back()
            time.sleep (2)
        
        #Moving to the next page
        driver.find_element(By.CLASS_NAME, "").click()

    #Creating dataframe    
    df_jobs=pd.DataFrame(job_list)


scrape_jobs()
