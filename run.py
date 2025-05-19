import os
import re
import sys
import json
import xml.etree.ElementTree as ET
import platform
import tempfile
import requests
import shutil
import subprocess
from datetime import datetime


def write_json(path, data, encoding="utf8"):
    """写入json"""
    with open(path, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def read_json(path, default_data={}, encoding="utf8"):
    """读取json"""
    data = {}
    if os.path.exists(path):
        try:
            data = json.loads(open(path, "r", encoding=encoding).read())
        except:
            data = default_data
            write_json(path, data, encoding=encoding)

    else:
        data = default_data
        write_json(path, data, encoding=encoding)
    return data

def get_executable_path():
    '''获取可执行文件路径'''
    system = platform.system()
    if system == 'Windows':
        executable_path = './bin/wechatmp2markdown-v1.1.11_win64.exe'
    else:
        executable_path = './bin/wechatmp2markdown-v1.1.11_linux_amd64'
    # 添加执行权限
    os.chmod(executable_path, 0o755)
    # 返回可执行文件的完整路径
    return executable_path

def get_md_path(executable_path,url):
    '''获取md文件路径'''
    temp_directory = tempfile.mkdtemp()
    command = [executable_path, url, temp_directory, '--image=url']
    subprocess.check_output(command)
    for root, _, files in os.walk(temp_directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                yield file_path

def get_chainreactors_url():
    '''获取今日url'''
    current_date = datetime.now().strftime("%Y-%m-%d")
    base_url = 'https://raw.githubusercontent.com/chainreactors/picker/refs/heads/master/archive/daily/{}/{}.md'.format(current_date[:4], current_date)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://github.com/chainreactors/picker',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }
    try:
        response = requests.get(
            base_url,
            headers=headers,
        )
        urls = re.findall('(?:复现|漏洞|CVE-\d+|CNVD-\d+|CNNVD-\d+|XVE-\d+|QVD-\d+|POC|EXP|0day|1day|nday|RCE|代码执行|命令执行).*?(https://mp.weixin.qq.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',response.text,re.I)
        urls = [url.rstrip(')') for url in urls]
        return urls
    except:
        return []

def get_BruceFeIix_url():
    '''获取今日url'''
    current_date = datetime.now().strftime("%Y-%m-%d")
    base_url = 'https://raw.githubusercontent.com/BruceFeIix/picker/refs/heads/master/archive/daily/{}/{}.md'.format(current_date[:4], current_date)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://github.com/BruceFeIix/picker',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }
    try:
        response = requests.get(
            base_url,
            headers=headers,
        )
        urls = re.findall('(?:复现|漏洞|CVE-\d+|CNVD-\d+|CNNVD-\d+|XVE-\d+|QVD-\d+|POC|EXP|0day|1day|nday|RCE|代码执行|命令执行).*?(https://mp.weixin.qq.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',response.text,re.I)
        urls = [url.rstrip(')') for url in urls]
        return urls
    except:
        return []

import xml.etree.ElementTree as ET

def get_doonsec_url():
    '''从 Doonsec RSS 获取今日URL，使用 XML 解析'''
    cookies = {
        'UM_follow': 'True',
        'UM_distinctids': 'fgmr',
        'session': 'eyJfcGVybWFuZW50Ijp0cnVlLCJjc3JmX3Rva2VuIjoiMzU2ZDE4OTcwZjliZDljY2NjN2M3YzlkMzRhOGVlZWQyZDk1NmI1ZSIsInZpc3RvciI6ImZHTXJGQXBlVndRUnZrWjJHdWplV2gifQ.ZzidRw.GyjS15N12JYU0TByO31rrwBIiPY',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
    }

    try:
        response = requests.get('https://wechat.doonsec.com/rss.xml', cookies=cookies, headers=headers)
        response.encoding = response.apparent_encoding

        # XML 解析
        root = ET.fromstring(response.text)
        urls = []
        for item in root.findall('./channel/item'):
            title = item.findtext('title') or ''
            link = item.findtext('link') or ''
            if re.search(r'(复现|漏洞|CVE-\d+|CNVD-\d+|CNNVD-\d+|XVE-\d+|QVD-\d+|POC|EXP|0day|1day|nday|RCE|代码执行|命令执行)', title, re.I) and link.startswith('https://mp.weixin.qq.com/'):
                urls.append(link.rstrip(')'))

        return urls
    except Exception as e:
        print("Error parsing Doonsec RSS:", e)
        return []


def get_issue_url():
    file = '/tmp/issue_content.txt'
    if os.path.exists(file):
        content = open(file,'r',encoding='utf8').read()
        urls = re.findall('(https://mp.weixin.qq.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)',content,re.I)
        urls = [url.rstrip(')') for url in urls]
        return urls
    return []
    
def rep_filename(result_path):
    ''' 
    替换不能用于文件名的字符
    '''
    for root, _, files in os.walk(result_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                new_file = re.sub(r'[\/\\\:\*\?\"\<\>\|]', '', file)
                shutil.move(os.path.join(root, file), os.path.join(root, new_file))
                
def update_readme(urls):
    """更新README.md文件"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 读取现有内容
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 准备新内容
    new_content = f"""## 📢 datetime.now().strftime('%Y-%m-%d')日更新提醒

### 📚 新增文章

"""
    
    # 获取文章信息
    articles = []
    data = read_json('data.json')
    for url in urls:
        if url in data:
            title = data[url]
            articles.append({'title': title, 'url': url})
    
    # 添加文章
    for i, article in enumerate(articles, 1):
        new_content += f"{i}. {article['title']} <sub>🔗[来源]({article['url']})</sub> \n\n"
    
    # 添加统计信息
    new_content += f"""#### 📊 统计信息

<sub>📝 新增文章数：{len(articles)}篇</sub>  
<sub>⏰ 更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</sub>

---
"""
    
    # 在更新日志部分插入新内容
    update_log_marker = "## 📝 更新日志"
    update_log_index = content.find(update_log_marker)
    
    if update_log_index != -1:
        # 在更新日志标题后插入新内容
        new_content = content[:update_log_index + len(update_log_marker)] + "\n\n" + new_content + content[update_log_index + len(update_log_marker):]
    else:
        # 如果找不到更新日志部分，在文件末尾添加
        new_content = content + "\n\n" + new_content
    
    # 写入更新后的内容
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
                
def main():
    '''主函数'''
    data_file = 'data.json'
    data = {}
    executable_path = get_executable_path()
    base_result_path = 'doc'
    # 创建基于当前年月的子目录 (格式: YYYY-MM)
    current_month = datetime.now().strftime("%Y-%m")
    result_path = os.path.join(base_result_path, current_month)
    os.makedirs(result_path, exist_ok=True)
    # 读取历史记录
    data = read_json(data_file, default_data=data)
    if len(sys.argv) == 2:
        if sys.argv[1] == 'today':
            urls = list(set(get_chainreactors_url() + get_BruceFeIix_url() + get_doonsec_url()))
        else:
            urls = get_issue_url()
        
        new_urls = []  # 记录新添加的URL
        for url in urls:
            if url in data:
                continue
            for file_path in get_md_path(executable_path, url):
                name = os.path.splitext(os.path.basename(file_path))[0]
                if name == '.md':
                    continue
                shutil.copy2(file_path,result_path)
                data[url] = name
                write_json(data_file,data)
                new_urls.append(url)  # 添加到新URL列表
                print(name,end='、')
        
        # 如果有新文章，更新README.md
        if new_urls:
            update_readme(new_urls)
    
    rep_filename(result_path)
if __name__ == '__main__':
    main()
