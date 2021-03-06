from voximplant.apiclient import VoximplantAPI, VoximplantException
import pytz
import datetime

if __name__ == "__main__":
    voxapi = VoximplantAPI("credentials.json")

    # Get statistics for all queues from the specified date

    FROM_DATE = datetime.datetime(2017, 1, 1, 0, 0, 0, pytz.utc)
    
    try:
        res = voxapi.get_acd_queue_statistics(FROM_DATE)
    except VoximplantException as e:
        print("Error: {}".format(e.message))
    print(res)
