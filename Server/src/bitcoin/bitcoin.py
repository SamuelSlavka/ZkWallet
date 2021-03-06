''' Bitcoin data handling '''

import json, logging
from .jsonRPC import *
from .btc_zok_utils import *
from ..constants import *

def get_zk_input(chainId, start, end):
    try:
        start = str(start)
        end = str(end)
        zkInput = create_zok_input(chainId, start, end)
        return json.dumps(zkInput)
    except Exception as err:
        logging.error("Error '{0}' occurred.".format(err))
        return {'error':'Error while fetching transaction'}
