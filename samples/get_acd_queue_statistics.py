from voximplant.apiclient import VoximplantAPI
import datetime
import pytz

if __name__ == "__main__":
    voxapi = VoximplantAPI("credentials.json")

    # Get statistics for all queues from the specified date

    FROM_DATE = datetime.datetime(2017, 1, 1, 0, 0, 0, pytz.utc)
    
    res = voxapi.get_acd_queue_statistics(FROM_DATE)
    print(res)
