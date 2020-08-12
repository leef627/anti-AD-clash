import requests
import os
try:
    os.remove('anti-ad.yaml')
except Exception as e:
    print(e)
url = 'https://anti-ad.net/surge.txt' 
r = requests.get(url)
with open("anti-ad.yaml",'w',newline='\n') as f:
    f.write('payload:\n')
    for line in r.text.split('\n'):
        try:
            if(line[0]=='D'):
                f.write('  - '+line+'\n')
            else:
                f.write(line+'\n')
        except Exception as e:
            print(e)
        
