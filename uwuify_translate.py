import requests
from sys import argv,exit

def translate(meter: str,  text: str):
    text = text
    json = {"text": text, "uwu_meter": meter}
    r = requests.post(r"http://localhost/uwuify", json=json)
    print(r.text)

if len(argv) > 1:
    translate(argv[1], argv[2])
else:
    exit("\nno parameters given:\n\nMeter ('high', 'medium', 'low')\nText\n"),