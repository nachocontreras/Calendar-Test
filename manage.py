from init_variables import get_service
from config import user_key, categories
from collections import defaultdict
import datetime
# import calendar

def get_events_list(calendar_id, minDate, maxDate):
    results = {}
    page_token = None
    service = get_service()
    while True:
        events = service.events().list(calendarId=calendar_id, pageToken=page_token, timeMax=maxDate, timeMin=minDate).execute()
        for event in events['items']:
            try:
                in = event["start"]["datetime"]
                fin = event["end"]["datetime"]
            except KeyError:
                in = event["start"]["date"]
                fin = event["end"]["date"]
            results[event["summary"]] = (in, fin) 
        page_token = events.get('nextPageToken')
        if not page_token:
          break
    results = {}

def manage_list_events():
    final = defaultdict(int)
    calendar_id = input("Ingrese mail de calendario")
    minDate = datetime.strptime(input("Ingrese fecha inicio (Jan 12 2017): "))
    maxDate = datetime.strptime(input("Ingrese fecha termino (Jan 12 2017): "))
    events = get_events_list(calendar_id, mindate, maxDate)
    for name, dates in events.items():
        print(name, date)
        for cat in categories:
            if cat in name:
                for user in user_key:
                    if user in name:
                        final[user_key[user]] += categories[cat]
                        print(final[user_key[user]])
                        break
                break
    return final
        
