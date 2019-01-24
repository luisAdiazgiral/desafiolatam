import requests
import json
tmp_dic={}
html=""

def request(url,api_k):
    newurl=url + api_k
    print(newurl)
    return newurl

def build_web_page(data):
    photos=map(lambda x: "<li>"+"<img src='"+x["img_src"]+"'>'"+"</li>",data["photos"])
    html=""
    html+="<html>"
    html+="<head>"
    html+="<title>Fotos Api Nasa</title>"
    html+="</head>"
    html+="<body>"
    html+="<ul>"
    for x in photos:
        html+=x
    html+="</ul>"
    html+="La cantidad de fotos es"
    html+="</body>"
    html+="</html>"
    print(html)
    with open("output.html", "w") as f:
        f.write(html)
    
    
    
url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&"
api_k="api_key=XsAbNWz8GvMs6IaI7Y4EhROzR0vkjcQNiG6ah6Wc"
nurl= request(url,api_k)

respuesta = requests.request("GET",nurl)
results = json.loads(respuesta.text)
build_web_page(results)