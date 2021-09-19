基于volatility的半自动化取证工具，目前并不完善，欢迎大家测试

##
所需环境:

* python2
* python3
* foremost



```bash
sudo pip install construct==2.5.5-reupload

pip install distorm3

pip install pycryptodome

pip3 install pycryptodome
```

##
使用方法:

1.配置好所需环境

2.用auto-vol1.py脚本识别出系统信息

用法:python3 + auto-vol1.py +镜像名称

示例:python3 auto-vol1.py 1.raw

3.用auto-vol2.py脚本进行auto取证

用法:python3 + auto-vol2.py +镜像名称 + --profile=镜像系统

示例:python3 auto-vol1.py 1.raw --profile=Win7SP1x64

4.若要分离扫描出的文件，请用exportfile.py脚本

用法:python3 + exportfile.py +镜像名称 + --profile=镜像系统 + dumpfiles + -Q + 所在内存地址


##
实现的功能:
* foremost分离镜像内的文件
* 扫描镜像内进程
* 扫描历史cmd命令
* 扫描网络连接
* 扫描网络流量
* 扫描注册表
* 爆破用户名密码
* 爆破bitlocker密码
* 扫描镜像内txt文件
* 扫描镜像内与flag有关文件
