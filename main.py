import requests, time
from random import randint as rand
ReportCount = 0

def Report(ID: int):
    global ReportCount
    while True:
        try:
            Reason = rand(0,12000)
            data = requests.get(f"https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={ID}&owner_id={ID}&reason={Reason}")
            ReportCount += 1
            if data.json()["status_code"] == 0:
                print(f"Reported {ReportCount} | Reason : {Reason}" )
            elif not data.status_code == 200:
                print(f"Failed {ReportCount} | Reason : {Reason} | Waiting a little bit |")
                time.sleep(5)
            else:
                print(f"Failed {ReportCount} | Reason : {Reason} | Waiting a little bit |")
                time.sleep(5)

        except KeyboardInterrupt:
            exit(-1)
        except:
            print(f"Failed {ReportCount} | Reason : {Reason} | Waiting a little bit |")
            time.sleep(5)

def GetID(Username):
    if not Username.startswith("@"):
        Username = "@"+Username
    try:
        reqs = requests.get(f"https://www.tiktok.com/node/share/user/@{Username}")
        return reqs.json()["user"]["id"], 1
    except:
        return "Failed to get user id, please put the user id your self", 0

def Start():
    Username = input("Username : @")
    Id = GetID(Username)
    if Id[1] == 0:
        print(Id[0])
        Id = int(input("User ID : "))
        Report(Id)
    else:
        Report(Id)

Start()