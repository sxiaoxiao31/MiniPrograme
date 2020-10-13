import requests, app, logging


class ProductApi:
    """商品接口"""

    def __init__(self):
        # 商品分类url
        self.product_classify_url = app.base_url + '/category/all'
        # 分类下商品url
        self.classify_url = app.base_url + '/product/by_category'
        # 商品信息url
        self.product_detail_url = app.base_url + '/product/{}'

    def product_classify_api(self):
        """商品分类"""
        logging.info('商品 - 商品分类')
        # 返回响应对象
        return requests.get(self.product_classify_url)

    def classify_product_api(self, id=2):
        """
        分类下商品
        :param id: 分类id
        :return:
        """
        logging.info('商品 - 分类下商品')
        # 请求参数
        data = {'id': id}
        # 打印 请求参数
        logging.info('请求参数：{}'.format(data))
        # 返回响应对象
        return requests.get(self.classify_url, params=data)

    def product_detail_api(self, num=2):
        """
        商品信息
        :param num: 商品id
        :return:
        """
        logging.info('商品 - 商品信息')
        # 返回响应对象
        return requests.get(self.product_detail_url.format(num))
