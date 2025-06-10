# openLinks
## A Script to open Job Links in Google Sheet
**Purpose/Goal:** This script is designed to take a list of links in a Google Sheet and open them in preparation for applying to to multiple jobs.  It will open a new instance of Chrome, then open each link in a new tab.
**Installation:**
<pre>
<code>
python3 -m venv venv
pip3 install -r requirements.txt
</code>
</pre>

**Usage:**
- Ensure we have a properly formatted *credentials.json* file in the root directory.  This will look like: 
<pre>
<code>
{
  "type": "service_account",
  "project_id": "employment-automation",
  "private_key_id": "e7133b0ae4ead42dac03d31a36d17821607d7b41",
  "private_key": "-----BEGIN PRIVATE KEY-----\<KEY>\n-----END PRIVATE KEY-----\n",
  "client_email": "employmentautomation@employment-automation.iam.gserviceaccount.com",
  "client_id": "101367580796631412044",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/employmentautomation%40employment-automation.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
</code>
</pre>

## Tips:
- You can use an autofill service (like [Simplify](simplify.jobs)) to fill the forms more quickly.
