## Import packages
import streamlit as st
import pandas as pd
import numpy as np


## Import data
df_mtbi = pd.read_csv("MBTI.csv")
df_ins = pd.read_csv("BNP_ins.csv")

## Header
from PIL import Image
image1 = Image.open('C:/Users/hp/streamlit_Dev/banner_1.jpg')
st.image(image1)

## Website
st.title('MBTI保單健檢行銷員')
st.text('最懂你的數位業務員 帶你了解你所需要的一切保單')

def Layouts_plotly():
    st.sidebar.write('法國巴黎人壽')
    add_selectbox = st.sidebar.radio(
        "數位保單健檢服務",
        ("數位服務介紹", "MBTI人格測驗", "基本個人資料",'個人保單存摺',"保單健診結果分析","數位智能業務員",'各銀行服務據點')
    )


def main():
    Layouts_plotly()
    
if __name__ == "__main__":
    main()



## Block 1
st.subheader('數位服務介紹')

col1, col2 = st.columns(2)
with col1:
    image10 = Image.open('C:/Users/hp/streamlit_Dev/pic_1.jpg')
    st.image(image10)
with col2:
    image11 = Image.open('C:/Users/hp/streamlit_Dev/pic_2.jpg')
    st.image(image11)

st.write('「投資型保單好難好複雜?!」、「該怎麼買才是真的有保障呀?」')
st.write('您也有這樣的煩惱嗎？只要短短五分鐘，MBTI保單健檢行銷員利用時下最流行的MBTI人格測驗和大數據保單健檢分析，除了讓您了解什麼樣的投資型保單最適合您的性格，也可以幫您檢查你現在所需的投資組合！')



## Block 2
st.subheader('MBTI人格測驗')

q_1 = st.selectbox('你在下列哪種情況比較能獲得能量？', ['請選擇一符合的情形','獨處，一個人追劇打電動','出去玩，或和朋友或家人相聚'])
if q_1 == '獨處，一個人追劇打電動':
    EI = 1
elif q_1 == '出去玩，或和朋友或家人相聚':
    EI = 0
q_2 = st.selectbox('當你學習新事物時，你傾向？', ['請選擇一符合的情形','天馬行空，喜歡開放性思考','依照經驗，需要明確方向'])
if q_2 == '天馬行空，喜歡開放性思考':
    SN = 1
elif q_2 == '依照經驗，需要明確方向':
    SN = 0
q_3 = st.selectbox('當你在溝通時，你傾向？', ['請選擇一符合的情形','先看這件事有沒有合乎邏輯或公平性','先確認對方感受，希望和諧相處'])
if q_3 == '先看這件事有沒有合乎邏輯或公平性':
    TF = 1
elif q_3 == '先確認對方感受，希望和諧相處':
    TF = 0
q_4 = st.selectbox('出國旅遊之前，你通常會？', ['請選擇一符合的情形','列好每個行程，並按照計畫進行','去到那裡再說，當天看心情決定'])
if q_4 == '列好每個行程，並按照計畫進行':
    PJ = 1
elif q_4 == '去到那裡再說，當天看心情決定':
    PJ = 0


if st.button('查看測驗結果'):
    if q_1 != '請選擇一符合的情形' or q_2 != '請選擇一符合的情形' or q_3 != '請選擇一符合的情形' or q_4 != '請選擇一符合的情形':
        set1 = df_mtbi['EI']==EI
        set2 = df_mtbi['SN']==SN
        set3 = df_mtbi['TF']==TF
        set4 = df_mtbi['PJ']==PJ
        MTBI = df_mtbi[(set1 & set2 & set3 & set4)]
        st.write('測驗結果：',MTBI['MBTI'].iloc[0],'|',MTBI['NAME'].iloc[0])
        image2 = Image.open('C:/Users/hp/streamlit_Dev/MBTI/'+MTBI['MBTI'].iloc[0]+'.jpg')
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.image(image2, width=350)
        st.write(MTBI['PROS'].iloc[0])
        st.write(MTBI['PEOPLE'].iloc[0])
    else:
        st.write('請先完成以上題目')
else:
    st.write('請先完成以上題目')



## Block 3
st.subheader('基本個人資料')

name=st.text_input('請輸入您的姓名：')

age=st.number_input('請輸入您的年齡：',min_value=0,max_value=120)

name=st.selectbox('請輸入您的職業：',['請選擇符合的職業','A','B','C','D'])

income=st.selectbox('請輸入您的年收入：',['請選擇符合的收入狀況','3萬以下','3萬以上，5萬以下','5萬以上，10萬以下','10萬以上'])

life=st.selectbox('請選擇您的投資目的：',['請選擇符合的投資目的','長期生涯規畫型','家庭保障型'])



## Block 4
st.subheader('個人保單存摺')
id=st.text_input('請輸入您的身分證字號：')

