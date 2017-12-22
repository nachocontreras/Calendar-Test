from init_variables import get_service
from config import user_key, categories
from collections import defaultdict
from datetime import datetime
import pprint
# import calendar

def get_events_list(calendar_id, minDate="", maxDate=""):
    results = {}
    page_token = None
    service = get_service()
    print(minDate, maxDate)
    while True:
        events = service.events().list(calendarId=calendar_id,
                                       pageToken=page_token).execute()
                                       # timeMax=maxDate, timeMin=minDate).execute()
        # print(events)
        for event in events['items']:
            try:
                ini = event["start"]["dateTime"]
                fin = event["end"]["dateTime"]
            except KeyError:
                ini = event["start"]["date"]
                fin = event["end"]["date"]
            results[event["summary"]] = (ini, fin)
        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return results


def manage_list_events():
    final = defaultdict(int)
    calendar_id = input("Ingrese mail de calendario")
    # minDate = datetime.strptime(input("Ingrese fecha inicio (31/12/1997): "), "%d/%m/%Y")
    # maxDate = datetime.strptime(input("Ingrese fecha termino (31/12/2000): "), "%d/%m/%Y")
    minDate = ""
    maxDate = ""
    events = get_events_list(calendar_id, minDate, maxDate)
    for name, dates in events.items():
        print(name, dates)
        for cat in categories:
            if cat in name:
                for user in user_key.values():
                    if user in name:
                        final[user] += categories[cat]
                        print(final[user])
                        break
                break
    print("-" * 50)
    return final
        
if __name__ == "__main__":
    final = manage_list_events()
    print(final)