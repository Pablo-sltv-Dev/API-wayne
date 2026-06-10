from src import app, limiter
from flask import jsonify
@app.route('/rta/teste')
@limiter.limit('5 per minute')
def connection_test():
    return jsonify({"menssage": True})