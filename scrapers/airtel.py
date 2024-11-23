from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_airtel_jobs(driver):
    AIRTEL_URL = "https://erey.fa.em3.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/requisitions"
    jobs = []

    try:
        driver.get(AIRTEL_URL)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results-jobs-list")))

        job_elements = driver.find_elements(By.XPATH, "//li[@data-qa='searchResultItem']")
        for job_element in job_elements:
            title = job_element.find_element(By.CLASS_NAME, "job-tile__title").text
            location = job_element.find_element(By.CLASS_NAME, "job-list-item__job-info-value").text
            posting_date = job_element.find_element(By.CLASS_NAME, "job-list-item__job-info-value").text
            description = job_element.find_element(By.CLASS_NAME, "job-list-item__description").text
            link = job_element.find_element(By.CLASS_NAME, "job-list-item__link").get_attribute("href")

            jobs.append({
                'Company': 'Airtel',
                'Title': title,
                'Location': location,
                'Posting Date': posting_date,
                'Description': description,
                'Job URL': link
            })

    except Exception as e:
        print(f"Error scraping Airtel jobs: {e}")
    return jobs
