from flask import Flask, Response, request

app = Flask(__name__)


@app.post('/feedback')
def feedback():
    if request.json == {}:
        return Response(status=400)
    return Response(status=200)
