import requests, app, logging


class OrderApi:
    def __init__(self):
        # 获取用户订单列表url
        self.order_list_url = app.base_url + '/order/by_user'
        # 创建订单url
        self.create_order_url = app.base_url + '/order'
        # 查看订单url
        self.query_order_url = app.base_url + '/order/{}'

    def order_list_api(self, page=1):
        """获取用户订单列表"""
        logging.info('订单 - 订单列表')
        # 请求参数
        data = {'page': page}
        # 打印请求参数
        logging.info('请求参数：{}'.format(data))
        # 返回响应对象
        return requests.get(self.order_list_url, headers=app.headers, params=data)

    def create_order_api(self, product_id=8, count=1):
        """创建订单"""
        logging.info('订单 - 创建订单')
        # 请求参数
        data = {'products': [{'product_id': product_id, 'count': count}]}
        # 打印请求参数
        logging.info('请求参数：{}'.format(data))
        # 返回响应对象
        return requests.post(self.create_order_url, headers=app.headers, json=data)

    def query_order_api(self, order_id=50):
        """查看订单"""
        logging.info('订单 - 查看订单')
        # 返回响应对象
        return requests.get(self.query_order_url.format(order_id), headers=app.headers)
