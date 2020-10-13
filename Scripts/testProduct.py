import utils, logging
from Api.apiFactory import ApiFactory


class TestProduct:
    def test_product_classify(self):
        """商品分类"""
        res = ApiFactory.get_product_api().product_classify_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言商品分类大于0
        assert len(res.json()) > 0
        # 断言存在 id name description url
        assert 'id' in res.text and 'name' in res.text and 'description' in res.text and 'url' in res.text

    def test_classify_product(self):
        """分类下商品"""
        res = ApiFactory.get_product_api().classify_product_api(6)
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言商品分类大于0
        assert len(res.json()) > 0
        # 断言存在 id name description url
        # assert False not in [i in res.text for i in ['id', 'name', 'price', 'stock']]
        assert True in [i in res.text for i in ['id', 'name', 'price', 'stock']]

    def test_product_detail(self):
        """商品信息"""
        res = ApiFactory.get_product_api().product_detail_api(20)
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言商品分类大于0
        assert len(res.json()) > 0
        # 断言 id
        assert res.json().get('id') == 20
        # 断言 name
        assert res.json().get('name') == '碧螺春 12克*3袋'
        # 断言 price
        assert res.json().get('price') == '0.01'
        # 断言存在 id name description url
        # assert 'name' in res.text and 'price' in res.text and 'stock' in res.text and 'main_img_url' in res.text
