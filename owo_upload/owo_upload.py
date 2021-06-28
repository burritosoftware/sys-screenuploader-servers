#!/usr/bin/env python3

import os
from tempfile import TemporaryDirectory

import click
from bottle import route, run, request, BaseRequest, HTTPError, default_app

import requests
import json
import pyperclip

BaseRequest.MEMFILE_MAX = 1024 * 1024 * 100

global TOKEN, BASE

@route('/', method='POST')
def index():

    if 'filename' not in request.params:
        raise HTTPError(400, 'filename param is missing')
    filename = os.path.basename(request.params['filename'])

    print("Recieving " + os.path.splitext(filename)[1] + " file!")

    owo = 'https://api.awau.moe/upload/pomf/associated?key=' + TOKEN

    with TemporaryDirectory() as d:
        fpath = os.path.join(d, filename)
        with open(fpath, 'wb') as f:
            body = request.body
            while True:
                chunk = body.read(0xFFFF)
                if not chunk:
                    break
                f.write(chunk)
        result = requests.post(owo, files={'files[]': open(file=fpath, mode='rb')})
        response = json.loads(result.text).get("files")[0].get("url")
        
        url = BASE + "/" + response
        
        print("Uploaded to " + url)
        pyperclip.copy(url)

    return 'OK'


@click.command()
@click.option('--host', '-h', envvar='HOST', default='0.0.0.0', type=str)
@click.option('--port', '-p', envvar='PORT', default=8080, type=int)
@click.option('--token', '-t', envvar='TOKEN', type=str)
@click.option('--base', '-b', envvar='BASE', default='https://awau.moe', type=str)
def start(host, port, token, base):
    global TOKEN, BASE
    TOKEN = token
    BASE = base
    run(host=host, port=port)


if __name__ == '__main__':
    start()

app = default_app()
