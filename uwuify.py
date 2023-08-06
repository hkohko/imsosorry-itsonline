import requests
from sys import exit


def translate():
    try:
        meter = input("Meter: ")
        if meter == "":
            print("Meter is set to High")
            meter = "high"
        text = input("Text: \n\n")
        json = {"text": text, "uwu_meter": meter}
        r = requests.post(r"https://uwuify-1-l3975896.deta.app/uwuify", json=json)
        print(r.text)
        translate()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)


translate()
