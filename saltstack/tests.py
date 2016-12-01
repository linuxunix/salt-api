# #coding=utf8
# import salt.client # 导入模块
# client = salt.client.LocalClient() # 初始化 saltstack
# def overview(request): # 获取所有机器信息
# target = request.GET.get("target",'*') # 获取请求中的
# try:
# grains = client.cmd(target, 'grains.items') #
# except:
# grains = {} # 如果出错 ,  将 grains  设置为空
# return grains # 返回 target
# def execute(**kwargs): # 执行命令函数
# return client.cmd_async(**kwargs) # 直接将命令发送到后端
# def get_state(target): # 获取所有可用的状态
# try:
# states = client.cmd(target,'state.show_top') #
# except:
# states = {} # 如果失败将状态设置为空
# return states # 返回状态
# if __name__ =="__main__": # 如果执行执行 ,  调用下面的命令
# print get_state('minion1')