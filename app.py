import os,json,redis,httpagentparser
from flask import Flask,render_template,request

app = Flask(__name__)

#REDIS_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:5000')
#redis = redis.from_url(REDIS_URL)


@app.route('/')
def index():
    #visitors = redis.get('visitors')
    #os = redis.get('osdata') ||

    #num = 0 if visitors is None else int(visitors)
    #num += 1

    num = 30

    #redis.set('visitors', num)
    return render_template('index.html', number=num)

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)  


