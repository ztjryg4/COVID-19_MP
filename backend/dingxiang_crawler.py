import requests
import re
import json
import time
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

    htmlfile = open("html.txt","w+")
    htmlfile.write(html)
    return html

def getBriefInfo():
    html = getHtml()
    reg1 = r'"countRemark":"(.*?)"'
    filter1 = re.compile(reg1)
    list1 = re.findall(filter1,html)
    if len(list1) != 0:
        # print(list1[0])
        try:
            brief = list1[0].replace("\\n"," ").replace("，"," ")
        except:
            brief = list1[0]
        return brief
    else:
        return -1

def getBriefTips():
    content = {
        "tips": [
        	"* 当前访问人数众多，可能出现响应延迟。",
            "传染源：野生动物，可能为中华菊头蝠；病毒：新型冠状病毒 2019-nCoV。",
            "传播途径未完全掌握，存在人传人、医务人员感染、一定范围社区传播，疫情扩散中，存在病毒变异可能。"
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

def getDetailInfoNew():
    html = getHtml()
    reg2 = r'getAreaStat = (.*?)}c'
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
                temp = i['provinceName']+'：'
                if i['confirmedCount']:
                    temp = temp + '确诊 ' + str(i['confirmedCount']) + ' 例 '
                if i['suspectedCount']:
                    temp = temp + '疑似 ' + str(i['suspectedCount']) + ' 例 '
                if i['curedCount']:
                    temp = temp + '治愈 ' + str(i['curedCount']) + ' 例 '
                if i['deadCount']:
                    temp = temp + '死亡 ' + str(i['deadCount']) + ' 例 '
                simpledata['detail'].append(temp)
        except:
            return -2
        else:
            return simpledata
    else:
        return -1

def getTempNews():
    content = {
        "news": []
    }
    tempcontent = {
        "title" : "暂无信息",
        "content" : ""
    }
    content['news'].append(tempcontent)
    return content

def getTimeLine():
    html = getHtml()
    reg3 = r'getTimelineService = (.*?)}c'
    filter3 = re.compile(reg3)
    list3 = re.findall(filter3,html)
    if len(list3) != 0:
        try:
            jsonstr = '{"news": ' + list3[0] + '}'
            jsonobj = json.loads(jsonstr)
            newsdata = jsonobj['news']
            content = {
                "news": []
            }
            for i in newsdata:
                tempnews = {
                    "title" : "",
                    "content" : ""
                }

                timestamp = int(i['pubDate']/1000)
                if timestamp:
                    time_local = time.localtime(timestamp)
                    pubDateString = time.strftime("%m-%d %H:%M",time_local)
                else:
                    pubDateString = '-'

                temptitle = '【动态】' + i['infoSource'] + '：' + i['title']
                tempcontent = i['summary'] + '(' + pubDateString + ')'
                tempnews['title'] = temptitle
                tempnews['content'] = tempcontent
                content['news'].append(tempnews)
        except:
            return getTempNews()
        else:
            return content
    else:
        return getTempNews()

def getRumor():
    html = getHtml()
    reg4 = r'getIndexRumorList = (.*?)}c'
    filter4 = re.compile(reg4)
    list4 = re.findall(filter4,html)
    # print(list4)
    if len(list4) != 0:
        try:
            jsonstr = '{"rumor": ' + list4[0] + '}'
            jsonobj = json.loads(jsonstr)
            newsdata = jsonobj['rumor']
            content = {
                "rumor": []
            }
            for i in newsdata:
                tempnews = {
                    "title" : "",
                    "content" : ""
                }
                temptitle = '【辟谣】' + i['title']
                tempcontent = i['mainSummary'] + '：' + i['body']
                tempcontent = tempcontent.replace("\\n"," ")

                tempnews['title'] = temptitle
                tempnews['content'] = tempcontent
                content['rumor'].append(tempnews)
        except:
            return 0 # error when getting rumors
        else:
            return content
    else:
        return 0

def getComplexTimeLine():
    newsContent = getTimeLine()
    rumorContent = getRumor()
    # print(rumorContent)
    if rumorContent != 0:
        try:
            tempContent = newsContent
            rumorNum = len(rumorContent['rumor'])
            for i in range(0,rumorNum):
                # print(i)
                tempContent['news'].insert(2*i,rumorContent['rumor'][i])
        except:
            return tempContent
        else:
            return newsContent
    else:
        return newsContent
    pass
# getHtml()
# print(getBriefInfo())
# getDetailInfo()
# getNews()
# getDetailInfoNew()
# print(getTimeLine())
print(getComplexTimeLine())
# getComplexTimeLine()
# print(getRumor())