Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = {}
type(data)
<class 'dict'>
data = dict()
type(data)
<class 'dict'>
data = {"name" : "John", "age" : 40}
data[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data[0]
KeyError: 0
data["name"]
'John'
data["age"]
40
data.keys()
dict_keys(['name', 'age'])
data.values()
dict_values(['John', 40])
data.items()
dict_items([('name', 'John'), ('age', 40)])
data["phone"] = 898989898
data
{'name': 'John', 'age': 40, 'phone': 898989898}
data["name"] = "Sam"
data
{'name': 'Sam', 'age': 40, 'phone': 898989898}
data.get("name")
'Sam'
data["name"]
'Sam'
data["email"]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data["email"]
KeyError: 'email'
data.get("email", "Not Available")
'Not Available'
data.get("email")
details = {"state":"MH", "city" : "Mumbai", "country" : "India"}
details
{'state': 'MH', 'city': 'Mumbai', 'country': 'India'}
data.update(details)
data
{'name': 'Sam', 'age': 40, 'phone': 898989898, 'state': 'MH', 'city': 'Mumbai', 'country': 'India'}
data.popitem()
('country', 'India')
data
{'name': 'Sam', 'age': 40, 'phone': 898989898, 'state': 'MH', 'city': 'Mumbai'}
data.pop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
data.popitem()
('city', 'Mumbai')
data
{'name': 'Sam', 'age': 40, 'phone': 898989898, 'state': 'MH'}
data.pop("age")
40
data
{'name': 'Sam', 'phone': 898989898, 'state': 'MH'}
data.fromkeys(["name", "phone"])
{'name': None, 'phone': None}
data
{'name': 'Sam', 'phone': 898989898, 'state': 'MH'}
data.update(details)
data
{'name': 'Sam', 'phone': 898989898, 'state': 'MH', 'city': 'Mumbai', 'country': 'India'}
for item in data:
    print(item)

    
name
phone
state
city
country
for item in data:
    print(item, "::", data[item])

    
name :: Sam
phone :: 898989898
state :: MH
city :: Mumbai
country :: India
for item in data.values():
    print(item)

    
Sam
898989898
MH
Mumbai
India
{i : i ** 2 for i in range(1,11)}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
{i : i ** 3 for i in range(1,11)}
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
data = [{}]
data = {"" : [], "" : []}
