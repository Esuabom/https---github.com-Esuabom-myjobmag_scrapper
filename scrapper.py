from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait 


#Arguments to be passed to scrape_jobs function:
#1. Keyword: The particular job role you want to search for and scrape
#2. jobs: The number of jobs you want to run
#3. verbose: 
#4. path: The path where Chrome driver is installed on your system
#5. 


def scrape_jobs(keyword= "data analyst", no_jobs= 10, path ="C:/Program Files (x86)/chromedriver_win32/chromedriver.exe"):
    
    '''Gathers jobs as a dataframe, scraped from myjobmag.com'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    
    driver = webdriver.Chrome(executable_path= path, options=options)
    driver.set_window_size(1120, 1000)    
    url = "https://www.myjobmag.com/"
    driver.get(url)
    time.sleep(10)
    search_element =  driver.find_element(By.ID, "search-key")
    search_element.send_keys(keyword)
    search_element1= driver.find_element(By.ID, "search-but")
    search_element1.click()
    time.sleep(5)
    for x in range(5):
        print ("testing")
    job_list = []
    element_no = 1
    for i in range (17):
        search_results = driver.find_elements(By.XPATH, "//*/h2/a")[element_no].click()
        print("done before")
        time.sleep(5)
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
        print(method_of_application + job_by_education + job_by_experience + job_by_field + job_by_location + job_by_qualification + job_by_type + job_company_name)
        job_list.append({"Job Type": job_by_type, "Qualification": job_by_qualification, "Experience": job_by_experience, "Location": job_by_location,
        "Job Field": job_by_field, "Job Title": subjob, "Name of Company": job_company_name, "Method of Application": method_of_application})
        print (job_list)
        element_no += 1
        driver.back()
        time.sleep (5)

        






scrape_jobs()






"""  jobs = []

    while len(jobs) < no_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(4)

        #Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element_by_class_name("selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()  #clicking to the X.
        except NoSuchElementException:
            pass

        
        #Going through each job in this page
        job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  #You might 
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                    location = driver.find_element_by_xpath('.//div[@class="location"]').text
                    job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
            except NoSuchElementException:
                salary_estimate = -1 #You need to set a "not found value. It's important."
            
            try:
                rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #
Company

            try:
                driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()

                try:
                    #

                    #    Headquarters
                    #    San Francisco, CA
                    #

                    headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                except NoSuchElementException:
                    headquarters = -1

                try:
                    size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
                except NoSuchElementException:
                    revenue = -1

                try:
                    competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                except NoSuchElementException:
                    competitors = -1

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                competitors = -1

                
            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Headquarters" : headquarters,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            "Competitors" : competitors})
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//li[@class="next"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.


     

#This line will open a new chrome window and start the scraping.
df = get_jobs("data scientist", 5, False)
df


     
Progress: 0/5
Progress: 1/5
Progress: 2/5
Progress: 3/5
Progress: 4/5
Progress: 5/5 """