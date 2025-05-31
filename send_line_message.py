
import requests
import os

import urllib.request as req
url="https://tw.stock.yahoo.com/world-indices"
#建立一個request物件附加headers資訊
request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
#print(data)

import bs4
#root=bs4.BeautifulSoup(data,"html.parser")
#print(root.title.string)
global soup

# 使用 BeautifulSoup 解析 HTML
soup = bs4.BeautifulSoup(data, 'html.parser')


def dj():
    # 找到道瓊指數的外層 li
    dj_card=soup.find("span", string="道瓊工業指數").find_parent("li")
    #print(dj_card)
    # 擷取各項數據-道瓊
    all_spans=dj_card.find_all("span", class_="Fz(14px)")
    all_spans2=dj_card.find_all("span", class_="Fw(600)")

    dj_time=all_spans[-1].text.strip()
    dow_price=dj_card.find_all("span",class_="Jc(fe)")[0]
    prev_close1=dj_card.find_all('span', class_="Jc(fe)")
    prev_close2=prev_close1[6]


    change_price=all_spans2[1]
    change_percent=all_spans2[-1]

    price1=prev_close2.text.strip()
    price2=dow_price.text.strip()
    fpr1=float(price1.replace(",",""))
    fpr2=float(price2.replace(",",""))

    if fpr1<=fpr2:
      j="+"
    else:
      j="-"   
    
    msg = f"""== 道瓊工業指數 ==
    資料時間: {dj_time}
    道瓊指數: {price2}
    昨    收: {price1}
    漲    跌: {j} {change_price.text.strip()}
    漲 跌 幅: {j} {change_percent.text.strip()}
    """
    return msg

    # 顯示結果
    #print("=============== 道瓊工業指數 ===============")
    #print("資料時間:", dj_time)
    #print("道瓊指數:", dow_price.text.strip())
    #print("昨    收:", prev_close2.text.strip())
    #print("漲    跌:", j , change_price.text.strip())
    #print("漲 跌 幅:", j , change_percent.text.strip())

                
def sp():
    # 找出指數卡片區塊（S&P 500）
    sp500_card = soup.find('span', string="S&P 500指數").find_parent('li')
    # 股價
    price = sp500_card.find_all('span', class_='Fw(600)')[0].text.strip()
    # 漲跌
    change = sp500_card.find_all('span', class_='Fw(600)')[1].text.strip()
    # 漲跌幅
    percent = sp500_card.find_all('span', class_='Fw(600)')[2].text.strip()

    # 昨收：根據順序，第 4 個價格類欄位（注意 class 不同）
    close = sp500_card.find_all('span', class_='Jc(fe)')[6].text.strip()
    
    #時間
    all_spans=sp500_card.find_all("span", class_="Fz(14px)")
    dj_time=all_spans[-1].text.strip()
    
    #比較昨天與今天
    fpr1=float(close.replace(",",""))
    fpr2=float(price.replace(",",""))

    if fpr1<=fpr2:
      j="+"
    else:
      j="-"   
    
    msg = f"""== S&P500指數 ==
    資料時間: {dj_time}
    S&P 500: {price}
    昨    收: {close}
    漲    跌: {j} {change}
    漲 跌 幅: {j} {percent}
    """
    return msg
    """
    print("================ S&P500指數 ================")
    print("資料時間:", dj_time)
    print("S&P 500:", price)
    print("昨    收:", close)
    print("漲    跌:",j, change)
    print("漲 跌 幅:",j, percent)
    """
    
def nasdaq():
    # 找到 NASDAQ 的外層區塊：根據「NASDAQ指數」這個文字往上找 li
    nasdaq_card = soup.find('span', string="NASDAQ指數").find_parent('li')
    # 擷取現價
    price = nasdaq_card.find_all('span', class_='Fw(600)')[0].text.strip()
    # 擷取漲跌
    change = nasdaq_card.find_all('span', class_='Fw(600)')[1].text.strip()
    # 擷取漲跌幅
    percent = nasdaq_card.find_all('span', class_='Fw(600)')[2].text.strip()
    # 擷取昨收（第 4 個 'Jc(fe)' 類別的 span，從你的 HTML 可看出）
    close = nasdaq_card.find_all('span', class_='Jc(fe)')[6].text.strip()
    #時間
    all_spans=nasdaq_card.find_all("span", class_="Fz(14px)")
    dj_time=all_spans[-1].text.strip()
    #比較昨天與今天
    fpr1=float(close.replace(",",""))
    fpr2=float(price.replace(",",""))

    if fpr1<=fpr2:
      j="+"
    else:
      j="-"   
    
    msg = f"""== NASDAQ ==
    資料時間: {dj_time}
    NASDAQ: {price}
    昨  收: {close}
    漲  跌: {j} {change}
    漲跌幅: {j} {percent}
    """
    return msg
    """
    print("================ NASDAQ指數 ================")
    print("資料時間:", dj_time)
    print("NASDAQ:", price)
    print("昨  收:", close)
    print("漲  跌:",j, change)
    print("漲跌幅:",j, percent)
    """
    
