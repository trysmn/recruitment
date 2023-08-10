from flask import Flask, Response

app = Flask(__name__)


@app.post('/feedback')
def feedback():
    return Response(status=200)
