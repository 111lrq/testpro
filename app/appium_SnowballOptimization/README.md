雪球 
实现：数据步骤驱动+截图+allure报告+录屏 
xueqiuframework的基础之上 
实现数据及步骤的驱动 
优化： 
1.基于PO的框架设计及yaml，步骤驱动（在basepage中解析数据） 
2.截图（保存在images下） 
3.生成allure报告 
4.实现录屏(conftest,fixture) 

自动化步骤： 
1.进入main页面 
2.点击行情进入行情页 
3.不直接操作点击搜索框，将其处理为类似弹窗的情况，黑名单中点击操作 
4.输入对应数据搜索 
5.点击确认对应的内容 
6.判断是否已添加，为已添加则操作取消 
7.点击加自选，变为已添加状态 
8.断言是否是已添加状态 


操作步骤： 
terminal: 
cd到当前目录下    
pytest test_search.py -s -q --alluredir=../results/ 
allure serve ../results/ 