import streamlit as st
st.title("แอปพลิแคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year=st.number4_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
ce_year=bh_year-543
st.headet(f"ปี ค.ศ. คือ : {ce_year}")
