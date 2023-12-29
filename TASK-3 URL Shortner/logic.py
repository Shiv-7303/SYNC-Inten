import requests


class Shortner:

    def __init__(self, url):
        self.url = url

    def get_shorten(self):
        main_url = "https://url-shortener-service.p.rapidapi.com/shorten"
        payload = {"url": f"{self.url}"}
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "8f0cfc0a75msh9764cf6ddb7cd1fp1f7851jsnc19bc89592da",
            "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
        }
        response = requests.post(main_url, data=payload, headers=headers)
        url_response = response.json()['result_url']
        return url_response
