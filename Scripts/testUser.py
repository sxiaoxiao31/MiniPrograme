import utils, app, pytest, logging
from Api.apiFactory import ApiFactory


@pytest.mark.run(order=0)
class TestUser:
    def test_get_token(self):
        """获取token"""
        # 获取返回数据
        res = ApiFactory.get_user_api().get_token_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言 token 存在
        assert len(res.json().get('token')) > 0
        # 保存token
        app.headers['token'] = res.json().get('token')

    def test_token_verify(self):
        """token验证"""
        # 获取返回数据
        res = ApiFactory.get_user_api().verify_token_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言 isValid为true
        assert res.json().get('isValid') is True

    def test_user_address(self):
        """用户地址信息"""
        # 获取返回数据
        res = ApiFactory.get_user_api().get_address_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言 name
        assert res.json().get('name') == '小乔'
        # 断言 mobile
        assert res.json().get('mobile') == '13588888888'
        # 断言 地址信息
        assert False not in [i in res.text for i in ['上海市', '浦东新区', '航头镇航都路18号']]
