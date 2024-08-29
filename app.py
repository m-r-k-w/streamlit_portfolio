import pandas as pd
import streamlit as st

#  タイトルの設定 
st.title('StreamlitによるApp')
#  テキストの表示 
st.header('レッスン3:テキスト要素の追加')
# 通常のテキスト
st.text('これは通常のテキストです')
# マークダウン形式のテキスト
st.markdown('これは**太字**です。これは*イタリック*です')
# LaTeX形式の数式 
st.latex(r'\sqrt{x^2 + y^2} = z')

# 情報メッセージ（⻘⾊） 
st.info('データの読み込みが完了しました。') 
 
# 警告メッセージ（⻩⾊） 
st.warning('ファイルのサイズが⼤きいため、処理に時間がかかる可能性があります。') 
 
# エラーメッセージ（⾚⾊） 
st.error('ファイルの形式が正しくありません。CSVファイルをアップロードしてください。') 
 
# 成功メッセージ（緑⾊） 
st.success('グラフの作成が完了しました。') 
# コードの表示
code = '''def hello(): 
    print("Hello, Streamlit!")''' 
st.code(code, language='python') 

st.text('----------------------------------------------------')
st.header('レッスン4:データ入力と表示')

# テキスト入力
name = st.text_input('あなたの名前を入力してください')
if name:
    st.write(f'こんにちは、{name}さん！！')
# 数値入力
age = st.number_input('あなたの年齢を入力してください', min_value=0, max_value=120, value=20)
st.write(f'あなたは{age}歳です。')
# 日付入力
date = st.date_input('日付を選択してください', value=pd.to_datetime('2024/8/8'))
st.write(f'選択された日付は、{date}です。')
# サンプルデータの作成 
data = { 
    '名前': ['太郎', '花⼦', '⼀郎'], 
    '年齢': [25, 30, 35], 
    '都市': ['東京', '⼤阪', '福岡'] 
} 
df = pd.DataFrame(data) 
# データフレームの表⽰ 
st.subheader('データフレームの表⽰') 
st.dataframe(df) 
# 表の表示
st.subheader('表の表示')
st.table(df)

