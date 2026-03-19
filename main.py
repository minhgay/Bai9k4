import streamlit as st
st.set_page_config(page_title='Thu vien dong vat', page_icon=':library:', layout='wide')
st.title('Thu vien dong vat')
st.write('Hay chon 1 con vat, toi se hien thi thong tin con vat')
Con_vat = {
    'Con mèo': ['https://tiengdong.com/tieng-meo-keu?utm_source=copylink&utm_medium=share_button&utm_campaign=shared_from_tiengdong.com&utm_content=vi-18h34-19-03-2026', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFz5fYgrepcP696Zm4ZtlldGLC6hEr83HUhDcUWJoyK2l-Rqp2YrkMskunDA_R5Hy-722xpQrOgG2-ZhAuOhuQ1aBRtwaf4jp3tfRNlNQKmg&s=10', 'https://www.youtube.com/watch?v=2WKEAHaAfSc'],}
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
