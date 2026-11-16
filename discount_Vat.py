import streamlit as st
st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")

price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.00 , value=0.00)
discountPercentage = st.number_input("กรอกส่วนลด (%):", min_value=0.00 , value=0.00)

discount = price * discountPercentage // 100

discounted = price - discount
vat = price * 0.07
netPrice = price - discount + vat

st.header(f"• ส่วนลด (**{discountPercentage}**%) : **{discounted:.2f}** บาท")
st.header(f"• ราคาหลังหักส่วนลด: **{discount:.2f}** บาท")
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิที่ต้องจ่าย: {netPrice:.2f} บาท")
st.divider()
st.write("นายชนากานต์ มหาวัน เลขที่ 23  ม.4/5")
