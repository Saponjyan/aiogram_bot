import requests
from  bs4 import BeautifulSoup
from time import sleep
from threading import *
import tkinter as tk
# import PIL.Image
# img=PIL.Image.open("bab.ico")




def send_msg(text):
    tok=ttok.get()
    cid = iid.get()
    token = f"{tok}"
    chat_id = f"{cid}"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)



proc=50




headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
def zash():
    try:
        sa=requests.get("http://saponjyan.ru/parser.html",headers=headers)
    except:
        sleep(1)

    sl=requests.get("http://saponjyan.ru/lentascraper.html",headers=headers)
    if sl.reason != "OK":
        sleep(10000)
    else:
        sleep(1)

stranica=["","&page=3","&page=4","&page=5","&page=6","&page=7","&page=8","&page=9",
"&page=10","&page=11","&page=12","&page=13","&page=14","&page=15","&page=16","&page=17",
"&page=18","&page=19","&page=20","&page=21","&page=22","&page=23","&page=24","&page=25",
"&page=26","&page=27","&page=28","&page=29","&page=30","&page=31"]

# 754  magazinov
smag=['0001','0002','0003','0004','0005','0006','0007','0008',
'0009','0010','0011','0012','0013','0014','0015','0016','0017','0018','0019','0020','0021','0022','0023','0024',
'0025','0026','0027','0028','0029','0030','0031','0032','0033','0034','0035','0036','0037','0038','0039','0040',
'0041','0042','0044','0045','0046','0047','0048','0049','0050','0051','0052','0054','0055','0056','0057','0058',
'0059','0060','0061','0062','0063','0065','0066','0067','0068','0069','0071','0072','0073','0074','0075','0076',
'0077','0078','0079','0080','0081','0082','0083','0084','0085','0086','0087','0088','0089','0091','0092','0093',
'0094','0095','0096','0097','0098','0099','0100','0106','0107','0108','0109','0110','0111','0112','0113','0114',
'0115','0116','0117','0118','0119','0121','0122','0123','0124','0126','0127','0128','0129','0130','0131','0132',
'0134','0135','0136','0137','0139','0140','0141','0142','0144','0146','0147','0148','0149','0150','0151','0152',
'0153','0154','0155','0156','0157','0158','0160','0161','0163','0164','0165','0166','0167','0168','0169','0171',
'0172','0173','0174','0175','0176','0177','0178','0179','0180','0182','0183','0184','0185','0188','0191','0192',
'0194','0195','0196','0199','0200','0201','0202','0203','0204','0206','0207','0208','0209','0210','0211','0212',
'0213','0214','0215','0216','0217','0218','0219','0220','0221','0223','0224','0225','0226','0227','0228','0229',
'0230','0233','0235','0236','0237','0238','0240','0241','0242','0244','0245','0246','0247','0248','0260','0262',
'0263','0264','0265','0266','0267','0268','0269','0270','0271','0272','0273','0277','0279','0284','0285','0286',
'0291','0292','0293','0294','0295','0296','0297','0298','0299','0300','0301','0302','0303','0304','0306','0307',
'0309','0311','0312','0316','0317','0318','0319','0503','0601','0603','0605','0606','0607','0608','0609','0610',
'0612','0613','0614','0615','0616','0620','0621','0623','0624','0625','0626','0627','0628','0629','0630','0632',
'0634','0636','0639','0640','0641','0642','0643','0644','0646','0647','0648','0649','0651','0655','0656','0657',
'0660','0661','0664','0665','0667','0669','0670','0673','0675','0680','0702','0703','0704','0705','0706','0707',
'0709','0710','0712','0713','0714','0716','0717','0718','0719','0721','0722','0723','0724','0725','0726','0727',
'0734','0735','0736','0737','0738','0739','0740','0741','0742','0743','0746','0748','0749','0750','0751','0753',
'0801','0802','0807','0808','0809','0810','0811','0812','0816','0817','0818','0819','0820','0821','0823','0825',
'0829','0831','0832','0833','0834','0835','0836','0837','0838','0839','0840','0841','0842','0843','0844','0845',
'0846','0847','0848','0849','0850','0851','0852','0853','0854','0855','0904','0905','0906','0907','0908','0909',
'0911','0912','0913','0920','0921','0922','0923','0924','0925','0926','0927','0928','0929','0930','0931','0932',
'0933','0934','0935','0936','0937','0938','0939','0940','0941','0942','0943','0944','0945','1300','1301','1302',
'1303','1304','1305','1306','1307','1308','1309','1310','1311','1312','1313','1314','1315','1316','1319','1320',
'1321','1322','1323','1324','1326','1327','1328','1329','1330','1331','1332','1333','1334','1335','1336','1337',
'1338','1339','1340','1341','1342','1343','1344','1345','1346','1347','1348','1349','1350','1351','1352','1356',
'1357','1358','1359','1360','1361','1362','1363','1364','1365','1368','1369','1370','1371','1372','1373','1374',
'1375','1376','1377','1378','1379','1380','1381','1382','1383','1384','1386','1387','1388','1389','1390','1391',
'1392','1393','1394','1395','1396','1397','1398','1402','1403','1404','1405','1406','1407','1408','1409','1410',
'1411','1412','1413','1414','1415','1416','1417','1418','1419','1421','1422','1423','1424','1425','1426','1427',
'1428','1429','1430','1431','1434','1435','1437','1438','1439','1440','1445','1446','1447','1448','1449','1450',
'1451','1452','1453','1454','1455','1456','1457','1458','1459','1461','1462','1463','1464','1466','3000','3001',
'3002','3003','3007','3008','3011','3012','3014','3018','3022','3023','3024','3025','3026','3028','3029','3030',
'3031','3032','3033','3034','3035','3037','3038','3039','3040','3041','3043','3044','3045','3046','3048','3057',
'3061','3063','3064','3065','3066','3067','3069','3070','3071','3072','3073','3076','3077','3078','3081','3084',
'3085','3088','3090','3091','3092','3093','3094','3097','3098','3099','3102','3104','3107','3110','3111','3112',
'3118','3119','3121','3122','3126','3130','3131','3133','3134','3135','3137','3147','3149','3153','3154','3158',
'3162','3164','3165','3166','3168','3169','3171','3173','3175','3176','3176','3181','3182','3184','3193','3500',
'3501','3502','3503','3504','3505','3506','3507','3510','3511','3512','3513','3514','3515','3516','3518','3520',
'3522','3523','3525','3526','3528','3532','3535','3537','3538','3539','3540','3541','3542','3543','3545','3546',
'3548','3549','3550','3551','3552','3553','3554','3558','3559','3560','3561','3562','3565','3566','3568','3569',
'3570','3573','3574','3575','3576','3577','3579','3580','3582','3583','3586','3587','3590','3591','3592','3594',
'3595','3596','3598','3599','3602','3605','3606','3610','3611','3614','3616','3618','3620','3624','3627','3628',
'3629','3631','3632','3634','3635','3636','3637','3640','3648','3654',]
##################################################################################################
zash()
def start1():
    proc = int(login.get())
    
    stranica1=stranica[0:10]
    mag1=smag
    #count=0
    #mags=[]
    for i in mag1:
    #sleep(2)

        mag={'Store':f'{i}'}
        for z in stranica1:
            #location = '/fake_useragent%s.json' % fake_useragent.VERSION
            # ua = fake_useragent.UserAgent()#use_external_data=True, cache_path=location
            # headers={'user-agent':ua.random}
            response = requests.post(f"https://lenta.com/promo/?sorting=ByPriority{z}",headers=headers,cookies=mag)
            sleep(3)
            soup = BeautifulSoup(response.text,"lxml")
            cards=soup.find_all("div",class_="sku-card-small-container")
            pages=soup.find_all("a",role="button") 
            addrs=soup.find_all("div",class_="js-store-picker")
            #print(count)
            
            #count+=1
            try:
                for page in pages:
                
                    page=page.get('rel')
                #pag=page[2]
                #print(pag)
        
                for addr in addrs:
                
                    dat=addr.get("data-store")
                    da=dat.split(":")[2][1:-16]
                    dat=dat[7:11]
                    #print(dat)
                    #print(da)
    
                for card in cards:
                    zz='https://lenta.com'+card.find("a").get("href")
                    #print(zz)
                    card=card.text.split()
                    procent=int(card[0][:-1])
                    card=" ".join(card)
                    #procent=card[:2]
                    tex.insert(0.0,[f"|{card}\n"])
                    #print(card)
                    #print(procent)
                    #print(response.headers)

                    if int(procent)>proc:
                        #print(proc)
                        sms=zz+"\n"+card+" \n "+da
                        #print(card,da)
                        #mags.append(sms)
                        #telegram_send(messages=[sms])
                        send_msg(sms)
            except:
                #print("oshibka")
                #telegram_send(messages="error")
                sleep(2)