ins_1 = {
    "保單名稱":['法商法國巴黎人壽金色榮耀變額年金保險','台灣人壽好易保一年定期壽險'],
    "保單期間":['終身','定期'],
    "保單生效日期":['101-06-06','112-03-07'],
    "保險類別":['投資型年金','定期壽險'],
    "保單幣別":['台幣','台幣'],
    "保單投資風險":['第4級','無']
}
ins_1 = pd.DataFrame(ins_1)


if st.button('查看保單存摺'):
    if id != '':
        st.dataframe(ins_1)



## Block 5
st.subheader('保單健診結果分析')

#ins_fit = pd.DataFrame(ins_fit, columns=("保單名稱","保單期間","保單幣別","保單風險","年均報酬率"))

if st.button('查看保單健診結果'):
    if id != '':
        
        # 萬能1 年金0 ins_class
        if TF == 1 & PJ == 1:
            ins_class = 1
            word_1 = '人格特質分析'
            word_2 = '您注重和諧且具備豐沛之同理心，同時偏好靈活且能根據自身變動的選擇，具備高度彈性且有保障性的萬能保險'
        elif TF == 1 & PJ == 0:
            ins_class = 0
            word_1 = '人格特質分析'
            word_2 = '您著重邏輯分析和因果關係，善於至定計畫並有條理、有規律地完成，按部就班充滿計畫性質的年金保險'
        elif life == '家庭保障型':
            ins_class = 1
            word_1 = '投資的目標'
            word_2 = '能提供您與家人更完整壽險保障的萬能保險'
        elif life == '長期生涯規畫型':
            ins_class = 0
            word_1 = '投資的目標'
            word_2 = '能提供未來退休生活穩定收入的年金保險'
        # 風險低0 風險高1 risk
        if SN == 0:
            set22 = df_ins['風險'] == 3
            word_3 = '對於嘗試不同的新鮮事總是充滿興趣，總是思索事物之未來可能性'
            word_4 = '風險類別較高'
        elif SN == 1:
            set22 = df_ins['風險'] >= 4
            word_3 = '為人務實，關注最重要的事實，且相信經驗而非未來可能性'
            word_4 = '風險類別較低'
        # 標的少0 標的多1 target
        if EI == 0:
            set33 = df_ins['投資標的數'] <= 200
            word_5 = '內向的你能透過獨處思考獲得能量，尋求知識的深度'
            word_6 = '採取相對集中的投資策略'
        elif EI == 1:
            set33 = df_ins['投資標的數'] >= 200
            word_5 = '外向的你總是能透過外界獲得滿滿的能量，更擅長尋求知識的廣度'
            word_6 = '具有多元的投資標的且相對分散之投資策略'
        # 台幣0 外幣1
        if len(ins_1[ins_1['保單幣別']=='台幣']) > len(ins_1[ins_1['保單幣別']=='外幣']):
            coin = 0
            word_7 = '台幣'
        elif len(ins_1[ins_1['保單幣別']=='台幣']) < len(ins_1[ins_1['保單幣別']=='外幣']):
            coin = 1
            word_7 = '外幣'
        elif len(ins_1[ins_1['保單幣別']=='台幣']) == len(ins_1[ins_1['保單幣別']=='外幣']):
            coin = [0,1]
            word_7 = '台幣'
        
        set11 = df_ins['萬能'] == ins_class
        set44 = df_ins['幣別'] == coin
        set55 = df_ins['Age_max'] > age
        set66 = df_ins['Age_min'] <= age

        ins_fit = df_ins[(set11 & set22 & set33 & set44 & set55 & set66)]
        ins_fit = ins_fit[['保單名稱','保單幣別','保單類型',"保單風險分類",'投資標的數']]
        #st.dataframe(ins_fit.style.)
        #st.dataframe(ins_fit[['保單名稱','幣別','萬能','年金',"風險",'投資標的數']], use_container_width=st.session_state.use_container_width)
        st.dataframe(ins_fit)
        st.write('以上為我們所推薦最適合您的投資型保單選項。我們根據您的'+ word_1 +
                 '，認為'+ word_2 +
                 "較能符合您的需求，此外，您"+ word_3 +
                 "，所以我們也推薦了"+ word_4 +"的投資型保單給您。從您的人格特質中我們也可以發現，"+
                 word_5 +"，所以我們也為您篩選出了"+ word_6 +
                 "供您參考，最後我們也依照您的投資習慣，提供了"+ word_7 +"相關的保單，")
    else:
        st.write('請先填寫完成以上資料')

else:
    st.write('請先填寫完成以上資料')



## Block 6
st.subheader('數位智能業務員')

image100 = Image.open('C:/Users/hp/streamlit_Dev/pic_3.png')
st.image(image100)



## Block 7
st.subheader('各銀行服務據點')

df1 = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [25.03, 121.55],
    columns=['lat', 'lon'])

st.map(df1)

bank = {
    "銀行名稱": ["台北富邦銀行", "國泰世華商業銀行", "玉山銀行", "中國信託商業銀行"],
    "連絡電話": ['0800-099-799', '0800-818-008', '0800-301-313', '0800-017-888'],
}

st.dataframe(bank)


