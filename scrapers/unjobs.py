from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_un_jobs(driver):
    """Scrape job listings from UN Jobs."""
    UNJOBS_URL = "https://unjobs.org/duty_stations/nbo"
    jobs = []

    try:
        driver.get(UNJOBS_URL)
        wait = WebDriverWait(driver, 20)

        # Wait for the job listings to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job")))

        # Find all job elements
        job_elements = driver.find_elements(By.CLASS_NAME, "job")

        for job_element in job_elements:
            try:
                # Extract job title and link
                title_element = job_element.find_element(By.CLASS_NAME, "jtitle")
                title = title_element.text
                link = title_element.get_attribute("href")

                # Extract organization/company name
                organization = job_element.text.split("\n")[1].strip()

                # Extract updated time
                updated_time_element = job_element.find_element(By.CLASS_NAME, "upd")
                updated_time = updated_time_element.text if updated_time_element else "Not available"

                # Extract closing date if available
                closing_date_element = job_element.find_elements(By.TAG_NAME, "span")
                closing_date = (
                    closing_date_element[0].text.split(": ")[1]
                    if closing_date_element and "Closing date:" in closing_date_element[0].text
                    else "Not specified"
                )

                # Extract description if available
                description = "Description not available"

                # Use updated_time as a placeholder for posting date (if relevant)
                posting_date = updated_time  # Adjust this logic based on data availability

                # Append the job details to the list
                jobs.append({
                    "Company": organization,
                    "Title": title,
                    "Location": "Nairobi, Kenya",
                    "Posting Date": posting_date,
                    "Closing Date": closing_date,
                    "Description": description,
                    "Job URL": link,
                })

            except Exception as e:
                print(f"Error processing a job element: {e}")
                continue

    except Exception as e:
        print(f"Error scraping UN Jobs: {e}")
    finally:
        driver.quit()

    return jobs
