import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack

app = Flask(__name__)

# @app.route('/')
# def hello():
    # return 'hello eric!'
	
@app.route('/')
def show_entries():
    return render_template('hero.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)