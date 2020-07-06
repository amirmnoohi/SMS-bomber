import requests


class Zarinpal:
    @staticmethod
    def send(phone_number):
        payload = {"username": "0" + phone_number, "channel": "sms"}
        resp = requests.post(url="https://my.zarinpal.com/rest/v3/oauth/initializeLogin.json", json=payload)
        output = {'code': 200, 'message': 'SMS Sent'}
        if resp.status_code == 200:
            return output
        else:
            payload = {"cell_number": "0" + phone_number, "first_name": "جهت", "last_name": "تست"}
            resp = requests.post(url="https://next.zarinpal.com/api/oauth/register", json=payload)
            if resp.status_code == 200:
                return output
        output['code'] = 500
        output['message'] = 'Failed to send SMS'
        return output
