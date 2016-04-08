#!/usr/bin/env python3


from flask import Flask, jsonify
from git import Repo, NoSuchPathError
from os import environ

import settings


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    response = {'head': ''}
    code_dir = settings.QSEE_CODE_DIR
    response['code_dir'] = code_dir
    try:
        repo = Repo(code_dir)
        response['head'] = repo.head.ref.name
        response['status'] = 'success'
    except NoSuchPathError as e:
        response['messages'] = 'no such path '
        response['status'] = 'failed'
    return jsonify(response)

if __name__ == '__main__':
        if settings.DEBUG:
            app.run(debug=True)
        else:
            app.run(debug=False, host='0.0.0.0')

