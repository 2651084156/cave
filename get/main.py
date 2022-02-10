import base64
import fileinput
import operator
# for line in fileinput.input("1.mht" , encoding='UTF-8'):
#     print(line)
import os
import shutil
import time

from tqdm import tqdm

import css_main_get as css_plus
import xpath_main_get as xpa
import time, threading

tttt = '''<tr><td><div style=color:#006EFE;padding-left:10px;><div style=float:left;margin-right:6px;>你这个人最蒟蒻了qwq&nbsp;awa(2803639523)</div>10:08:19</div><div style=padding-left:20px;><font style="font-size:14pt;font-family:'汉仪蝶语体简','MS Sans Serif',sans-serif;" color='000000'>难度不就下来了？</font></div></td></tr>'''

f = '''<tr><td><div style=color:#006EFE;padding-left:10px;><div style=float:left;margin-right:6px;>Baka伯特(2677390946)</div>7:59:41</div><div style=padding-left:20px;><font style="font-size:10pt;font-family:'宋体','MS Sans Serif',sans-serif;" color='000000'>回声洞分洞——(291)<br><br>CMC-Na1.2g+2ml甘油研匀后加入16.8ml水+1g水杨酸细粉+尼泊金乙酯4滴研匀可得去脚底角质的软膏剂,孝敬长辈的必选品!<br>——吃瓜群众</font></div></td></tr>'''


# for line in fileinput.input("1.mht" , encoding='UTF-8'):
#     pass
strr = 0

# for line in open("1.mht" , encoding='UTF-8'):
#
#     if line == '------=_NextPart_DFBDCFAB_606C_4402_A865.4671C015A076\n':
#         strr =strr+1
#         print(strr)
#     if strr >=2:
#         break
#
#     with open("1.txt",'a', encoding='UTF-8') as fll:
#         fll.write(line)
#         # fll.write('\n')

# for line in open("1.txt" , encoding='UTF-8'):
#
#     if operator.contains(line, "回声洞分洞"):
#
#         with open("2.txt",'a', encoding='UTF-8') as fll:
#             fll.write(line)
#             # fll.write('\n')

# tt12= time.time()
#


# print(tt12-tt)
#
#
#
# tt = time.time()
# for line in open("2.txt" , encoding='UTF-8'):
#     ac = xpa.xpath_get(line, '//img')
#
#     if ac is not None:
#         for i in ac:
#             with open("3.txt", 'a', encoding='UTF-8') as fll:
#                 fll.write(xpa.xpath_out_html(i))
#                 fll.write('\n')
#
# tt12= time.time()
#
# print(tt12-tt)
# ccc = 0
# acac = 0
# cbcb = 0
# for line in open("1.mht", encoding='UTF-8'):
#
#     if line == '------=_NextPart_DFBDCFAB_606C_4402_A865.4671C015A076\n':
#         ccc = 1
#     if ccc == 1:
#         ccc = 0
#         acac = 1
#         continue
#
#     if acac == 1:
#         acac = 0
#         if operator.contains(line, "image"):
#             cbcb = 1
#
#     if cbcb == 1:
#         if operator.contains(line, "Content-Location"):
#             cbcb = 0
#             with open("8.txt", 'a', encoding='UTF-8') as fll:
#                 fll.write(line)
#
#         # fll.write('\n')
#
# for line in open("3.txt", encoding='UTF-8'):
#     aaq = css_plus.css_get_attr(line,'src')
#     with open("81.txt", 'a', encoding='UTF-8') as fll:
#         fll.write(aaq)
#         fll.write('\n')

