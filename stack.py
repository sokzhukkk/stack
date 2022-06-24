import requests

from datetime import date, timedelta
from pprint import pprint

def stack_py():
    teg = 'python'
    today = date.today()
    yesterday = today - timedelta(days=1)
    host = 'https://api.stackexchange.com/'
    params = {'fromdate': yesterday, 'todate' : today, 'tagged':teg, 'site':'stackoverflow'}
    resp = requests.get(f'{host}/2.3/questions', params = params)
    pprint(resp.json())


stack_py()
