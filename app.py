import brainstem
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/switch', methods=['POST'])
def switch():
    id = request.json['id']
    port = request.json['port']

    usbc_switch = brainstem.stem.USBCSwitch()
    result = usbc_switch.discoverAndConnect(brainstem.link.Spec.USB, id)
    usbc_switch.mux.setChannel(port)

    return f'{result == 0}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')