################################################################################################
def start2():
    proc = int(login.get())
    stranica2=stranica[:2]
    mag2=smag
    #count=0
    #mags=[]
    for i in mag2:
    #sleep(2)

        mag={'Store':f'{i}'}
        for z in stranica2:
            #location = '/fake_useragent%s.json' % fake_useragent.VERSION
            # ua = fake_useragent.UserAgent()#use_external_data=True, cache_path=location
            # headers={'user-agent':ua.random}
            response = requests.post(f"https://lenta.com/promo/?sorting=ByPriority&nodeCode=ga4638d8e16b266a51b9906c290531afb{z}",headers=headers,cookies=mag)
            sleep(3)
            soup = BeautifulSoup(response.text,"lxml")
            cards=soup.find_all("div",class_="sku-card-small-container")
            pages=soup.find_all("a",role="button") 
            addrs=soup.find_all("div",class_="js-store-picker")
            #print(count)
            #count+=1
            try:
                for page in pages:
                
                    page=page.get('rel')
                #pag=page[2]
                #print(pag)
        
                for addr in addrs:
                
                    dat=addr.get("data-store")
                    da=dat.split(":")[2][1:-16]
                    dat=dat[7:11]
                    #print(dat)
                    #print(da)
    
                for card in cards:
                    zz='https://lenta.com'+card.find("a").get("href")
                    #print(zz)
                    card=card.text.split()
                    procent=int(card[0][:-1])
                    card=" ".join(card)
                    #procent=card[:2]
                    tex.insert(0.0,[f"|{card}\n"])
                    #print(card)
                    #print(procent)

                    if int(procent)>proc:
                        #print(proc)
                        sms=zz+"\n"+card+" \n "+da
                        #print(card,da)
                        #mags.append(sms)
                        #telegram_send.send(messages=[sms])
                        send_msg(sms)
            except:
                #print("oshibka")
                #telegram_send.send(messages="error")
                sleep(2)
