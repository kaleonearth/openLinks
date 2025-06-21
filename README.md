# openLinks
## A Script to open Job Links in a Google Sheet to optimize the job application process.
**Purpose/Goal:** This script is designed to take a list of links in a Google Sheet and open them in preparation for applying to to multiple jobs.  It will open a new instance of Chrome, then open each link in a new tab.
**Installation:**
<pre>
<code>
python3 -m venv venv
pip3 install -r requirements.txt
</code>
</pre>

**Usage:**
- Ensure we have a properly formatted *credentials.json* file in the root directory.  In your Google console we will need to create a *Service Account* and *Service Account Key*, which will be linked to a project. This will give us the *credentials.json* file we need. 
**Steps:** 
- Create a Google Sheet with the following column format: 

| Employer     | Position       | Link  |
|--------------|----------------|-------|
| Employer1    | Engineer       | Link1 |
| Employer2    | Designer       | Link2 |

- Create a Project and Service Account/Key Pair:
    - Ensure you have created a project where we can assign a service account and key.  Once created, select that project in the [Google Cloud Console](https://console.cloud.google.com).
    - Service Accounts can be created [here](https://console.cloud.google.com/iam-admin/serviceaccounts).
    - Click *Manage Service Accounts*
    - Click *Create Service Account*
    - Give the Service Account a relevant name, a Service Account ID if not satisfied with the one that's generated, and Service Account Description.
    - Click *Create and Continue*
    - Select the role of *Editor*.
    - Click *Continue*.
    - Click *Done*. 
    - In the [Service Accounts Page](https://console.cloud.google.com/iam-admin/serviceaccounts), click the link for the *Service Account* we will be using for authentication.
    - Click the *Keys* tab.
    - Click *Add Key*.  Select *JSON*, then click *Create*. A JSON file will be created that we will use as *credentials.json*. This will be automatically downloaded into your Downloads directory.
    - Once the key is created, formatting should look like: 
<pre>
<code>
{
  "type": "service_account",
  "project_id": "PROJECT_ID",
  "private_key_id": "PRIVATE_KEY_ID",
  "private_key": "-----BEGIN PRIVATE KEY-----\KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "EMAIL.iam.gserviceaccount.com",
  "client_id": "CLIENTID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/employmentautomation%40employment-automation.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
</code>
</pre>
- Share SS created above with Service Account email address by clicking "File > Share With Others" 
- Create a *config.json* file that has the Google Sheets ID.  This can be found in the URL of the sheet, see below.
<pre>
<code>
{
    "AUTOMATION_SHEET_KEY": "JOB_AUTOMATION_SS_KEY",
    "EMPLOYMENT_SHEET_KEY": "EMPLOYMENT_SS_KEY"
}
</pre>
</code>

- If your Google sheet URL is: `https://docs.google.com/spreadsheets/d/1x9piz0Jwwai-It7KS8ng_floXgXNxLlOaBCDeFG_aa/edit?gid=0#gid=0` then the *SS_ID* above will be: `1x9piz0Jwwai-It7KS8ng_floXgXNxLlOaBCDeFG_aa`.
- Run the main.py file.
<pre>
<code>
python3 main.py
</pre>
</code>


## Tips:
- You can use an autofill service (like [Simplify](simplify.jobs)) to fill the forms more quickly.
