import requests
import re

# В данном случае запрос request.get заменен на загрзку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()

print(re.findall(r'<h3.*>(.*)</h3>', text))
# По итогу вы так же получаете код сайта в виде одной строки

response = requests.get('http://www.columbia.edu/~fdc/sample.html')

if response.status_code == 200:

    for element in re.findall(r'<h3 .*>(.*)</h3>', response.text):
        print(element)
