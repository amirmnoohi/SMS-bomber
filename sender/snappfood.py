import requests


class Snappfood:
    @staticmethod
    def send(phone_number):
        try:
            payload = {"cellphone": "0" + phone_number,
                       "captcha": "111"}
            resp = requests.post(url="https://snappfood.ir/auth/login_with_no_pass", data=payload).json()
            output = {'code': 200, 'message': 'SMS Sent'}
            if resp['result'] is True:
                if resp["isRegistered"] is True:
                    if resp["hasPassword"] is True:
                        # Forget
                        payload = {"username_or_email": "0" + phone_number,
                                   "type": "sms",
                                   "captcha": "111"}
                        resp = requests.post("https://snappfood.ir/customer/password/forgot", data=payload).json()
                    else:
                        return output
                else:
                    return output
            else:
                output['code'] = 500
                output['message'] = 'Failed to send SMS'
            return output
        except Exception as e:
            output = {'code': 500, 'message': 'Failed to send SMS', 'response': resp, 'exception': e}
            return output
