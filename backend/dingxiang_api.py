from flask import Flask
from flask import Response
# import dingxiang_crawler
import json
import dingxiang_middleware

app = Flask(__name__)


@app.route('/dx/brief')
def briefResponse():
    data = dingxiang_middleware.select(0)
    # data = dingxiang_crawler.getBriefInfoNew()
    res = Response(data, status=200, mimetype='text/plain')
    return res


@app.route('/dx/tips')
def tipsResponse():
    # data = dingxiang_crawler.getBriefTips()
    # js = json.dumps(data, ensure_ascii=False)
    # print(js)
    js = dingxiang_middleware.select(1)
    res = Response(js, status=200, mimetype='application/json')
    return res


@app.route('/dx/detail')
def detailResponse():
    # data = dingxiang_crawler.getComplexDetail()
    # js = json.dumps(data, ensure_ascii=False)
    # print(js)
    js = dingxiang_middleware.select(2)
    res = Response(js, status=200, mimetype='application/json')
    return res


@app.route('/dx/info')
def infoResponse():
    # data = dingxiang_crawler.getComplexTimeLine()
    # js = json.dumps(data, ensure_ascii=False)
    # print(js)
    js = dingxiang_middleware.select(3)
    res = Response(js, status=200, mimetype='application/json')
    return res


if __name__ == "__main__":
    # app.run(host="0.0.0.0",debug=True,port=2019)
    app.run(debug=True, port=2019)
