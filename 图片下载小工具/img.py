import requests
 
# 声明全局变量
down_list = []
 
 
# 读取下载列表函数
def open_file(txt):
    global down_list
    try:
        file = open(txt, "r", encoding="utf-8")
        temp_lists = file.readlines()  # 取出每行作为数组
        for i in temp_lists:
            down_list.append(i.replace("\n", ""))
        print("共获取到" + str(len(down_list)) + "个下载任务!")
    except Exception as e:
        print(e)
 
 
# 下载函数
def download(url, name, proxy=""):
    # Header请求头，如有其它参数的可以往里面加
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    }
    # 代理信息
    proxy_temp = {
        "http": "",
        "https": ""
    }
    if "127.0.0.1" in proxy:
        proxy_temp["http"] = "http://" + proxy
        proxy_temp["https"] = "https://" + proxy
    else:
        proxy_temp["http"] = proxy
        proxy_temp["https"] = proxy
    try:
        r = requests.get(url, headers=headers, proxies=proxy_temp, timeout=20)
        with open(name, "wb") as code:
            code.write(r.content)
    except Exception as e:
        print(e)
 
 
# 列表去重函数
def check_list(lists):
    temp = []
    for i in lists:
        if not i in temp:
            temp.append(i)
    return temp
 
 
if __name__ == '__main__':
    input("请将要下载的图片链接以一行一个的形式，存放在 @list.txt@ 中，完成后请按 Enter 键：")
    open_proxy = input("是否使用代理（下载被墙的图片） 1. 关闭（默认） 2. 开启：")
    if open_proxy == "2":
        input_proxy = input("请输入代理IP，以 IP:端口 的形式，如 127.0.0.1:1080 这样:")
    else:
        pass
    input_filename = input("请输入要删除的URL前缀，不然你的文件名将会是完整的URL名称：")
    open_file("list.txt")
    final_list = check_list(down_list)
    print("去重后共获取到" + str(len(final_list)) + "个图片链接，开始下载...")
    for file_url in final_list:
        file_name = file_url.replace(input_filename, "").replace('/', "").replace('\\', "").replace('*', "").replace(
            '?', "").replace('<', "").replace('>', "").replace(':', "").replace('|', "")  # 删除url前缀
        if open_proxy == "2":
            download(file_url, file_name, input_proxy)
        else:
            download(file_url, file_name)
    input("下载已完成!")
