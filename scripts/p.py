from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Set up the Google Play Console API credentials
creds = Credentials(
    token="YOUR_ACCESS_TOKEN",
    refresh_token="YOUR_REFRESH_TOKEN",
    token_uri="https://oauth2.googleapis.com/token",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)

# Create the Google Play Console API client
play_console = build("androidpublisher", "v3", credentials=creds)

# Specify the app details
app_id = "com.example.myapp"
start_date = "2023-01-01"
end_date = "2023-12-31"

# Convert the start and end dates to datetime objects
start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

# Iterate through the date range and fetch the download counts
current_date = start_date_obj
while current_date <= end_date_obj:
    try:
        response = play_console.statistics().downloads().get(
            packageName=app_id,
            startDate=current_date.strftime("%Y-%m-%d"),
            endDate=current_date.strftime("%Y-%m-%d")
        ).execute()

        download_counts = response["downloadStats"]["totalDownloads"]
        print(f"Downloads on {current_date.strftime('%Y-%m-%d')}: {download_counts}")

    except Exception as e:
        print(f"An error occurred for {current_date.strftime('%Y-%m-%d')}: {e}")

    current_date += timedelta(days=1)