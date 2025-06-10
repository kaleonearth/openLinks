import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess
import time
import pandas as pd

def get_jobs(GOOGLE_SHEET_KEY):
    # --------- Google Sheets ---------
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(GOOGLE_SHEET_KEY)
    ws = sheet.worksheet("Job List")
    df = pd.DataFrame(ws.get_all_records())
    urls = df["Link"].dropna().tolist()
    return urls
    

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
def open_urls(GOOGLE_SHEET_KEY):
    urls = get_jobs(GOOGLE_SHEET_KEY)
    for url in urls:
        open_in_browser_tab(url)
        time.sleep(0.5)

print("All tabs opened in existing Chrome session.")