import os
import sys

from flask import Flask, request, Response

from crawler import Crawler

app = Flask(__name__)
c = Crawler()

@app.post('/category/')
def get_category():
    request_data = request.get_json()
    urls = request_data.get("links")
    print(urls)
    if urls is None:
        return Response("You must pass a valid url", status=500)
    
    output = []
    for url in urls:
        try:
            content = c.start(url)
            category = c.categorize(content)
            split_cat = category.split(";")
            formatted = [i.strip() for i in split_cat]
            output_dict = {}
            for i in formatted:
                k_v = i.split(":")
                # print(k_v)
                key = k_v[0]
                val = k_v[1].strip().strip('.')
                output_dict.update({key: None if val == "None" else val})
            #     print(item)
            output.append(output_dict)
        except Exception as err:
            print(err)
            return Response(f"An error occured: {err}", 500)
    return {
        "categories": output
    }, 200


@app.post('/summary/')
def get_summary():
    request_data = request.get_json()
    url = request_data.get("link")
    print(url)

    if url is None:
        return Response("You must pass a valid url", status=500)  
    try:
        content = c.start(url)
        summary = c.make_summary(content)
    except Exception as err:
        print(err)
        return Response(f"An error occured: {err}", 500)
    return {
        "summary": summary
    }, 200


@app.post('/rewrite/tv/')
def rewrite_tv():
    request_data = request.get_json()
    url = request_data.get("link")
    print(url)

    if url is None:
        return Response("You must pass a valid url", status=500)  
    try:
        content = c.start(url)
        response = c.tv_rewrite(content).replace('\n', '')
    except Exception as err:
        print(err)
        return Response(f"An error occured: {err}", 500)
    return {
        "response": response
    }, 200


@app.post('/rewrite/radio/')
def rewrite_radio():
    request_data = request.get_json()
    url = request_data.get("link")
    print(url)

    if url is None:
        return Response("You must pass a valid url", status=500)  
    try:
        content = c.start(url)
        response = c.radio_rewrite(content).replace('\n', '')
    except Exception as err:
        print(err)
        return Response(f"An error occured: {err}", 500)
    return {
        "response": response
    }, 200


@app.post('/rewrite/online/')
def rewrite_online():
    request_data = request.get_json()
    url = request_data.get("link")
    print(url)

    if url is None:
        return Response("You must pass a valid url", status=500)  
    try:
        content = c.start(url)
        response = c.online_rewrite(content).replace('\n', '')
    except Exception as err:
        print(err)
        return Response(f"An error occured: {err}", 500)
    return {
        "response": response
    }, 200




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