def sox():
    # 找到費城半導體指數的外層 li
    sox_card = soup.find('span', string="費城半導體指數").find_parent('li')
    # 擷取現價
    price = sox_card.find_all('span', class_='Fw(600)')[0].text.strip()
    # 擷取漲跌
    change = sox_card.find_all('span', class_='Fw(600)')[1].text.strip()
    # 擷取漲跌幅
    percent = sox_card.find_all('span', class_='Fw(600)')[2].text.strip()
    # 擷取昨收（同樣抓第 4 個 'Jc(fe)'）
    close = sox_card.find_all('span', class_='Jc(fe)')[6].text.strip()
    #時間
    all_spans=sox_card.find_all("span", class_="Fz(14px)")
    dj_time=all_spans[-1].text.strip()
    #比較昨天與今天
    fpr1=float(close.replace(",",""))
    fpr2=float(price.replace(",",""))

    if fpr1<=fpr2:
      j="+"
    else:
      j="-"   
      
    msg = f"""== 費城半導體指數 ==
    資料時間: {dj_time}
    費城半導體: {price}
    昨     收: {close}
    漲     跌: {j} {change}
    漲  跌  幅: {j} {percent}
    """
    return msg
    """  
    print("============== 費城半導體指數 ==============")
    print("資料時間:", dj_time)
    print("費城半導體:", price)
    print("昨  收:", close)
    print("漲  跌:",j, change)
    print("漲跌幅:",j, percent)
    """
    
#---------------------------------------------------------------------------
#黃金白銀報價
def goldsliver():
    import json
    from datetime import datetime, timezone, timedelta
    headers = {
    "x-access-token": "goldapi-4r2h6smbc4f5lr-io",
    "User-Agent": "Mozilla/5.0"}
    
    urlxau = "https://www.goldapi.io/api/XAU/USD"  # 查黃金對美元
    urlxag = "https://www.goldapi.io/api/XAG/USD"  # 查黃金對美元
    responsexau = requests.get(urlxau, headers=headers)
    responsexag = requests.get(urlxag, headers=headers)
    dataxau=responsexau.json()    
    dataxag=responsexag.json()
    #print(data)
    
    # 建立 UTC 時間
    tsxau=dataxau['timestamp']
    utc_timexau = datetime.fromtimestamp(tsxau, tz=timezone.utc)
    # 加上台灣的時區（UTC+8）
    tw_timexau = utc_timexau + timedelta(hours=8)
    pricexau=dataxau["price"] #黃金現價
    chxau=dataxau["ch"]
    chpxau=dataxau["chp"]
    
     # 建立 UTC 時間
    tsxag=dataxag['timestamp']
    utc_timexag = datetime.fromtimestamp(tsxag, tz=timezone.utc)
    # 加上台灣的時區（UTC+8）
    tw_timexag = utc_timexag + timedelta(hours=8)
    pricexag=dataxag["price"] #黃金現價
    chxag=dataxag["ch"]
    chpxag=dataxag["chp"]
    
    inf=f"""
    == 黃金報價 ==
    資料時間: {tw_timexau} 
    價格: {pricexau} 美元/盎司
    漲跌: {chxau} 美元
    漲跌幅: {chpxau} %
    
    == 白銀報價 ==
    資料時間: {tw_timexag} 
    價格: {pricexag} 美元/盎司
    漲跌: {chxag} 美元
    漲跌幅: {chpxag} %
    
    """
    #print(inf)
    return inf   
#--------------------------------------------------------------------------------------------
#美國30年國債殖利率
def get_30y_yield(api_key):
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": "DGS30",
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        obs = data["observations"][0]
        date = obs["date"]
        value = obs["value"]
        print(f"美國30年國債殖利率：{value}%（更新日期：{date}）")
        return value, date
    except (KeyError, IndexError):
        print("讀取資料失敗：", data)
        return None

# ✅ 將這裡換成你自己的 API 金鑰
us30rate = str(get_30y_yield("b8bc49ca47acb7dada9fdd889ab66928"))

#---------------------------------------------------------------
#匯率
def get_usd_exchange_rates(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        print("讀取匯率資料失敗：", data)
        return

    rates = data["conversion_rates"]
    update_time = data["time_last_update_utc"]

    currencies = {
        "TWD": "台幣",
        "JPY": "日圓",
        "EUR": "歐元",
        "GBP": "英鎊",
        "CNY": "人民幣"
    }

    msg = f"💱 匯率更新時間（UTC）：{update_time}\n\n"
    for code, name in currencies.items():
        rate = rates.get(code)
        if rate:
            msg += f"1 美元 = {rate:.4f} {name}（{code}）\n"
        else:
            msg += f"❌ 無法取得 {name}（{code}）匯率\n"
    return msg
money = get_usd_exchange_rates("ec260df72b83c9dd309c93b0")
#-----------------------------------------------------------------------------------------------

message = dj() + "\n" + sp() + "\n" + nasdaq() + "\n" + sox()
goldinf = goldsliver()
#print(message)


line_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
user_id = os.environ['LINE_USER_ID']

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {line_token}"
}

data = {
    "to": user_id,
    "messages": [ {"type": "text", "text": "五寶們早安! 榴槤機器人來報告！"},
        {"type": "text", "text": message},
        {"type": "text", "text": goldinf},
        {"type": "text", "text": us30rate},
        {"type": "text", "text": money}]
}

res = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, json=data)
print(res.status_code, res.text)
