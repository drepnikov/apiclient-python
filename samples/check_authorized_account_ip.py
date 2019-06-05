from voximplant.apiclient import VoximplantAPI, VoximplantException

if __name__ == "__main__":
    voxapi = VoximplantAPI("credentials.json")

    AUTHORIZED_IP = "92.255.220.0/24"
    
    try:
        res = voxapi.check_authorized_account_ip(AUTHORIZED_IP)
    except VoximplantException as e:
        print("Error: {}".format(e.message))
    print(res)
