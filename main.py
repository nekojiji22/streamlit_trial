import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image # 画像表示
import time # プログレスバーのところで

st.title('Streamlitだよ')

st.write('文字がでるよ')

df = pd.DataFrame({
    'x': [1,2,3,4],
    'y': [1,4,9,16]
})

st.write('write(df)')
st.write(df)
st.write('dataframe(df)')
st.dataframe(df.style.highlight_max(axis=0), width=300, height=600)
st.write('table(df)')
st.table(df.style.highlight_max(axis=0))

"""
# マークダウン
## 記法で
### かけます

```
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.latex(r'''
   a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
   a \left(\frac{1-r^{n}}{1-r}\right)
''')



st.write('ランダムなデータ')
df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)
st.write(df2)
st.line_chart(df2)


st.write('緯度経度')
df3 = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)



if st.checkbox('画像を表示する'):
    st.write('画像表示')
    img = Image.open('HIRAU_v01.png')
    st.image(img, caption='gazoudayo', use_column_width=True)

option = st.sidebar.selectbox(
    '好きな数字選択',
    list(range(1,11))
)
'好きな数字は', option, 'です。'


st.write('テキスト入力')
option2 = st.sidebar.text_input('ご趣味は？',value='ねこなでなで')
'趣味は', option2, 'です。'


tension = st.sidebar.slider('あなたのテンションは？', 0, 100, 50)
'テンションは', tension, '％です。'


left_column, right_column = st.columns(2)
button = left_column.button('表示する(ここは左コラム)')
if button:
    right_column.write('ばーん（ここは右コラム）')

expander = st.expander('問い合わせ')
toiawase = expander.text_input('ここに書いて')
expander.write(toiawase)


button_progress = st.button('プログレスバー')
latest_iteration = st.empty()
bar = st.progress(0)
if button_progress:
    'start!'
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.02)
    'finish!!'
