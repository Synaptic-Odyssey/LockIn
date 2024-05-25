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

#TODO append /public/basic.ics
public_ics_url = "https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/public/basic.ics"

ics_data = download_ics_file(public_ics_url)

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


if ics_data:
    current_event_summary = get_current_event_summary(ics_data)
    if current_event_summary:
        print("Current Event Summary:", current_event_summary)
    else:
        print("No event currently scheduled.")