import utils, logging
from Api.apiFactory import ApiFactory


class TestOrder:
    def test_order_list(self):
        """用户订单列表"""
        # 响应对象
        res = ApiFactory.get_order_api().order_list_api()
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言当前页面
        assert res.json().get('current_page') == 1
        # 断言 订单数量大于0
        assert len(res.json().get('data')) > 0
        # 断言关键字
        assert False not in [i in res.text for i in ['id', 'order_no', 'total_price', 'total_count']]

    def test_create_order(self):
        """创建订单"""
        # 购买商品id 、数量
        product_id = 15
        count = 2
        # 响应对象
        res = ApiFactory.get_order_api().create_order_api(product_id, count)
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言 order_no和order_id 存在
        assert len(res.json().get('order_no')) > 0 and len(res.json().get('order_id')) > 0
        # 断言订单状态
        assert res.json().get('pass') is True

    def test_view_order(self):
        """查看订单"""
        # 订单id
        order_id = 120
        # 收件人姓名
        exp_name = '小乔'
        # 收件人手机号
        exp_mobile = '13588888888'
        # 响应对象
        res = ApiFactory.get_order_api().query_order_api(order_id)
        # 打印 请求参数、请求地址、请求响应数据
        logging.info('请求地址：{}'.format(res.url))
        logging.info('请求响应：{}'.format(res.json()))
        # 断言响应状态码
        utils.common_assert(res)
        # 断言订单编号
        assert res.json().get('id') == order_id
        # 断言地址 用户名 和 手机号
        assert res.json().get('snap_address').get('name') == exp_name
        assert res.json().get('snap_address').get('mobile') == exp_mobile
        # 断言关键字
        assert False not in [i in res.text for i in
                             ['order_no', 'total_price', 'snap_img', 'snap_name', 'total_count']]
