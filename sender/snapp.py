import requests


class Snapp:
    @staticmethod
    def send(phone_number):
        payload = {"cellphone": "0" + phone_number,
                   "g-recaptcha-response": None}
        resp = requests.post(url="https://web-api.snapp.ir/api/v1/auth/otp", json=payload).json()
        output = {'code': 200, 'message': 'SMS Sent'}
        if 'status' in resp:
            if resp['status'] == "OK":
                return output
        output['code'] = 500
        output['message'] = 'Failed to send SMS'
        return output
