from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from services import DicomNet

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/echo')
def echo():
    return render_template('echo.html')

@app.route('/find')
def find():
    return render_template('find.html')

@app.route('/api/echo', methods=['POST'])
def api_echo():
    remote_host = request.form['remote_host']
    remote_port = int(request.form['remote_port'])
    aetitle = request.form['aetitle']

    dn = DicomNet()
    dn.setAddress(remote_host)
    dn.setPort(remote_port)
    dn.setCallerAET(aetitle)
    dn.setAssociation()
    success = dn.cecho()
    print(success)
    dn.releaseAssociation()

    return {'success': success}

@app.route('/api/find', methods=['POST'])
def api_find():
    remote_host = request.form['remote_host']
    remote_port = int(request.form['remote_port'])
    query = {}
    for key, value in request.form.items():
        tag = key.split('[')[1][1:-2].split(',')
        group = tag[0][1:-1]
        element = tag[1][1:-1]
        query[(group, element)] = {'vr': 'PN', 'value': value}
    result = cfind(remote_host, remote_port, query)
    return {'result': result}

if __name__ == '__main__':
    app.run(debug=True)
