import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_to_google_sheets(data, sheet_id, sheet_name, credentials_file):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    client = gspread.authorize(credentials)

    # Open the spreadsheet and create/get the worksheet
    sheet = client.open_by_key(sheet_id)
    try:
        worksheet = sheet.worksheet(sheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=sheet_name, rows="100", cols="10")

    # Clear the existing data
    worksheet.clear()

    # Insert headers
    headers = ["Company", "Title", "Location", "Posting Date", "Description", "Job URL"]
    worksheet.append_row(headers)

    # Insert job data
    for job in data:
        worksheet.append_row([job['Company'], job['Title'], job['Location'], job['Posting Date'], job['Description'], job['Job URL']])

    print(f"Data successfully saved to Google Sheets: {sheet_name}")
