import requests
url = "https://google.com"
header = {
    "User-Agent":"Nasa"
}
data = requests.get(url,headers=header)
print(data)