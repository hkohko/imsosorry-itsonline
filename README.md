# imsosorry-itsonline
imsosorry its now accessible through API

built on the amazing, legendary, the one and only [imsosorry](https://github.com/letsbuilda/imsosorry)

# How to use  
run the web server
```
python app\main.py
```
Write your text in a json body and send a POST request through `localhost/uwuify`  
```python
import requests

text = "You are the chosen one."
json = {"text": text}
r = requests.post(r"http://localhost/uwuify", json=json)

print(r.text)
```
```
"you~ awe t-the c-chosen onye."
```

Accepts `uwu_meter` in json body with `"high", "medium", "low"` value.  
Set to `"medium"` by default.  
```python
import requests

text = "You are the chosen one."
for meter in ("low", "medium", "high"):
    json = {"text": text, "uwu_meter": meter}
    r = requests.post(r"http://localhost/uwuify", json=json)
    print(r.text)
```
```
"you awe the chosen o-onye."
"you a-awe~ t-the~ c-chosen~ o-onye."
"you~ a-awe~ t-the~ c-chosen~ onye~ 😳 "
```
`uwu_meter` values are in a range. You should see a gap in variety of results using the same text.  
```python
import requests

text = "You are the chosen one."
for _ in range(3):
    json = {"text": text, "uwu_meter": "high"}
    r = requests.post(r"http://localhost/uwuify", json=json)
    print(r.text)
```  
```
"you~ a-awe~ t-the~ c-chosen~ o-onye~ >_< "
"you a-awe~ the~ c-chosen~ o-onye~ ^^ "
"you~ a-awe~ t-the~ chosen~ o-onye."
```
Was there any reason for this repo to exist? probably not.  
Was it worth an hour of my weekend? probably not.  
It's funni tho.