#
# ccc = 0
# acac = 0
# cbcb = 0
# ca =0
# ccd0=0
# accd =''
# lll =[]
# for line in open("81.txt", encoding='UTF-8') :
#     lll.append(line.strip())
#
# a =0
# for line in open("1.mht", encoding='UTF-8'):
#
#     if line == '------=_NextPart_DFBDCFAB_606C_4402_A865.4671C015A076\n':
#         # print(line)
#         ccc = 1
#         ccd0 =0
#
#         # ccd0=1
#         # continue
#
#     # if ca == 1:
#     #     if line == '------=_NextPart_DFBDCFAB_606C_4402_A865.4671C015A076\n':
#     #         # print(line)
#     #         ccc = 1
#     #         ca =0
#     #         # ccd0=1
#     #         continue
#     # if operator.contains(line, "Content-Transfer-Encoding:"):
#     #     continue
#     if ccc == 1:
#         ccc = 0
#         acac = 1
#         continue
#
#     if acac == 1:
#         # acac = 0
#         if operator.contains(line, "Content-Type:image/"):
#             # print(line)
#             acac = 0
#             cbcb = 1
#             continue
#
#     if cbcb == 1:
#         if operator.contains(line, "Content-Location"):
#             cbcb = 0
#             ccd0 =1
#             # print(line)
#             accd = line.replace('Content-Location:','')
#             accd =accd.strip()
#             # print(accd)
#             continue
#
#     if ccd0 ==1:
#         if accd in lll:
#             with open("./1/"+accd, 'a', encoding='UTF-8') as fll:
#                 fll.write(line.strip())

        # fll.write('\n')

#
# with open('./1/{1C5C080E-444E-4147-8C63-4A22E3084485}.dat','r',encoding='utf8') as f:
#     inm = f.read()
#
# aaa = base64.b64decode(inm)
# # print(aaa)
# with open('11.png','ab') as f:
#     f.write(aaa)
# cccp ='./2/'
# for idx,i in enumerate(open('2.txt','r',encoding='utf8')):
#     # print(i)
#     # aa= xpa.xpath_get(i,'//div[2]')
#     # # print(aa)
#     # cc =xpa.xpath_out_html(aa[0])
#
#     # cc =xpa.xpath_out_test(cc)
#
#     cc =css_plus.css_find(i,'div:nth-child(2)')
#     a = css_plus.css_get_item(cc,'img')
#     if a is not None:
#         for ii in a:
#             aak ='<img src="data:image/png;base64,iVBORw0KGgo=..." />'
#             ack =css_plus.css_get_attr(ii,'src')
#             # print(ack)
#             with open('./1/'+ack,'a+',encoding='utf8') as fc:
#                 fc.seek(0,0)
#                 anm = fc.read()
#                 # print('./1/'+ack)
#             if anm !='':
#                 # print('cccc')
#                 cc =cc.replace(ii,'<img src="data:image/png;base64,'+anm+'" />')
#
#     with open('./2/'+str(idx)+'.html','a',encoding='utf8') as pig:
#         pig.write(cc)
#
# with open('./1/' + '{518D6793-0D52-47fb-A557-2638C35E82BA}.dat', 'r', encoding='utf8') as fc:
#     anm = fc.read()
    # print(anm)

    # cc =css_plus.css_get_text(cc)
    # print(cc)
    # print('-__________________________________')
    # b =cccp+str(idx)


    # print(a.strip())
def make_html(path,outf):
    b = './tmp/tmps/'
    if not os.path.exists(outf):  # 判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(outf)
    for idx,i in tqdm(enumerate(open(path,'r',encoding='utf8'))):
        # print(i)
        # aa= xpa.xpath_get(i,'//div[2]')
        # # print(aa)
        # cc =xpa.xpath_out_html(aa[0])

        # cc =xpa.xpath_out_test(cc)

        cc =css_plus.css_find(i,'div:nth-child(2)')
        a = css_plus.css_get_item(cc,'img')
        if a is not None:
            for ii in a:
                aak ='<img src="data:image/png;base64,iVBORw0KGgo=..." />'
                ack =css_plus.css_get_attr(ii,'src')
                # print(ack)
                with open(b+ack,'a+',encoding='utf8') as fc:
                    fc.seek(0,0)
                    anm = fc.read()
                    # print('./1/'+ack)
                if anm !='':
                    # print('cccc')
                    cc =cc.replace(ii,'<img src="data:image/png;base64,'+anm+'" />')

        with open(outf+str(idx)+'.html','a',encoding='utf8') as pig:
            pig.write(cc)

