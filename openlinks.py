import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess
import time
import pandas as pd


def get_jobs(AUTOMATION_SHEET_KEY):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(AUTOMATION_SHEET_KEY)
    ws = sheet.worksheet("Job List")
    df = pd.DataFrame(ws.get_all_records())
    jobs = []
    for _, row in df.iterrows():
        if pd.notna(row.get("Link")):
            jobs.append({
                "company": row.get("Employer"),
                "position": row.get("Position"),
                "link": row.get("Link"),
                "date_applied": row.get("Date Applied", time.strftime("%Y-%m-%d"))
            })
    return jobs
    

# --------- AppleScript Firefox Control ---------
def open_in_browser_tab(url):
    script = f'''
    tell application "Chrome"
        activate
        open location "{url}"
    end tell
    '''
    subprocess.run(["osascript", "-e", script])

# --------- Open Links in Separate Tabs in Chrome ---------
def open_urls(AUTOMATION_SHEET_KEY, EMPLOYMENT_SHEET_KEY):
    jobs = get_jobs(AUTOMATION_SHEET_KEY)
    if not jobs:
        print("No jobs found in the Job List.")
        return
    for job in jobs:
        open_in_browser_tab(job["link"])
        time.sleep(0.5)
        update_job_search_sheet(
            EMPLOYMENT_SHEET_KEY,
            job["company"],
            job["position"],
            job["link"],
            job["date_applied"]
        )


# --------- Update Employment SS with Jobs Being Applied To ---------
def update_job_search_sheet(EMPLOYMENT_SHEET_KEY, company, position, link, date_applied):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(EMPLOYMENT_SHEET_KEY)
    ws = sheet.worksheet("Job Search")
    
    # Find the first empty row
    next_row = len(ws.get_all_values()) + 1
    ws.update_cell(next_row, 1, company)
    ws.update_cell(next_row, 2, position)
    ws.update_cell(next_row, 4, link)
    ws.update_cell(next_row, 5, date_applied)

print("All tabs opened in existing Chrome session.")