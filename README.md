# TestCode
APITestPractice

文件：
1.ApiTestFromwork是基于本地在虚拟机使用docker构建的jnfluxdb+Grafana的服务进行的api自动化测试，代码内部实现了：
  - 封装requests的post方法 
  - 构造方法，文件读取，测试用例，动态参数的分离
 
用途，可以用于公司进行自动化测试搭建框架

2.lagouAPITest是网易云平台自动化测试视频API自动化测试框架部分源码，以拉勾网为实例，剖析如何进行API自动化测试，内部实现了：
  - 目录优化
  - 数据分离
  - 获取json文件内容
  - 关联excel与json的请求参数
  - 对POST请求的二次封装
  - 编写测试用例
  - 增加断言
  - 重构代码
  - 当请求参数是动态参数的处理
  - 参数关联业务处理
  - 关联参数写入文件
  - 检测headers函数
  - 测试结果写入文件
  - 统计测试成功率
  - 新增发送邮件功能
  - 针对平台加密数据处理

3.tryApiTest是自我练习，主要是对UI自动化和API自动化测试的基本方法练习，其中包括：
  - apiRequestTests 
  
    - apiTests            数据驱动练习
    - frist_PO-master     基于pytest框架的移动端自动化测试
    - tryApiTest          基于unittest和webdriver做百度链接跳转的测试
    - TryPythonApiTest    pyhon基本方法的练习
    
  - dataDriver            数据驱动的详细练习
  
    - dirverDDTTest       ddt数据驱动
    - driverConfigTest    配置文件驱动
    - driverCSVTest       csv文件驱动
    - driverExeclTest     execl文件驱动
    - driverLog           log文件驱动
    - driverMysqlTest     Mysql驱动
    - driverXmlTest       xml文件驱动
    
  - requestsPractice      requests库的基本方法使用（包括requests分析，session、cookie获取，文件上传和下载）
  - TestUnittestWebdriver 基于unittest和webdriver编写UI自动化测试实现了，代码分离和HTM报告的输出
    
    
