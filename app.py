import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image
st.write('''
        # Media Files
''')
st.write('''
## Image
''')
st.image(Image.open('istockphoto-521375354-612x612.jpg'))
st.write('''
### Video
''')
st.video(open('y2mate.com - Snow Leopards 101  Nat Geo Wild_v144P.mp4','rb'))
st.write('''
### Audio
''')
st.audio(open('Snow Leopard Chuffs with Inhale - QuickSounds.com.mp3','rb'))
st.markdown('Markdown')
st.title('Title')
st.header('Header')
st.text('Text')
df=sns.load_dataset('iris')
st.write(df.head())
# import libraries
import streamlit as st
import plotly.express as px
import pandas as pd
# import dataset
st.title("Plotly and Streamlit ko mila k app bnana")
df = px.data.gapminder() 
st.write(df)
# st.write(df.head())
st.write(df.columns)
# summary stat
st.write(df.describe())
# data management
year_option = df['year'].unique().tolist()
year = st.selectbox("which year should we plot?", year_option, 0)
# df = df[df['year']== year]
# plotting
fig = px.scatter(df, x= 'gdpPercap', y ='lifeExp', size='pop', color='continent', hover_name='continent',
                log_x=True, size_max=55, range_x=[100,100000], range_y=[20,90],
                animation_frame='year', animation_group='country')
fig.update_layout(width=800, height=600)
st.write(fig)