import requests


class Snappmarket:
    @staticmethod
    def send(phone_number):
        try:
            resp = requests.post(
                url="https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0" + phone_number).json()
            output = {'code': 200, 'message': 'SMS Sent'}
            if resp['status'] is True:
                return output
            output['code'] = 500
            output['message'] = 'Failed to send SMS'
            return output
        except Exception as e:
            output = {'code': 500, 'message': 'Failed to send SMS', 'response': resp, 'exception': e}
            return output