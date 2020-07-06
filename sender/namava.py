import requests


class Namava:
    @staticmethod
    def send(phone_number):
        try:
            payload = {"UserName": "+98" + phone_number}
            resp1 = requests.post(url="https://www.namava.ir/api/v1.0/accounts/reset-passwords/by-phone/request",
                                  json=payload)
            resp2 = requests.post(url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
                                  json=payload)
            output = {'code': 200, 'message': 'SMS Sent'}
            if resp1.status_code == 200 or resp2.status_code == 200:
                return output
            output['code'] = 500
            output['message'] = 'Failed to send SMS'
            output['response'] = {resp1.json(), resp2.json()}
            return output
        except Exception as e:
            output = {'code': 500, 'message': 'Failed to send SMS', 'response': {resp1.json(), resp2.json()}, 'exception': e}
            return output
