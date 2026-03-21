import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-2.5-flash')
st.set_page_config(page_title='Thư viện động vật', page_icon=':library:', layout='wide')
st.title('Thu vien dong vat')
st.write('Hay chon 1 con vat, toi se hien thi thong tin con vat')
Con_vat = {
    'Con mèo': ['https://tiengdong.com/wp-content/uploads/Tieng-meo-keu-www_tiengdong_com.mp3'
, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFz5fYgrepcP696Zm4ZtlldGLC6hEr83HUhDcUWJoyK2l-Rqp2YrkMskunDA_R5Hy-722xpQrOgG2-ZhAuOhuQ1aBRtwaf4jp3tfRNlNQKmg&s=10', 'https://www.youtube.com/watch?v=2WKEAHaAfSc'],
    'Con chó': ['https://tiengdong.com/wp-content/uploads/Tieng-cho-sua-www_tiengdong_com.mp3'
,'https://img.freepik.com/vektoren-kostenlos/die-illustration-von-happy-cartoon-puppy_1308-166286.jpg?semt=ais_rp_progressive&w=740&q=80','https://www.youtube.com/watch?v=D0z6MLTsusA']}
cols = st.columns(len(Con_vat))
chon = None
for i, (con_vat, tinh_cach) in enumerate(Con_vat.items()):
    with cols[i]:
        if st.button(con_vat):
            chon = con_vat
if chon:
    with st.expander(chon):
        st.write('Âm thanh:')
        st.audio(Con_vat[chon][0],format='audio/mp3')
        st.write('Hình ảnh')
        st.image(Con_vat[chon][1],caption=chon)
        st.write('Video minh hoạ')
        st.video(Con_vat[chon][2],format='video/mp4')
        #AI
        st.write('viết giới thiệu bằng AI')
        prompt=f'Viết đoạn giới thiệu ngắn 200 từ , dễ hiểu , thú vị {chon} cho học sinh.'
        response = model.generate_content(prompt)
        st.write(response.text) 
        
