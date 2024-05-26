import requests

def download_ics_file(public_ics_url):
    response = requests.get(public_ics_url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to download .ics file.")
        return None

# TODO: append /public/basic.ics to links
public_ics_url = "https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/public/basic.ics"

# Download the .ics file
ics_data = download_ics_file(public_ics_url)

# Process the .ics data as needed
if ics_data:
    
