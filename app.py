from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/switch', methods=['POST'])
def switch():
    port = request.json['port']
    #TODO add port switch with accroname
    return req_data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
