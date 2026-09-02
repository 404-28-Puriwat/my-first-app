import time
import streamlit as st
st.title("⏱️ เกมเติมศัพท์จับเวลา")

if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2\
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog
# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()

 # ตรวจข้อ 1
if u_ans1 == "apple":
    print("Correct!")
    print("Wrong!")
       if u_ans1 == "apple":
    st.success("✅ ข้อ 1: ถูกต้อง")
else:
    st.error("❌ ข้อ 1: ไม่ถูกต้อง")
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")
  # ตรวจข้อ 2
  if u_ans2 == "fish":
   st.success("✅ ข้อ 2: ถูกต้อง")
   score += 1
 else:
      st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
 # ตรวจข้อ 3
  if u_ans3 == "Banana":
   st.success("✅ ข้อ 3: ถูกต้อง")
   score += 3
 else:
     st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
    # ตรวจข้อ 4
    if u_ans4 == "pen":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 4
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

 if score == 2:
        st.success("🎉 You win!")
    else:
      st.error("💀 You lose!")

# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: I want to eat a `B _ n _ n _`. 🍌",
    value=st.session_state.ans1_val,
)
ans4 = st.text_input(
    "ข้อ 4: I need a `p _ n` for writing. 🖊️ ",
    value=st.session_state.ans2_val,
)

f "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)

    st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
st.write("นายภูริวัฒน์ สุทัศนรักษ์ เลขที่ 28 ม.4/4")
