from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if(request.method == 'POST'):
        print(request.json)
        return request.json, 200
    if(request.method == 'GET'):
        print(request.query_string.decode())
        print(request.json)
        return request.query_string.decode(), 200
if __name__ == '__main__':
    app.run()