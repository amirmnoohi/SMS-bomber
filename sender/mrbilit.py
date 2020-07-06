import requests


class Mrbilit:
    @staticmethod
    def send(phone_number):
        resp = requests.get(
            url="https://auth.atighgasht.com/AuthService/api/Login/Exists?mobileOrEmail=" + "0" + phone_number + "&source=2&sendTokenIfNot=true").json()
        output = {'code': 200, 'message': 'SMS Sent'}
        if resp is False:
            return output
        else:
            resp = requests.get(
                url="https://auth.atighgasht.com/AuthService/api/Token/send?mobile=" + "0" + phone_number ).json()
            if resp is True:
                return output
        output['code'] = 500
        output['message'] = 'Failed to send SMS'
        return output
