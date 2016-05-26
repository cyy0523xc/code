# scrapyd


```shell
# 注意需要sudo启动，否则会报权限不足的错误
sudo scrapyd

# 生成egg
sudo python setup.py install

# 发布爬虫
curl http://localhost:6801/addversion.json -F project=turorial -F version=r1 -F egg=@dist/turorial-1.0-py2.7.egg

# 启动爬虫
curl http://localhost:6801/schedule.json -d project=turorial -d spider=baidu
```
