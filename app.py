import os,json,httpagentparser
from flask import Flask,render_template,request

app = Flask(__name__)

#REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:5000')
#redis = redis.from_url(REDIS_URL)
global mac_count
global win_count
global file
@app.route('/')
def index():
    #visitors = redis.get('visitors')
    #os = redis.get('osdata') ||

    #num = 0 if visitors is None else int(visitors)
    #num += 1
    try:
        with open('data.txt', 'r+') as f:
            file = f
            process()
    except IOError:
        initFile()

    num = 30

    #redis.set('visitors', num)
    return render_template('index.html', number=num)
def process():
    print ('reading file')
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
    print 'Oh dear.'
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  


