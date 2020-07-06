import requests


class Torob:
    @staticmethod
    def send(phone_number):
        resp = requests.get(url="https://api.torob.com/a/phone/send-pin/?phone_number=0"+phone_number).json()
        output = {'code': 200, 'message': 'SMS Sent'}
        if 'message' in resp:
            if resp['message'] == "pin code sent":
                return output
        output['code'] = 500
        output['message'] = 'Failed to send SMS'
        return output
