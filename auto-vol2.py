import os
import sys

tools_dir = "tools/"
result_dir = "result/"
vol_dir = tools_dir + "volatility/vol.py"

def show_tools():
    tools_list=os.listdir(tools_dir)
    print('共发现{}种工具：'.format(str(len(tools_list))))
    for i in tools_list:
        print(i)
    return tools_list

def pslist(target):
    print("\n\033[34m[+] Sacnning pslist!\033[0m\n")
    os.system('python2 {} -f {} pslist > ./result/pslist.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 扫描进程结束,结果保存在result目录下的pslist.txt中!\033[0m\n")


def cmdscan(target):
    print("\n\033[34m[+] Sacnning cmdusing!\033[0m\n")
    os.system('python2 {} -f {} cmdscan >./result/cmdscan.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 扫描历史cmd命令结束,结果保存在result目录下的cmdscan.txt中!\033[0m\n")

def netscan(target):
    print("\n\033[34m[+] Sacnning net connecting!\033[0m\n")
    os.system('python2 {} -f {} netscan >./result/netscan.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 扫描网络连接结束,结果保存在result目录下的netscan.txt中!\033[0m\n")

def ndispktscan(target):
    print("\n\033[34m[+] Sacnning pacng!\033[0m\n")
    os.system('python2 {} -f {} ndispktscan >./result/ndispktscan.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 扫描网络流量,结果保存在result目录下的ndispktscan.txt中!\033[0m\n")

def hivelist(target):
    print("\n\033[34m[+] Sacnning havelist!\033[0m\n")
    os.system('python2 {} -f {} hivelist >./result/hivelist.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 扫描注册表结束,结果保存在result目录下的hivelist.txt中!\033[0m\n")

def mimikatz(target):
    print("\n\033[34m[+] Cracking user and password!\033[0m\n")
    os.system('python2 {} -f {} mimikatz >./result/password.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 用户名和密码爆破成功,结果保存在result目录下的password.txt中!\033[0m\n")

def bitlocker(target):
    print("\n\033[34m[+] Cracking bitlocker!\033[0m\n")
    os.system('python2 {} -f {} bitlocker >./result/bitlocker.txt'.format(vol_dir,target))
    print("\n\033[32m[-] bitlocker密码爆破成功,结果保存在result目录下的bitlocker.txt中!\033[0m\n")


def txtfile(target):
    print("\n\033[34m[+] Sacnning txtfile!\033[0m\n")
    os.system('python2 {} -f {} filescan |grep "txt" >./result/txtfile.txt'.format(vol_dir,target))
    print("\n\033[32m[-] txt文件地址信息已到出到result目录中的 txtfile.txt中!\033[0m\n")

def flagfile(target):
    print("\n\033[34m[+] Sacnning flagfile!\033[0m\n")
    os.system('python2 {} -f {} filescan grep flag >./result/flagfile.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 扫描出与flag文件有关的信息已经放入result目录下的flagfile.txt中!\033[0m\n")

def filescan(target):
    print("\n\033[34m[+] Sacnning all file!\033[0m\n")
    os.system('python2 {} -f {} filescan >./result/allfile.txt'.format(vol_dir,target))
    print("\n\033[32m[-] 扫描出的文件地址及信息已经放入result目录下的allfile.txt中!\033[0m\n")

def main(target):

    print("\033[33m[+] 正在查询镜像中的进程\033[0m")

    pslist(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在查询镜像中的cmd命令\033[0m")
    cmdscan(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在查询镜像中的网络连接\033[0m")
    netscan(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在扫描镜像中的网络流量\033[0m")
    ndispktscan(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在查询镜像中的注册表\033[0m")
    hivelist(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在爆破镜像中登录用户名与登录密码\033[0m")
    mimikatz(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在爆破镜像中的BitLocker密码\033[0m")
    bitlocker(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在扫描镜像中的文本的文件\033[0m")
    txtfile(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在查询镜像中含有flag的文件\033[0m")
    flagfile(target)
    input("\033[33m[+] Continue?\033[0m\n")

    print("\033[33m[+] 正在扫描镜像中的全部文件\033[0m")
    filescan(target)
    input("\033[33m[+] Alldone,请前往result目录查看结果\033[0m\n")

main(sys.argv[1])
