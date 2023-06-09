from flask import Flask, abort, request, render_template
from elasticsearch import Elasticsearch

from config import Config
from helpers import gen_query_for_auto_complete, get_elastic_query

from flask_cors import CORS
from flask_compress import Compress

es = Elasticsearch(
        Config.ELASTICSEARCH_HOST_NAME,
        ssl_assert_fingerprint=Config.SSL_ASSERT_FINGERPRINT,
        basic_auth=(Config.USERNAME, Config.PASSWORD)
    )

app = Flask(__name__)

CORS(app)
Compress(app)

@app.route('/search', methods=['GET'])
def search():
    generated_query = get_elastic_query(request.args.get('q'))
    skip_results = request.args.get('from')

    if not skip_results:
        skip_results = 0
    else:
        try:
            skip_results = int(skip_results)
        except:
            abort(400, "From should be Integer.")


    skip_results = skip_results * Config.DEFAULT_FETCH_SIZE

    if skip_results >= 10000:
        abort(404, "Can't query above 10000 hits.")

    res = es.search(
        index=Config.ELASTIC_INDEX_NAME,
        query=generated_query,
        size=Config.DEFAULT_FETCH_SIZE,
        from_=skip_results,
        track_total_hits=True
    )

    lis = []
    response_to_template = {}
    response_to_template['i'] = str(request.args.get('q'))

    for hit in res['hits']['hits']:
        lis.append(hit["_source"])

    response_to_template['data'] = lis

    response_to_template['time_taken'] = res['took']
    response_to_template['total_records'] = res['hits']['total']['value']

    return render_template('index.html', a=response_to_template)


@app.route('/autocomplete') 
def auto_comp():
    s = request.args.get('s')
    dic = {}
    for field in Config.AUTO_COMPLETE_FIELDS:
        auto_complete_query = gen_query_for_auto_complete(field, request.args.get('s'))
        res = es.search(
            index=Config.ELASTIC_INDEX_NAME,
            query=auto_complete_query,
            size=10,
            source_includes=[field]
        )
        for hit in res['hits']['hits'] :
            dic[hit["_source"][field]] = ""
    
    return {"data": list(dic.keys())}


@app.route('/get-response', methods=['GET'])
def get_response():
    generated_query = get_elastic_query(request.args.get('q'))
    skip_results = request.args.get('from')

    if not skip_results:
        skip_results = 0
    else:
        try:
            skip_results = int(skip_results)
        except:
            abort(400, "From should be Integer.")


    skip_results = skip_results * Config.DEFAULT_FETCH_SIZE

    if skip_results >= 10000:
        abort(404, "Can't query above 10000 hits.")

    res = es.search(
        index=Config.ELASTIC_INDEX_NAME,
        query=generated_query,
        size=Config.DEFAULT_FETCH_SIZE,
        from_=skip_results,
        track_total_hits=True
    )

    lis = []
    response_to_template = {}
    response_to_template['i'] = str(request.args.get('q'))

    for hit in res['hits']['hits']:
        lis.append(hit["_source"])

    response_to_template['data'] = lis

    response_to_template['time_taken'] = res['took']
    response_to_template['total_records'] = res['hits']['total']['value']

    return response_to_template

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.1.9', port=9876, debug=True)