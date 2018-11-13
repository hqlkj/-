from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
import random
class usercheck:
    def Check(self,phonenum):
        appid=1400122085
        appkey='9fbbf9cc9d1bf428a442ed15c3c9f1c9'
        ssender = SmsSingleSender(appid, appkey)
        key=""
        for  i in range(1,7):
            key+=str(random.randrange(10))
        params = [key,5]

        try:
            result = ssender.send_with_param(86, phonenum,169389, params)
        except HTTPError as e:
            print(e)
        except Exception as e:
            print(e)

        return key