import os
import redis
from flask import Flask, request

redis_host = os.environ.get('REDIS_1_PORT_6379_TCP_ADDR')
redis_port = os.environ.get('REDIS_1_PORT_6379_TCP_PORT')

app = Flask(__name__)
r = redis.StrictRedis(host=redis_host, port=redis_port, db=0)


@app.route('/set/<name>', methods=['POST'])
def set(name):
    r.set(name, request.form.get(name))
    return 'OK'


@app.route('/get/<name>', methods=['GET'])
def get(name):
    return r.get(name)


if __name__ == "__main__":
    app.run()
