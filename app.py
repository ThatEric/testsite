import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack

app = Flask(__name__)

#Just a random update to test git
	
@app.route('/')
def show_home():
    return render_template('hero.html')
	
@app.route('/about/')
def show_about():
    return render_template('about.html')
	
@app.route('/resume/')
def show_resume():
    return render_template('resume.html')
	
@app.route('/misc/')
def show_misc():
    return render_template('misc.html')
	
@app.route('/contact/')
def show_contact():
    return render_template('contact.html')

@app.route('/sunburn/')
def show_sunburn():
    return render_template('sunburn.html')
	
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)