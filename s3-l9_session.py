import streamlit as st 
import pandas as pd 
import plotly.graph_objects as go 
import numpy as np 
import time 

# レッスン9: セッション状態の管理
st.header('レッスン9: セッション状態の管理') 

# ＊＊＊カウンター＊＊＊
st.subheader('＊＊＊カウンター＊＊＊')

# 'count' がセッション状態に存在しない場合、初期値として0を設定します。
if 'count' not in st.session_state: 
    st.session_state.count = 0 

# 現在のカウントを表示します。
st.write(f"現在のカウント: {st.session_state.count}") 

# "カウントアップ"ボタンがクリックされた場合の処理
if st.button('カウントアップ'): 
    # カウントを1増やします。
    st.session_state.count += 1 
    # アプリを再実行して、更新されたカウントを表示します。
    st.rerun() 


# ＊＊＊フォーム入力の維持＊＊＊
st.subheader('＊＊＊フォーム入力の維持＊＊＊')

# 'user_name' がセッション状態に存在しない場合、初期値として空文字列を設定します。
if 'user_name' not in st.session_state: 
    st.session_state.user_name = ""
# 'user_email' がセッション状態に存在しない場合、初期値として空文字列を設定します。
if 'user_email' not in st.session_state: 
    st.session_state.user_email = "" 

# ユーザー名入力欄を表示します。セッション状態に保存されたユーザー名があれば初期値として表示します。
user_name = st.text_input("ユーザー名", value=st.session_state.user_name) 
# メールアドレス入力欄を表示します。セッション状態に保存されたメールアドレスがあれば初期値として表示します。
user_email = st.text_input("メールアドレス", value=st.session_state.user_email) 

# "ユーザー情報を保存"ボタンがクリックされた場合の処理
if st.button("ユーザー情報を保存"): 
    # 入力されたユーザー名をセッション状態に保存します。
    st.session_state.user_name = user_name 
    # 入力されたメールアドレスをセッション状態に保存します。
    st.session_state.user_email = user_email 
    # 成功メッセージを表示します。
    st.success("ユーザー情報が保存されました！") 

# セッション状態に保存されたユーザー名を表示します。
st.write(f"セッションに保存されたユーザー名: {st.session_state.user_name}") 
# セッション状態に保存されたメールアドレスを表示します。
st.write(f"セッションに保存されたメールアドレス: {st.session_state.user_email}") 


# ＊＊＊データフレームの状態管理＊＊＊
st.subheader('＊＊＊データフレームの状態管理＊＊＊')

# 'df' がセッション状態に存在しない場合、'商品' と '価格' を列名に持つ空のデータフレームを作成します。
if 'df' not in st.session_state: 
    st.session_state.df = pd.DataFrame(columns=['商品', '価格']) 

# 商品名を入力するためのテキスト入力欄を表示します。
product = st.text_input("商品名を⼊⼒") 
# 価格を入力するための数値入力欄を表示します。最小値は0に設定されています。
price = st.number_input("価格を⼊⼒", min_value=0) 

# "商品データを追加"ボタンがクリックされた場合の処理
if st.button("商品データを追加"): 
    # 入力された商品名と価格を新しいデータフレームに追加します。
    new_data = pd.DataFrame({'商品': [product], '価格': [price]}) 
    # セッション状態に保存されているデータフレームに、新しいデータフレームを結合します。
    st.session_state.df = pd.concat([st.session_state.df, new_data], ignore_index=True) 

# 現在の商品データを表示します。
st.write("現在の商品データ:") 
st.write(st.session_state.df) 

# "データをリセット"ボタンがクリックされた場合の処理
if st.button("データをリセット"): 
    # セッション状態のデータフレームを空のデータフレームにリセットします。
    st.session_state.df = pd.DataFrame(columns=['商品', '価格']) 
    # アプリを再実行して、リセットされたデータフレームを表示します。
    st.rerun() 