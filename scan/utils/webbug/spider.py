import requests


def get_site(url):
    response = requests.get(url)
    with open("file.txt") as f:
        content = response.content.decode("utf-8")
        f.write(content)