def fing_img(listt,path,lines):
    if os.path.isfile(path):
        if os.path.isfile(listt):


            ccc = 0
            acac = 0
            cbcb = 0
            ca =0
            ccd0=0
            accd =''
            lll =[]
            b ='./tmp/tmps/'
            if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
                os.makedirs(b)
            for line in open(listt, encoding='UTF-8') :
                lll.append(line.strip())

            a =0
            for line in tqdm(open(path, encoding='UTF-8')):
                scds =line.strip()
                if scds == lines:
                    # print(line)
                    ccc = 1
                    ccd0 =0

                    # ccd0=1
                    # continue

                # if ca == 1:
                #     if line == '------=_NextPart_DFBDCFAB_606C_4402_A865.4671C015A076\n':
                #         # print(line)
                #         ccc = 1
                #         ca =0
                #         # ccd0=1
                #         continue
                # if operator.contains(line, "Content-Transfer-Encoding:"):
                #     continue
                if ccc == 1:
                    ccc = 0
                    acac = 1
                    continue

                if acac == 1:
                    # acac = 0
                    if operator.contains(line, "Content-Type:image/"):
                        # print(line)
                        acac = 0
                        cbcb = 1
                        continue

                if cbcb == 1:
                    if operator.contains(line, "Content-Location"):
                        cbcb = 0
                        ccd0 =1
                        # print(line)
                        accd = line.replace('Content-Location:','')
                        accd =accd.strip()
                        # print(accd)
                        continue

                if ccd0 ==1:
                    if accd in lll:
                        with open(b+accd, 'a', encoding='UTF-8') as fll:
                            fll.write(line.strip())

            # fll.write('\n')

def fin_img_list(path,patho):
    if os.path.isfile(path):



        for line in tqdm(open(path, encoding='UTF-8')):
            aaq = css_plus.css_get_attr(line,'src')
            with open(patho, 'a', encoding='UTF-8') as fll:
                fll.write(aaq)
                fll.write('\n')

def get_getnanme_img(path,patho):


    for line in tqdm(open(path , encoding='UTF-8')):
        ac = xpa.xpath_get(line, '//img')

        if ac is not None:
            for i in ac:
                with open(patho, 'a', encoding='UTF-8') as fll:
                    fll.write(xpa.xpath_out_html(i))
                    fll.write('\n')

def get_hsd(path,tmp):


    for line in tqdm(open(path , encoding='UTF-8')):

        if operator.contains(line, "回声洞分洞"):

            with open(tmp,'a', encoding='UTF-8') as fll:
                fll.write(line)
                # fll.write('\n')

def get_text(path,linew,tmp):
    strr = 0

    for line in tqdm(open(path , encoding='UTF-8')):
        # print(linew)

        if line.strip() == linew:
            strr =strr+1
            # print(strr)
            # print(strr)
        if strr >=2:
            break

        with open(tmp,'a', encoding='UTF-8') as fll:
            fll.write(line)
            # fll.write('\n')






def get_fing(path):
    iaa = ''
    for i, iu in enumerate(open(path, encoding='utf8')):
        # print(iu.strip())
        if i == 6:
            # print(iu)
            iaa = iu.strip()
            break
    iaa =iaa.replace('boundary=','')
    iaa =iaa.strip('"')
    return  iaa

def clearimg(path):
    os.remove(path)

if __name__ == '__main__':
    tt = time.time()
    c ='./in/'
    ap = os.listdir(c)
    print(ap)
    for ci in tqdm(ap):
        shutil.rmtree('./tmp')
        os.mkdir('./tmp')
        ccd = c +ci
        abd =get_fing(ccd)
        main_a = '--'+abd
        tmp ='./tmp/' + ci +'.tmp1'
        # get_text(ccd,main_a,tmp)
        tmp2 = './tmp/' + ci + '.tmp2'
        # get_hsd(ccd,tmp2)
        t = threading.Thread(target=get_hsd, args=(ccd,tmp2))
        t2 = threading.Thread(target=get_text, args=(ccd,main_a,tmp))
        t.start()
        t2.start()
        t2.join()
        t.join()
        tmp3 = './tmp/' + ci + '.tmp3'
        tmp4 = './tmp/' + ci + '.tmp4'
        get_getnanme_img(tmp2, tmp3)
        fin_img_list(tmp3,tmp4)
        fing_img(tmp4,ccd,main_a)
        make_html(tmp2,'./out/'+ci.replace('.','')+'/')
        shutil.rmtree('./tmp')
        os.mkdir('./tmp')












    tt12 = time.time()
    print(tt12 - tt)