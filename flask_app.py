import sys, os
sys.path.append('..')
from flask import render_template, Flask, redirect
from config import config_dict

conf_dict = config_dict()

config_path = 'config.py'
app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile(config_path)

@app.route('/', methods=['GET'])
def main_reroute():
    return redirect('index.html')

@app.route('/index.html', methods=['GET'])
def index_html():
    return render_template('index.html', flask=conf_dict['say_me'])

def main():
    HOST = os.getenv('SERVER_HOST', '0.0.0.0')
    PORT = int(conf_dict['server_port'])
    THREADED = app.config['THREADED']
    PROCESSES = app.config['PROCESSES']
    FLASK_DEBUG = app.config['FLASK_DEBUG']
    if app.config['USE_SSL']:
        app.run(debug=FLASK_DEBUG, host=HOST, port=PORT,
                threaded=THREADED,
                processes=PROCESSES,
                ssl_context=('server.crt', 'server.key'))
    else:
        app.run(debug=FLASK_DEBUG,
                host=HOST,
                port=PORT,
                threaded=THREADED,
                processes=PROCESSES)


if '__main__' == __name__:
    main()
