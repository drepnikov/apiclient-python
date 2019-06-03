from voximplant.apiclient import VoximplantAPI

if __name__ == "__main__":
    voxapi = VoximplantAPI("credentials.json")

    # Add the 92.255.220.0/24 network to the white list.

    AUTHORIZED_IP = "92.255.220.0/24"
    
    res = voxapi.add_authorized_account_ip(AUTHORIZED_IP)
    print(res)
