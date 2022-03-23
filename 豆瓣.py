
#豆瓣电影 Top 250 2020年年度前250部电影


#导入所用的模块
import urllib.request                                               #用于操作URL的模块，我们爬取网页的时候，经常需要用到这个库。
import re                                                           #正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
from bs4 import BeautifulSoup                                       #BeautifulSoup4和 lxml 一样,主要的功能是如何解析和提取 HTML/XML 数据。
import xlwt                                                         #Excel表
import time                                                         #时间


def main():                                                         #main函数整理
    baseurl = "https://movie.douban.com/top250?start="              #基础网址
    datalist = getData(baseurl)                                     #数据表 = “获取数据”函数
    savepath = "电影.xls"                                           #保存路径
    saveData(datalist,savepath)                                     #“保存数据”函数



#爬取网页
def askURL(url):                                                    #网页爬取函数
    head = {                                                        #响应头伪装
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head)               #进行封装（有网站和头文件)
    html = ""                                                        #定义html
    try:                                                             
        response = urllib.request.urlopen(request)                   #打开网页
        html =response.read().decode("utf-8")                        #将全部数据于html.(utf-8解码)
    except urllib.error.URLError as e:                               #可能的异常
        if hasattr(e, "code"):                                      
            print(e,"code")                                          #打印出来异常
        if hasattr(e,"reason"):
            print(e,"reason")

    time.sleep(1.5)                                                  #访问间隔（防止短时多次访问）
    return html


#创建正则表达式规则对象(re.compile)         (全局变量)
#<a href="https://movie.douban.com/subject/1292052/">
findLink = re.compile(r'<a href="(.*?)">')                          #筛电影链接     
#<img width="100" alt="肖申克的救赎" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)                  #筛图片链接
#<span class="title">肖申克的救赎</span>
findTitle = re.compile(r'<span class="title">(.*)</span>')          #筛片名
#<span class="rating_num" property="v:average">9.7</span>
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')   #筛评分
#<span>2504557人评价</span>
findJudge = re.compile(r'<span>(\d*)人评价</span>')                  #筛评价人数
#<span class="inq">希望让人自由。</span>
findInq = re.compile(r'<span class="inq">(.*)</span>')               #筛概况
#<p class="">导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>1994/美国/犯罪 剧情</p>
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)                  #筛相关信息



#解析数据
def getData(baseurl):                                               #定义函数
    datalist =[]                                                    #存入所有的网页数据
    for i in range(0,10):                                           #调用十次页面信息
        url = baseurl + str(i*25)                                   #通过循环换网页
        html = askURL(url)                                          #保存源码

        #解析数据
        soup = BeautifulSoup(html,"html.parser")                    #定义解析 解析器
        #查询有div和class=item (注意：class在Python中属于关键字，所以加_以示区别)
        for item in soup.find_all('div',class_="item"):             #传入一个列表，返回所有匹配的节点
            data = []                                               #一部电影的全部
            item = str(item)                                        #转换成字符串   

            link = re.findall(findLink,item)[0]                     #re库来查找在item中符合模式的第一个元素（[0]）
            data.append(link)                                       #列表追加，到data里
            imgSrc = re.findall(findImgSrc, item)[0]                #同理
            data.append(imgSrc)                                     #同理
            titles = re.findall(findTitle,item)                     #片名中外名字
            if(len(titles)== 2):                                    #长度=2既有中文也有英文
                ctitle = titles[0]                                  #单独存储
                data.append(ctitle)                                 #中文名
                otitle = titles[1].replace("/","")                  #英文名前有/ ，进行替换
                data.append(otitle)                                 #外国名
            else:
                data.append(titles[0])
                data.append('  ')                                   #存一个空（excel表）

            rating = re.findall(findRating,item)[0]                 #同理
            data.append(rating)                                     #同理
            judgeNum = re.findall(findJudge,item)[0]                #同理
            data.append(judgeNum)                                   #同理
            inq = re.findall(findInq,item)                          #可能不存在
            if len(inq) !=0:                                        #存在
                inq = inq[0].replace("。","")                       #替换句号
                data.append(inq)                                    #存入
            else:
                data.append(" ")                                    #存空

            bd = re.findall(findBd,item)[0]                         #同理
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)                 #去掉<br/>
            bd = re.sub('/'," ", bd)                                #去掉/
            data.append(bd.strip())                                 #去掉空格
            
            datalist.append(data)                                   #数据放入datalist

    return datalist



#保存数据     于excel
def saveData(datalist,savepath):                                    #创建函数
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)      #创建对象
    sheet = book.add_sheet('电影',cell_overwrite_ok=True)           #创建工作表 覆盖单元格
    col = ('电影链接','图片链接','影片中文名','影片外国名','评分','评价数','概况','相关信息')
    for i in range(0,8):                                            #输入数据
        sheet.write(0,i,col[i])
    for i in range(0,250):
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])



    book.save(savepath)                                     #保存到excel


if __name__=="__main__":                                    #当程序执行时                              
    main()                                                  #调用函数main

print("爬取完成")                                            #完成