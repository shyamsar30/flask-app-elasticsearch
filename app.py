from flask import Flask, request, render_template
from elasticsearch import Elasticsearch

from config import Config
from helpers import get_elastic_query

es = Elasticsearch(
        Config.ELASTICSEARCH_HOST_NAME,
        ssl_assert_fingerprint=Config.SSL_ASSERT_FINGERPRINT,
        basic_auth=(Config.USERNAME, Config.PASSWORD)
    )

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    generated_query = get_elastic_query(request.args.get('q'))
    res = es.search(index=Config.ELASTIC_INDEX_NAME, query=generated_query, size=Config.DEFAULT_FETCH_SIZE)

    lis = []

    for hit in res['hits']['hits']:
        lis.append(hit["_source"])
    print(request.args.get('q'))
    a = {'data': lis, 'i': str(request.args.get('q'))}
    print(a['i'])
    return render_template('index.html', a=a)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)