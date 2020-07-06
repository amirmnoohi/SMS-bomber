import requests


class Divar:
    @staticmethod
    def send(phone_number):
        output = {'code': 200, 'message': 'SMS Sent'}
        try:
            payload = {"phone": "0" + phone_number}
            resp = requests.post(url="https://api.divar.ir/v5/auth/authenticate", json=payload)
            if resp.status_code == 200:
                return output
            output['code'] = 500
            output['message'] = 'Failed to send SMS'
            return output
        except Exception as e:
            output['code'] = 500
            output['message'] = 'Failed to send SMS'
            output['response'] = resp
            output['exception'] = e
            return output
