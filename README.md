# 2019 新冠肺炎疫情动态小程序  
新冠肺炎 (COVID-19) 疫情动态小程序，数据来自国家卫健委、丁香园 · 丁香医生等。  

近期小程序访问人数众多，为了防止对生产环境的 API 服务器造成过大压力，已隐藏了项目代码中的 API 请求地址。  

## 想法  
看到近期武汉乃至全国日渐严重的疫情，希望通过自己的方式，让更多人及时了解疫情进展以及动态，为疫情防控尽绵薄之力。  

## 介绍  
`MP` 目录为小程序代码部分，采用微信原生开发。  

`backend` 目录为丁香园爬虫及服务端支持程序。使用 Python 实时爬取丁香园网站的数据，使用  
Flask 框架提供服务端支持。  

为减轻服务端压力，爬虫仅爬取了微信小程序需要使用的部分疫情数据，未提供完整的疫情数据支持。更完善的疫情数据请转向这个项目：https://github.com/BlankerL/DXY-2019-nCoV-Crawler  

## 其他  
### 微信访问  
~~通过下方的小程序码或搜索「新冠疫情」~~  

受个人资质所限，小程序目前已在微信平台上下架。
### 相关项目  
[wuhan2020](https://github.com/wuhan2020) 由 Xlab 开放实验室发起的 wuhan2020 开源项目，正通过开源的方式收集经过审核与确认过的武汉新型冠状病毒防疫相关信息，旨在统一收集本次事件中相关事务处理方的信息，并利用开源和分布式协作优势实时更新并通报，提供各方的联系平台。  
### 支持  
本项目所产生的上云资源费用支出目前完全可控，因此不需要任何捐赠支持，如果你有捐赠的想法，请移步~~当地红十字会或其他~~与本次疫情有关的可信公益项目，他们将更好地安排资金，帮助到疫情中需要帮助的人。  

**祝大家身体健康，平安过年！**  
