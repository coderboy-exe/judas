import os
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
    split_cat = category.split(";")
    formatted = [i.strip() for i in split_cat]
    output = []
    output_dict = {}
    for i in formatted:
        k_v = i.split(":")
        # print(k_v)
        key = k_v[0]
        val = k_v[1].strip()
        output_dict.update({key: val})
    #     print(item)
    return {
        "categories": output_dict
    }, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
