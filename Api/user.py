import requests, app, logging


class UserApi:

    def __init__(self):
        self.get_token_url = app.base_url + '/token/user'
        self.token_verity_url = app.base_url + '/token/verify'
        self.get_address_url = app.base_url + '/address'

    def get_token_api(self):
        """获取token"""
        logging.info('用户 - 获取token')
        # 请求体
        data = {'code': app.code}
        # 打印 请求参数
        logging.info('请求参数：{}'.format(data))
        # 返回响应对象
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def verify_token_api(self):
        """token验证"""
        logging.info('用户 - token验证')
        # 请求体
        data = {'token':app.headers.get('token')}
        # 打印 请求参数
        logging.info('请求参数：{}'.format(data))
        # 返回响应对象
        return requests.post(self.token_verity_url, json=data, headers=app.headers)

    def get_address_api(self):
        """用户地址信息"""
        logging.info('用户 - 用户地址信息')
        # 返回响应对象
        return requests.get(self.get_address_url, headers=app.headers)
