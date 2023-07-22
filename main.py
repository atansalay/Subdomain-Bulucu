import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
target_input = "google.com"


with open("subdomainList.txt", "r") as subdomain_List:
    for word in subdomain_List:
        word = word.strip() # stringi temizlemek için strip kullanabilriz boşluk , . gibi şeyleri temizleyebilriz.
        url = "http://" + word + "." + target_input
        response = make_request(url)
        if response:
            print("Found Subdomain    " + url)
