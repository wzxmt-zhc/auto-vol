import os
import sys

tools_dir = "tools/"
result_dir = "result/"
vol_dir = tools_dir + "volatility/vol.py"
imageinfo_dir = "imageinfo.py"

def exportfile(target):
    print("\n\033[34m[+] Running Exportfile!\033[0m\n")
    os.system('python2 {} -f {} --dump-dir=./'.format(vol_dir,target))
    print("\n\033[32m[-] 成功分离文件!\033[0m\n")

def main(target):
    print("\033[33m[+] 正在分离文件\033[0m")

    imageinfo(target)
    input("\033[33m[+] 分离成功,请在目录中查看文件\033[0m\n")
main(sys.argv[1])