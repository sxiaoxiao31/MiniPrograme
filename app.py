import logging.handlers, os


def log_conf():
    """初始化日志配置"""
    # 日志文件位置
    current_dir = os.path.abspath(os.path.dirname(__file__))
    logPath = current_dir + os.sep + 'Log/mini.Log'
    # 日志器
    logger = logging.getLogger()
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 处理器 -控制台
    sh = logging.StreamHandler()
    # 处理器 -文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename=logPath,
                                                     when='midnight', interval=1,
                                                     backupCount=7, encoding='utf-8')
    # 格式化字符串
    f = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    # 格式化器
    formatter = logging.Formatter(f)
    # 处理器添加格式化器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)
    # 日志器添加处理器
    logger.addHandler(sh)
    logger.addHandler(trfh)


# 请求通用接口地址
base_url = 'http://e.cn/api/v1'
# 微信code
code = '0937Y40w3HtD7V2Dgk0w334Awh17Y40b'
# 请求头
headers = {'Content-Type': 'application/json',
           'token': '6ef66dfc41b4041e7bb5318126f45b49'}

if __name__ == '__main__':
    log_conf()
    logging.info('打印输出')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
