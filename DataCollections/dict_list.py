# data = {
#     "names" : ["John", "Sam", "Max", "Tom", "Nick"],
#     "age" : [45,33,47,14,64],
#     "city" : ["delhi","pune","mumbai","chennai","chennai"]
# }
#
# for i in range(len(data["names"])):
#     if data["age"][i] > 40:
#         print(data["names"][i], data["age"][i], data["city"][i])

data = [
    {"name" : "John", "age" : 40, "city" : "delhi"},
    {"name" : "Max", "age" : 49, "city" : "noida"},
    {"name" : "Sam", "age" : 34, "city" : "delhi"},
    {"name" : "Tom", "age" : 17, "city" : "pune"},
    {"name" : "Nick", "age" : 60, "city" : "chennai"},
]

for i in range(len(data)):
    if data[i]["age"] > 40:
        print(data[i]["name"], data[i]["age"], data[i]["city"])




