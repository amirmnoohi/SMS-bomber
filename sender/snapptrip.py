import requests


class Snapptrip:
    @staticmethod
    def send(phone_number):
        # Register
        url = "https://www.snapptrip.com/register"
        payload = {"country_code": "+98",
                   "country_id": "860",
                   "lang": "fa",
                   "mobile_phone": "0" + phone_number,
                   "password": "11041104"}
        resp = requests.post(url=url, json=payload)
        output = {'code': 200, 'message': 'SMS Sent'}
        if resp.json()["status_code"] == -1:
            # Forget password
            resp = requests.get("https://www.snapptrip.com/auth/code-request?username=" + phone_number)
            if resp.json()["status_code"] == 200:
                output['message'] = 'SMS Sent'
            else:
                output['code'] = 500
                output['message'] = 'Failed to send SMS'
        return output
