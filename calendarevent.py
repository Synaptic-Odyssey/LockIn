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
    
#public_ics_url = "https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/private-cd3778bb335f55bf428dc4307e5a7994/basic.ics"
#https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/public/basic.ics

#ics_data = download_ics_file(public_ics_url)

def get_current_event(ics_data):
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
    
    ics_data = download_ics_file(url)
    if ics_data:
        current_event= get_current_event(ics_data)
    if current_event:
<<<<<<< Updated upstream
        # print(current_event)
        return current_event
    else:
        # print("No event currently scheduled.")
        return None
        

print(get_event("https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/private-cd3778bb335f55bf428dc4307e5a7994/basic.ics"))
=======
        return current_event
    else:
        return None
        

print(get_event("https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/private-cd3778bb335f55bf428dc4307e5a7994/basic.ics"))
>>>>>>> Stashed changes
