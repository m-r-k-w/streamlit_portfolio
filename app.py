import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import time

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

st.text('----------------------------------------------------')
st.header('レッスン5:折れ線グラフ（plotly.graph_objectsの作成')

# サンプルデータ作成
data = {
    '月': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '売上': [100, 120, 140, 180, 200, 210],
    # '利益': [20, 25, 30, 40, 50, 55]
    '利益': [1, 5, 30, 40, 50, 55]
}
df = pd.DataFrame(data)

st.write('サンプルデータ:')
st.dataframe(df)

# 基本的な折れ線グラフの作成 
fig = go.Figure()
## fig.add_trace()を2回⾏って、売上と利益の2本の線を追加
fig.add_trace(go.Scatter(x=df['月'], y=df['売上'], mode='lines+markers', name='売上'))
fig.add_trace(go.Scatter(x=df['月'], y=df['利益'], mode='lines+markers', name='利益'))
fig.update_layout(title='月別売上と利益', xaxis_title='月', yaxis_title='⾦額（万円）')
st.plotly_chart(fig)

# カスタマイズされた折れ線グラフの作成 
fig = go.Figure() 
fig.add_trace(go.Scatter(x=df['月'], y=df['売上'], mode='lines+markers', 
name='売上', line=dict(color='blue', width=2))) 
fig.add_trace(go.Scatter(x=df['月'], y=df['利益'], mode='lines+markers', 
name='利益', line=dict(color='red', width=2))) 
 
fig.update_layout( 
    title='⽉別売上と利益の推移', 
    xaxis_title='月', 
    yaxis_title='⾦額（万円）', 
    font=dict(family="Meiryo", size=12), 
    legend=dict(orientation="h", yanchor="bottom", y=1.02, 
xanchor="right", x=1), 
    hovermode="x unified" 
) 
fig.update_xaxes(tickangle=45) 
fig.update_yaxes(zeroline=True, zerolinewidth=2, 
zerolinecolor='lightgrey') 
 
st.plotly_chart(fig) 

st.text('----------------------------------------------------')
st.header('レッスン6:棒グラフ（plotly.graph_objectsの作成')

# サンプルデータの作成 
data = { 
    '製品': ['A', 'B', 'C', 'D', 'E'], 
    '売上': [300, 400, 200, 600, 500], 
    '利益': [30, 60, 20, 100, 80] 
} 
df = pd.DataFrame(data) 

st.write('サンプルデータ:') 
st.dataframe(df) 

# 基本的な棒グラフの作成 
fig = go.Figure() 
fig.add_trace(go.Bar(x=df['製品'], y=df['売上'], name='売上')) 
fig.add_trace(go.Bar(x=df['製品'], y=df['利益'], name='利益')) 
 
fig.update_layout(title='製品別の売上と利益', 
                  xaxis_title='製品', 
                  yaxis_title='⾦額（万円）', 
                  barmode='group') 
 
st.plotly_chart(fig) 

# カスタマイズされた棒グラフの作成 
fig = go.Figure() 
fig.add_trace(go.Bar(x=df['製品'], y=df['売上'], name='売上', 
marker_color='blue')) 
fig.add_trace(go.Bar(x=df['製品'], y=df['利益'], name='利益', 
marker_color='red')) 
 
fig.update_layout( 
    title='製品別の売上と利益⽐較', 
    xaxis_title='製品', 
    yaxis_title='⾦額（万円）', 
    barmode='group', 
    font=dict(family="Meiryo", size=12), 
    legend=dict(orientation="h", yanchor="bottom", y=1.02, 
xanchor="right", x=1), 
    hovermode="x unified" 
) 
 
fig.update_traces(texttemplate='%{y}', textposition='outside') 
fig.update_yaxes(range=[0, max(df['売上'].max(), df['利益'].max()) * 1.1]) 
 
st.plotly_chart(fig) 

st.text('----------------------------------------------------')
st.header('レッスン7:円グラフ（plotly.graph_objectsの作成')

# サンプルデータの作成 
data = { 
    '商品': ['A', 'B', 'C', 'D', 'E'], 
    '売上': [300, 200, 180, 150, 120] 
} 
df = pd.DataFrame(data) 

st.write('サンプルデータ:') 
st.dataframe(df) 

# 基本的な円グラフの作成 
fig = go.Figure(data=[go.Pie(labels=df['商品'], values=df['売上'])]) 
fig.update_layout(title='商品別売上⽐率') 
st.plotly_chart(fig) 

# カスタマイズされた円グラフの作成 
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 
'lightcoral'] 
 
fig = go.Figure(data=[go.Pie(labels=df['商品'],  
                             values=df['売上'],  
                             hole=.3,  
                             marker=dict(colors=colors,  
                                         line=dict(color='#000000', 
width=2)))]) 
 
fig.update_traces(textposition='inside',  
                  textinfo='percent+label', 
                  hoverinfo='label+value+percent',  
                  textfont_size=14) 
 
fig.update_layout( 
    title='商品別売上⽐率（詳細版）', 
    font=dict(family="Meiryo", size=12), 
    legend=dict(orientation="h", yanchor="bottom", y=1.02, 
xanchor="right", x=1), 
    annotations=[dict(text='総売上', x=0.5, y=0.5, font_size=20, 
showarrow=False)] 
) 
 
st.plotly_chart(fig) 



st.header('***セクション3:パフォーマンスとセッション管理***')
st.header('レッスン8: キャッシュを使⽤したパフォーマンス最適化')
 
def generate_large_dataset():
    # ⼤きなデータセットを⽣成（約10秒かかる）
    data = pd.DataFrame(np.random.randn(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])
    return data
 
@st.cache_data
def load_data_cached():
    return generate_large_dataset()

def load_data_uncached():
    return generate_large_dataset()


st.subheader("キャッシュなしの場合")
start_time = time.time()
data_uncached = load_data_uncached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_uncached.head())
 
st.subheader("キャッシュありの場合")
start_time = time.time()
data_cached = load_data_cached()
end_time = time.time()
st.write(f"データ読み込み時間: {end_time - start_time:.2f} 秒")
st.write(data_cached.head())
 
st.write("キャッシュありの場合、2回⽬以降の読み込みは⾮常に⾼速になります。") 


st.header('キャッシュの無効化') 
@st.cache_data(ttl=10)
def get_current_time(): 
    return pd.Timestamp.now() 
 
st.subheader("キャッシュの無効化") 
st.write("現在時刻（10秒ごとに更新）:") 
st.write(get_current_time()) 