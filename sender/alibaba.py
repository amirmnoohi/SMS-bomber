import requests


class Alibaba:
    @staticmethod
    def send(phone_number):
        try:
            payload = {"phoneNumber": "0" + phone_number}
            resp = requests.post(url="https://ws.alibaba.ir/api/v3/account/mobile/otp", json=payload).json()
            output = {'code': 200, 'message': 'SMS Sent'}
            if 'success' in resp:
                if resp['success'] is True:
                    return output
            output['code'] = 500
            output['message'] = 'Failed to send SMS'
            return output
        except Exception as e:
            output = {'code': 500, 'message': 'Failed to send SMS', 'response': resp, 'exception': e}
            return output
