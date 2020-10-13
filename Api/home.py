import requests, app, logging


class HomeApi:
    """首页API接口方法"""

    def __init__(self):
        # 轮播图url
        self.banner_url = app.base_url + '/banner/{}'
        # 专题栏url
        self.theme_url = app.base_url + '/theme?ids=1,2,3'
        # 最近新品url
        self.recent_product_url = app.base_url + '/product/recent'

    def banner_api(self, num=1):
        """
        请求轮播图
        :param num: 轮播图页面数
        :return: 相应对象
        """
        logging.info('首页 - 轮播图')
        # 返回响应对象
        return requests.get(self.banner_url.format(num))

    def theme_api(self, ids='1,2,3'):
        """
        请求专题栏
        :param ids: 专题栏数据
        :return:
        """
        logging.info('首页 - 专题栏')
        # 请求参数
        data = {'ids': ids}
        # 打印 请求参数
        logging.info('请求参数：{}'.format(data))
        # 返回响应对象
        return requests.get(self.theme_url, params=data)

    def recent_product_api(self):
        """请求最近新品"""
        logging.info('首页 - 最近新品')
        # 返回响应对象
        return requests.get(self.recent_product_url)
