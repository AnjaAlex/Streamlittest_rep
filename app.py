import streamlit as st
import requests
st.image('piog.jpg', use_column_width=True)

 
st.title('Weather app')

#st.write('City_name')

city_name=st.text_input('Inserire la città')

if city_name:
    if st.button('weather check'):
        API_key="dfb9f2611380fcad47d78c9e15c20e7a"
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'

        result = requests.get(url)
        json = result.json()
        temp=round(json['main']['temp']-273.15)
        st.write('Temperatura:',temp)
        temp_max = round(json['main']['temp_max']-273.15)
        st.write('Temperatura max:', temp_max)
        temp_min = round(json['main']['temp_min']-273.15)
        st.write('Temperatura min:', temp_min)
        pressure = json['main']['pressure']
        st.write('Pressione:', pressure)
        humidity=json['main']['humidity']
        st.write('Humidity:', humidity)
        visibility = json['visibility']
        st.write('Visibility:', visibility)

    
# else: 
#     st.write('no data')
