import os
import sys
import json
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

def load_config(args):
    with open('config.json') as f:
            data = json.load(f)
    if args == 'database':
        return data['database']
    elif args == 'token':
        return data['token']
    else:
        raise RuntimeError('올바른 입력값이 지정되지 않았습니다.')