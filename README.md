# imsosorry-itsonline
imsosorry its now accessible through API  
**THIS ENTIRE THING ALREADY EXISTS:** [api.letsbuilda.dev](https://github.com/letsbuilda/api.letsbuilda.dev)  
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
W̶a̶s̶ ̶t̶h̶e̶r̶e̶ ̶a̶n̶y̶ ̶r̶e̶a̶s̶o̶n̶ ̶f̶o̶r̶ ̶t̶h̶i̶s̶ ̶r̶e̶p̶o̶ ̶t̶o̶ ̶e̶x̶i̶s̶t̶?̶ ̶p̶r̶o̶b̶a̶b̶l̶y̶ ̶n̶o̶t̶.̶    
There's even less reason for this to exist now because, it already exists. Still worth it.  
Was it worth an hour of my weekend? probably not.  
It's funni tho.
