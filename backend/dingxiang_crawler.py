import requests
import re
import json

def getHtml():
    dx_url = "https://3g.dxy.cn/newh5/view/pneumonia"
    headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                'Accept - Encoding':'gzip, deflate',
                'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
                'Connection':'Keep-Alive',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
    res = requests.get(dx_url, headers=headers)
    res.encoding = 'utf-8'
    html = res.text

    # htmlfile = open("html.txt","w+")
    # # htmlfile.write(html)
    return html

def getBriefInfo():
    html = getHtml()
    reg1 = r'"countRemark":"(.*?)"}'
    filter1 = re.compile(reg1)
    list1 = re.findall(filter1,html)
    if len(list1) != 0:
        print(list1[0])
        return list1[0]
    else:
        return -1

def getBriefTips():
    content = {
        "tips": [
            "病毒传染源: 尚不明确；病毒：新型冠状病毒 2019-nCoV",
            "传播途径: 未完全掌握，存在人传人、医务人员感染、一定范围社区传播",
            "传播进展：疫情扩散中，存在病毒变异可能"
        ]
    }
    # print(content)
    return content
    

def getDetailInfo():
    html = getHtml()
    reg2 = r'TypeService1 = (.*?)}c'
    filter2 = re.compile(reg2)
    list2 = re.findall(filter2,html)
    # print(list2)
    if len(list2) != 0:
        try:
            jsonstr = '{"detail": ' + list2[0] + '}'
            jsonobj = json.loads(jsonstr)
            detaildata = jsonobj['detail']
            simpledata = {'detail':[]}
            for i in detaildata:
                temp = i['provinceName']+'：'+i['tags']
                simpledata['detail'].append(temp)
        except:
            return -2
        else:
            return simpledata
    else:
        return -1

def getNews():
    content = {
        "news": []
    }
    tempcontent = {
        "title" : "暂无信息",
        "content" : ""
    }
    content['news'].append(tempcontent)
    # print(content)
    return content


# getBriefInfo()
# getDetailInfo()
# getNews()