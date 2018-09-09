import csv
import json
import requests
#
# data = """[
#     {
#         "_id": {
#             "$oid": "5b941a1a2f4125b98b706d99"
#         },
#         "Timestamp": 153638395,
#         "Category": "Work",
#         "Activity": "Atom",
#         "Keystrokes": 14,
#         "Gaze": 2,
#         "Emotion": 6,
#         "Eyes": "False"
#     },
#     {
#         "_id": {
#             "$oid": "5b94121a2f4125b98b706d99"
#         },
#         "Timestamp": 154638395,
#         "Category": "Entertainment",
#         "Activity": "Google Chrome",
#         "Keystrokes": 5,
#         "Gaze": 0,
#         "Emotion": 1,
#         "Eyes": "True"
#     }
# ]"""

url = 'https://e5690c0c.ngrok.io/all-data'
r = requests.get(url)
data = r.json()

# Write CSV Header, If you dont need that, remove this line
header = ["Timestamp", "Category", "Activity", "Keystrokes", "Gaze", "Emotion", "Eyes"]

with open('data/test.csv', 'w', newline='') as csvfile:

    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(header)
    for i in data:
        spamwriter.writerow(i[h] for h in header)
