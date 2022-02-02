import requests
personalUse = 'PERSONAL USE'
secret = 'SECRET'
Username = 'USERNAME'
Password = 'PASSWORD'

def connect():
    client_auth = requests.auth.HTTPBasicAuth(personalUse, secret)
    post_data = {"grant_type": "password", "username": Username, "password": Password}
    headers = {"User-Agent": "karmaextractor/0.1 by tahiraslam8k"} 
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

    resData = response.json()
    access_token = resData['access_token']

    headers = {"Authorization": f"bearer {access_token}", "User-Agent": "karmaextractor/0.1 by tahiraslam8k"}
    response = requests.get("https://oauth.reddit.com/api/v1/me/karma", headers=headers)
    data = response.json()
    new_data = data['data']
    return new_data


def saveFile():
    new_data = connect()
    length = len(new_data)
    list = ['ethtrader','CryptoCurrency','Vechain','dankmemes','HydroHomies']
    f = open("currentKarma.txt", "w")
    for i in range(length):
        if new_data[i]['sr'] in list:
            toWrite = f"[{new_data[i]['sr']}](//www.reddit.com/r/{new_data[i]['sr']}) | {new_data[i]['link_karma']} | {new_data[i]['comment_karma']} \n"
            f.write(str(toWrite))
    f.close()
saveFile()



