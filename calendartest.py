import google.auth
from googleapiclient.discovery import build

# Set up credentials
credentials, _ = google.auth.default()
service = build('calendar', 'v3', credentials=credentials)

# Define calendar IDs of the calendars you want to access
calendar_ids = ['primary', 'calendar.google.com/calendar/u/0?cid=MWUzYTgxZTIzZGIxNWRiNTM3MWFmZjgzNDM1ZTYyNmU5OTZlZjhmMjZmNzViMTMzMWFiMTdlYzBlZmFiMzdiYUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t']  # Add more calendar IDs as needed

# Retrieve events from each calendar
all_events = []
for calendar_id in calendar_ids:
    events_result = service.events().list(calendarId=calendar_id).execute()
    events = events_result.get('items', [])
    all_events.extend(events)

# Process the event data
for event in all_events:
    print(event['summary'], event['start'].get('dateTime', event['start'].get('date')))
