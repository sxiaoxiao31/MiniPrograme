from Api.apiFactory import ApiFactory
import os

# 请求轮播图
# print('轮播图：\n{}'.format(ApiFactory.get_home_api().banner_api().json()))
# 请求主题
# print('主题：\n{}'.format(ApiFactory.get_home_api().theme_api().json()))
# 请求最近新品
# print('最近新品：\n{}'.format(ApiFactory.get_home_api().recent_product_api().json()))

# 商品分类
# print('商品分类：\n{}'.format(ApiFactory.get_product_api().product_classify_api().json()))
# 分类下商品
# print('分类下商品：\n{}'.format(ApiFactory.get_product_api().classify_product_api(6).json()))
# 商品信息
# print('商品信息：\n{}'.format(ApiFactory.get_product_api().product_detail_api(20).json()))

# 获取token
# print('获取token：\n{}'.format(ApiFactory.get_user_api().get_token_api().json()))

# 获取用户订单列表
# print('订单列表：\n{}'.format(ApiFactory.get_order_api().order_list_api().json()))
# 创建订单
# print('创建订单：\n{}'.format(ApiFactory.get_order_api().create_order_api(17,1).json()))
# 查看订单
# print('查看订单：\n{}'.format(ApiFactory.get_order_api().query_order_api(119).json()))


current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
parent_dir = os.path.dirname(current_dir)
print(parent_dir)
