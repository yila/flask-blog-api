from app import api
import json


@api.route('/')
def main_route():
    return json.dumps({'user': 'Miguel'})
