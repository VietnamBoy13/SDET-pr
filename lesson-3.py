import json
import csv

with open('in.json', 'r') as json_file:
    data = json.load(json_file)

def filter_users(json_data):
    for user in json_data:
        phone = user.get("phoneNumber"," ")
        user_agent = user.get ("userAgent", "")

        if (phone.startswith("+1") or phone.startswith("1")) and "4.0 Safari" in user_agent:
            yield user["name"], user["address"], user["email"]


with open('filtered_users.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "address", "email "])
    for name, address, email in filter_users(data):
        writer.writerow([name, address, email])

print("Команда выполненна")