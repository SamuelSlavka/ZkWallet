from flask import Flask
from .ethereum import *
from .bitcoin import *
from .constants import *

# Initialize flask app
app = Flask(__name__)
app.debug = True

web3 = ethereum.init_eth_with_pk(PRIVATE_KEY)

@app.route('/')
@app.route('/api/')
def home():
    if web3.isConnected():
        return 'Hello there!'
    return 'Connection error'        


@app.route('/last/')
def lastTransaction():
    """ Returns last transaction on current blockchain """
    return ethereum.get_last_transaction(web3), 200


@app.route('/eth/')
def createEthProof():
    """ Creates proof for headers """
    return ethereum.create_proof(2), 200

@app.route('/btc/')
def createBtcProof():
    """ Creates proof for headers """
    return bitcoin.create_proof(2), 200

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')