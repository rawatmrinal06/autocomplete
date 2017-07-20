import json
import logging

from flask import Flask,app,request, render_template,Response

from appdb import get_title_by_partial_keyword
app = Flask(__name__, static_url_path='/static')


@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    titles = get_title_by_partial_keyword(keyword.strip())
    return json.dumps({'status': 'ok', 'results': titles})


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

