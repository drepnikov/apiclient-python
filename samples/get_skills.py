from voximplant.apiclient import VoximplantAPI, VoximplantException

if __name__ == "__main__":
    voxapi = VoximplantAPI("credentials.json")

    # Get two skills, but skip the first one.

    OFFSET = 1
    COUNT = 2
    
    try:
        res = voxapi.get_skills(offset=OFFSET, count=COUNT)
    except VoximplantException as e:
        print("Error: {}".format(e.message))
    print(res)
