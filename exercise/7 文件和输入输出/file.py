# 1

import datetime
now = datetime.datetime.now()
with open('time.txt','w') as f:
    f.write(str(now))

# 2
with open('time.txt','w') as f:
    text_4 = f.read(4)
    print(text_4)

