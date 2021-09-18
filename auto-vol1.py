import os
import sys

tools_dir = "tools/"
result_dir = "result/"
vol_dir = tools_dir + "volatility/vol.py"
imageinfo_dir = "imageinfo.py"

def show_tools():
    tools_list=os.listdir(tools_dir)
    print('共发现{}种工具：'.format(str(len(tools_list))))
    for i in tools_list:
        print(i)
    return tools_list

def foremost(target):
    print("\n\033[34m[+] Running foremost!\033[0m\n")
    os.system('foremost {} -T -o ./result/foremost_out'.format(target))
    print("\n\033[32m[-] 成功分离文件!\033[0m\n")

def imageinfo(target):
    print("\n\033[34m[+] 获取镜像系统信息!\033[0m\n")
    os.system('python2 {} -f {} imageinfo >./result/imageinfo.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 获取成功!\033[0m\n")
    os.system('python3 {}'.format(imageinfo_dir))

def main(target):

    print("\033[33m[+] 正在分离镜像文件\033[0m")

    foremost(target)
    input("\033[33m[+] 是否继续?\033[0m\n")

    print("\033[33m[+] 正在获取镜像系统信息\033[0m")

    imageinfo(target)
    input("\033[33m[+] 获取成功,Suggested Profile(s)后为可能的系统信息,接下来请使用auto-vol2脚本\033[0m\n")

main(sys.argv[1])
