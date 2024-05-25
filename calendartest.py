import requests
import icalendar
from datetime import datetime, timezone

def download_ics_file(public_ics_url):
    response = requests.get(public_ics_url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to download .ics file.")
        return None

def get_current_event_summary(ics_data):
    current_time = datetime.now(timezone.utc)
    cal = icalendar.Calendar.from_ical(ics_data)
    for component in cal.walk():
        if component.name == "VEVENT":
            start_time = component.get('dtstart').dt
            end_time = component.get('dtend').dt
            if start_time <= current_time <= end_time:
                return str(component.get('summary'))
    return None

def get_event(url):
    public_ics_url = url + "/public/basic.ics"
    ics_data = download_ics_file(public_ics_url)
    return get_current_event_summary(ics_data)

    


# if ics_data:
#     current_event_summary = get_current_event_summary(ics_data)
#     if current_event_summary:
#         print("Current Event Summary:", current_event_summary)
#     else:
#         print("No event currently scheduled.")