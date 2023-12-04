import hashlib
filename = "malwar.exe"
api_key="e63aec06020b6dfe77fb35fd6bd77c83aa6bdab720b43476639e70d04516b312"
with open(filename, "rb") as f:
    bytes = f.read()
    readable_hash = hashlib.sha256(bytes).hexdigest()
import requests
url='https://www.virustotal.com/vtapi/v2/file/report'
params={'apikey':api_key,'resource':readable_hash}
response=requests.get(url, params=params)
for key in response.json():
    if key=="positives":
        if response.json()[key]==0:
            print("Fisierul este sigur")
        else:
            print("Fisierul nu este sigur")