
def scrape_jamii_jobs(driver):
    """Scrape Jamii Telecom job listings."""
    JTL_URL = "https://careers.jtl.co.ke/openings"
    jobs = []

    try:
        driver.get(JTL_URL)
        wait = WebDriverWait(driver, 20)

        # Wait for job listings to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "card")))

        # Find job elements
        job_elements = driver.find_elements(By.CLASS_NAME, "card")

        for job_element in job_elements:
            try:
                # Extract job title
                title_element = job_element.find_element(By.CLASS_NAME, "card-title")
                title = title_element.text

                # Extract job URL
                link = title_element.find_element(By.TAG_NAME, "a").get_attribute("href")

                # Extract job reference number
                reference_element = job_element.find_element(By.CLASS_NAME, "card-subtitle")
                reference = reference_element.text if reference_element else "No reference"

                # Extract job type and department
                type_department_element = job_element.find_elements(By.CLASS_NAME, "card-subtitle")[1]
                type_department = type_department_element.text if type_department_element else "No details"

                # Extract posting and expiry dates
                dates_element = job_element.find_elements(By.CLASS_NAME, "card-subtitle")[2]
                dates = dates_element.text if dates_element else "No dates"

                # Extract job description (truncated)
                description_element = job_element.find_element(By.CLASS_NAME, "card-text")
                description = description_element.text if description_element else "No description"

                # Append the job data
                jobs.append({
                    'Company': 'Jamii Telecom',
                    'Title': title,
                    'Location': "Not specified",  # Default Location
                    'Reference': reference,
                    'Details': type_department,
                    'Posting Date': dates.split('|')[0].strip() if '|' in dates else dates,  # Extract posting date
                    'Expiry Date': dates.split('|')[1].strip() if '|' in dates else "Not specified",  # Extract expiry date
                    'Description': description,
                    'Job URL': link
                })
            except Exception as e:
                print(f"Error parsing a job element: {e}")
                continue

    except Exception as e:
        print(f"Error scraping Jamii Telecom jobs: {e}")
    return jobs
