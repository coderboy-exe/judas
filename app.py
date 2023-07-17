import sys

from flask import Flask, request, Response

from crawler import Crawler

app = Flask(__name__)
c = Crawler()

@app.post('/category/')
def get_category():
    request_data = request.get_json()
    url = request_data.get("link")
    print(url)
    if url is None:
        return Response("You must pass a valid url", status=500)
    
    category = c.start(url)
    print(category)
    return {
        "category": category
    }, 200


if __name__ == "__main__":
    app.run('0.0.0.0')
