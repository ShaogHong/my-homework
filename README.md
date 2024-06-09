# 服务器响应日志处理
需求:将日志格式化到csv中并作简要统计和分析,且使用了ip查询api查询ip属地信息；
## 执行start_main.py
只需要提供日志文件即可，所有操作生成的文件都在所提供的日志文件同一目录下

提供了text_log.log样本日志作示范

ip属地查询api：https://qifu.baidu.com/ip/geo/v1/district?ip=	能查的信息还挺多的：

``` json
{
  "code": "Success",
  "data": {
      "continent": "亚洲",
      "country": "印度尼西亚",
      "zipcode": "",
      "timezone": "UTC+7",
      "accuracy": "省",
      "owner": "Institut Teknologi Del",
      "isp": "Institut Teknologi Del",
      "source": "数据挖掘",
      "areacode": "ID",
      "adcode": "",
      "asnumber": "142367",
      "lat": "2.110200",
      "lng": "99.541564",
      "radius": "",
      "prov": "北苏门答腊省",
      "city": "",
      "district": ""
  },
  "charge": false,
  "msg": "查询成功",
  "ip": "103.167.217.137",
  "coordsys": "WGS84"
  }
```


 



