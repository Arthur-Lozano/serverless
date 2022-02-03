from http.server import BaseHTTPRequestHandler
from urllib import parse

import requests

# import requests
# from requests.exceptions import HTTPError


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "word" in dic:
            url = "https://api.thedogapi.com/v1/breeds"
            r = requests.get(url + dic["word"])
            data = r.json()
            print(data)
            definitions = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            message = str(definitions)
        else:
            message = "Pic a dog"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

        return
