import requests
import json

sess = requests.Session()
filename = "access.log"

with open(filename, "r") as rf:
	contents = rf.read()

splitted = contents.split("\n")
ip_addresses = [item.split(" ")[0] for item in splitted]

ip_addresses = list(set(ip_addresses))

print("IP addresses:")
for item in ip_addresses:
	resp = sess.post("http://ip-api.com/json/{}".format(item))
	resp = json.loads(resp.text)
	print("{} - {}, {}".format(item, resp['city'].encode("utf-8"), resp['country'].encode('utf-8')))
	
