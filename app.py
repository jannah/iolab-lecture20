import os,json,httpagentparser
from flask import Flask,render_template,request

app = Flask(__name__)

#REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:5000')
#redis = redis.from_url(REDIS_URL)
mac_count = 0
win_count = 0
file =''
@app.route('/')
def index():
    #visitors = redis.get('visitors')
    #os = redis.get('osdata') ||

    #num = 0 if visitors is None else int(visitors)
    #num += 1
    try:
        with open('data.txt', 'r+') as f:
            global file
            file = f
            process()
    except IOError:
        initFile()

    
    s = "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9"
    os = httpagentparser.detect(s)
    print (os)
    num = 30

    #redis.set('visitors', num)
    return render_template('index.html', number=num, win_num=win_count, mac_num=mac_count, user_os=os )
def process():
    print ('reading file')
    global win_count
    global mac_count
    global file
    lines = file.readlines()
    linecount = 0
    for line in lines:
        strs = line.split('=')
        print (strs)
        if linecount == 0:
            win_count = int(float(strs[1]))
            linecount = 1
        else:
             mac_count = int(float(strs[1]))
    print(win_count)
    print(mac_count)
         
        
        
    
def initFile():
    print ('Oh dear.')
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  


