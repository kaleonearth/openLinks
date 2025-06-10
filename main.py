import json
import os
from openlinks import open_urls

# --------- Load Config ---------
def get_config():
    """Load and return config from JSON file located in the script's directory."""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    with open(config_path) as f:
        return json.load(f)

def main():
    config=get_config()
    GOOGLE_SHEET_KEY = config["GOOGLE_SHEET_KEY"]
    open_urls(GOOGLE_SHEET_KEY)

if __name__ == "__main__":
    main()
