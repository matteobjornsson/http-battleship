#import http.client
import urllib
import requests
import sys

host = sys.argv[1]
port = sys.argv[2]
x = sys.argv[3]
y = sys.argv[4]

response = requests.post("http://" + host + ":" + port, {"x": x, "y": y})
content_parsed = urllib.parse.parse_qs(response.content.decode("utf-8"))

print(f"HTTP Status code: {response.status_code} {response.reason}")
print(f"Response content: {content_parsed}")

