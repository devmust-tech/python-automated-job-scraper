from utils.webdriver import setup_driver
from utils.sheets import save_to_google_sheets
from scrapers.safaricom import scrape_safaricom_jobs
from scrapers.airtel import scrape_airtel_jobs
from scrapers.jamii import scrape_jamii_jobs
from scrapers.unjobs import scrape_un_jobs


# Configurations
DRIVER_PATH = r"C:\Users\Lenovo\Downloads\edgedriver_win64\msedgedriver.exe"
CREDENTIALS_FILE = r"C:\Users\Lenovo\Downloads\windy-energy-424106-s3-8dc1609bbfa8.json"
SHEET_ID = "18d88ANCBZc2UNbfiX6BUscfQJbQnD4wGthlDghy-GAs"

if __name__ == "__main__":
    print("Starting job scrapers...")
    driver = setup_driver(DRIVER_PATH)

    try:
        safaricom_jobs = scrape_safaricom_jobs(driver)
        airtel_jobs = scrape_airtel_jobs(driver)
        jamii_jobs = scrape_jamii_jobs(driver)


        if safaricom_jobs:
            print("Saving Safaricom jobs...")
            save_to_google_sheets(safaricom_jobs, SHEET_ID, "Safaricom", CREDENTIALS_FILE)

        if airtel_jobs:
            print("Saving Airtel jobs...")
            save_to_google_sheets(airtel_jobs, SHEET_ID, "Airtel", CREDENTIALS_FILE)

        if jamii_jobs:
            print("Saving Jamii Telecom jobs...")
            save_to_google_sheets(jamii_jobs, SHEET_ID, "Jamii Telecoms", CREDENTIALS_FILE)

        un_jobs = scrape_un_jobs(driver)
        if un_jobs:
            print("Saving UN Jobs to Google Sheets...")
            save_to_google_sheets(un_jobs, SHEET_ID, "UN Nairobi Jobs", CREDENTIALS_FILE)

    finally:
        driver.quit()
        print("Scraping complete.")
