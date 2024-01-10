# QB Crawler

A simple crawler that uses crawls news articles and analyzes their content

## Setup

1. Navigate into the `judas` directory.
2. Create a virtual environment named `my-env`:

```python
python3 -m venv my-env
```
3. Activate your virtual environment `my-env`:

```python
python3 my-env/bin/activate
```
4. Install dependencies:

```python
pip install -r requirements.txt
```

5. Paste your OpenAI API key in the `.env.example` file and rename the file to `.env`.

```env
OPENAI_API_KEY=<YOUR_API_KEY>
```


## Usage

1. The keywords file is in the `data` folder. You can add as many more context files for GPT to index and use. (N.B: This will cost more money as the usage is calculated by number of tokens/characters).
2. To run the crawler, run the `index.py` file with the URL to be crawled/categorized as the second command line argument. For example:

```python
python3 index.py <url_to_be_crawled>
```

3. Alternatively, you can modify the `index.py` file and crawl the URL directly by replacing this line:

```python
url = sys.argv[1]
```

### Running and using the API

1. Run the flask app 

```python
python3 app.py
```
The Flask server will start running on port 5000.


### -- These Instructions are outdated. The README will be updated soon --



2. Send a post request to `localhost:5000/category/`

```json
{
    "link": "<str:article_url>"
}
```

A successful request should return a `200` status code with the following json

```json
{
    "category": "<str:news_category>"
}
```



