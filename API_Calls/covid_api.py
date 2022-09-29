Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import urllib.request as url
import json
path = "https://data.covid19india.org/states_daily.json"
response = url.urlopen(path)
data = json.load(response)
type(data)
<class 'dict'>
states = data["states"]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    states = data["states"]
KeyError: 'states'
states = data["states_daily"]
len(states)
1563
states[0]
{'an': '0', 'ap': '1', 'ar': '0', 'as': '0', 'br': '0', 'ch': '0', 'ct': '0', 'date': '14-Mar-20', 'dateymd': '2020-03-14', 'dd': '0', 'dl': '7', 'dn': '0', 'ga': '0', 'gj': '0', 'hp': '0', 'hr': '14', 'jh': '0', 'jk': '2', 'ka': '6', 'kl': '19', 'la': '0', 'ld': '0', 'mh': '14', 'ml': '0', 'mn': '0', 'mp': '0', 'mz': '0', 'nl': '0', 'or': '0', 'pb': '1', 'py': '0', 'rj': '3', 'sk': '0', 'status': 'Confirmed', 'tg': '1', 'tn': '1', 'tr': '0', 'tt': '81', 'un': '0', 'up': '12', 'ut': '0', 'wb': '0'}
states[0][0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    states[0][0]
KeyError: 0
states[0]'
SyntaxError: unterminated string literal (detected at line 1)
states[0]['dl']
'7'
states[0]['up']
'12'
states[0]['tt']
'81'
