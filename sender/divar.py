import requests


class Divar:
    @staticmethod
    def send(phone_number):
        payload = {"phone": "0" + phone_number}
        resp = requests.post(url="https://api.divar.ir/v5/auth/authenticate", json=payload)
        output = {'code': 200, 'message': 'SMS Sent'}
        if resp.status_code == 200:
            return output
        output['code'] = 500
        output['message'] = 'Failed to send SMS'
        return output
