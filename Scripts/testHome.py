import utils, logging
from Api.apiFactory import ApiFactory


class TestHomeApi:
    def test_banner_api(self):
        """轮播图"""
        # 请求返回数据
        res = ApiFactory.get_home_api().banner_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言 id 和 name
        assert res.json().get('id') == 1 and res.json().get('name') == '首页置顶'
        # 断言 items列表长度大于0
        assert len(res.json().get('items')) > 0

    def test_theme_api(self):
        """专题栏"""
        # 返回请求数据
        res = ApiFactory.get_home_api().theme_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言 id存在
        assert 'id":1' in res.text and 'id":2' in res.text and 'id":3' in res.text
        # 断言存在 name,description,topic_img,head_img
        ls = ['name', 'description', 'topic_img', 'head_img']
        assert False not in [i in res.text for i in ls]

    def test_recent_product_api(self):
        """最近新品"""
        # 返回请求数据
        res = ApiFactory.get_home_api().recent_product_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        assert res.status_code == 200
        utils.common_assert(res)
        # 断言新品数量大于0
        assert len(res.json()) > 0
        # 断言关键字段
        assert 'id' in res.text and 'name' in res.text and 'price' in res.text