###############################################################################################
def start3():
    proc = int(login.get())
    stranica3=stranica[0:2]
    mag3=smag
    count=0
    #mags=[]
    for i in mag3:
    #sleep(2)

        mag={'Store':f'{i}'}
        for z in stranica3:
            #location = '/fake_useragent%s.json' % fake_useragent.VERSION


            response = requests.post(f" https://lenta.com/promo/?sorting=ByPriority&nodeCode=c565ed80964136a0374429fdc4d59ff8b{z}",headers=headers,cookies=mag)
            sleep(2)


            
            soup = BeautifulSoup(response.text,"lxml")
            cards=soup.find_all("div",class_="sku-card-small-container")
            pages=soup.find_all("a",role="button") 
            addrs=soup.find_all("div",class_="js-store-picker")
            #print(count)
            # print(response.headers)
            # print(response.cookies)
            count+=1
            try:
                for page in pages:
                
                    page=page.get('rel')
                #pag=page[2]
                #print(pag)
        
                for addr in addrs:
                
                    dat=addr.get("data-store")
                    da=dat.split(":")[2][1:-16]
                    dat=dat[7:11]
                    #print(dat)
                    #print(da)
    
                for card in cards:
                    zz='https://lenta.com'+card.find("a").get("href")
                    #print(zz)
                    card=card.text.split()
                    procent=int(card[0][:-1])
                    card=" ".join(card)
                    # try:
                    #     procent=int(card[:2])
                    # except:
                        
                        # print('osh')

                    tex.insert(0.0,[f"{card}\n"])
                    #print(card)
                    #print(procent)

                    if procent>proc:
                        #print(proc)
                        sms=zz+"\n"+card+" \n "+da
                        #print("11111111111111111")
                        #mags.append(sms)
                        #telegram_send.send(messages=[sms])
                        #await bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nРад что ты зашел\nЯ тупенький бот но я все равно смогу расказать все что ты хочеш знать.\nа что тебе интересно?'.format(message.from_user), reply_markup=but)
                        #await bot.send_message(idd,sms)
                        send_msg(sms)
                        #print("2222222222222222222")
            except:
                #print("oshibka")
                sleep(1)
                #telegram_send.send(messages=["error"])
                #sleep(2)

################################################################################################



t1= Thread(target=start1)
t2= Thread(target=start2)
t3= Thread(target=start3)
# t4= Thread(target=start4)
def st1():
    t1.start()
def st2():
    t2.start()
def st3():
    t3.start()



#img="pn.png"
win = tk.Tk()
win.title('Saponjyan.ru')
win.geometry("450x250")
win.resizable(True,True)
#win.iconbitmap('pn.png')
#win.wm_iconbitmap(bitmap=img)

tex=tk.Text(win,width=150,height=4)
tex.pack()
loginl=tk.Label(win,text='lenta.com scraper')
loginl.pack()


login=tk.Entry(win)
login.pack()
login.insert(0,50)

iid=tk.Entry(win)
iid.pack()
iid.insert(0,"your telegram id")


ttok=tk.Entry(win)
ttok.pack()
ttok.insert(0,"your telegram-bot token")

btn= tk.Button(win,text='Start all',command=st1).pack()
btn2= tk.Button(win,text='Products for children',command=st2).pack()
btn3= tk.Button(win,text='Children food',command=st3).pack()
btn4= tk.Button(win,text='STOP',command=win.destroy).pack()
win.mainloop() 

