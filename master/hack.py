import requests
username = 'BuckBeak'
api_key = 'vEmLU3bpNq7poVGFy4YYgUXVhKw48YSN'

def eventz():
    url = "https://clist.by/api/v1/contest/?username={}&api_key={}".format(username,api_key)
    req = requests.get(url)
    if req.status_code == 200:
        lst = req.json()
        message = ""
        for i in range(77,88):
            message += "**Event: **" + lst['objects'][i]['event'] + '\n' + "**Link: **" + lst['objects'][i]['href'] + '\n\n'

        return message
    else:
        message = "Check connections"
        return message    