# import json
#
# with open ("sensors_current.json", "r") as f:
#     text = f.read()
#
# print(text)
#
# import json
#
# with open ("sensors_current.json", "r") as f:
#     text = f.read()
#
# parsed = json.loads(text) ##zamienia tekst na strukture danych w pythonie
# print (parsed)


# import json
# with open ("sensors_current.json", "r") as f:
#     text = f.read()
# parsed = json.loads(text)
# print (type(text))
# print (type(parsed))

import json
with open ("sensors_current.json", "r") as f:
    text = f.read()
parsed = json.loads(text)
# print (parsed[0])
# print (parsed[0]["name"])
# print (parsed[0]["address"]["locality"])
# print (parsed[0]["id"])

for sensor in parsed:
    sensor_id = sensor["id"]
    sensor_name = sensor["name"]
    print(sensor_name)


