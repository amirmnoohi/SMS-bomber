import requests


class Tapsi:
    @staticmethod
    def send(phone_number):
        try:
            payload = {"credential": {"phoneNumber": "0" + phone_number,
                                      "role": "PASSENGER"}}
            resp = requests.post(url="https://tap33.me/api/v2/user", json=payload).json()
            output = {'code': 200, 'message': 'SMS Sent'}
            if 'result' in resp:
                if resp['result'] == "OK":
                    return output
            output['code'] = 500
            output['message'] = 'Failed to send SMS'
            return output
        except Exception as e:
            output = {'code': 500, 'message': 'Failed to send SMS', 'response': resp, 'exception': e}
            return output