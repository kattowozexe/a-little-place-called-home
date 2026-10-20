import streamlit as st
if "opened" not in st.session_state:
    st.session_state["opened"] = False
st.markdown("""
<style>
    .stApp {
        background-color: #F4EFF7;
    }
        .stApp h1 {
    color: #B83D4B;
    }
        .stApp h2 {
    color: #B83D4B !important;
}
        st.App p {
    color: #B83D4B;
    }
    .stApp h1{
    text-align: center !important;
    width: 100%;
}
</style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center; padding: 35px 10px 20px;">
        <p style="font-size: 45px; margin-bottom: 0;">💌 ✨ 🌷</p>
        <h1 style="color: #B83D4B;">
            A Little Place Called Us
        </h1>
        <p style="font-size: 18px; color: #8F6AB8;">
            a tiny collection of memories, love, and gratitude ♡
        </p>
        <p style="font-size: 14px; color: #777;">
            made with love, for two very special people
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="A Little Place Called Us",
    page_icon="🌷",
)

st.markdown("""
<style>
/* Soft scrapbook background */
.stApp {
    background: linear-gradient(
        180deg,
        #FFF7F8 0%,
        #FFFDFB 50%,
        #FDF6FF 100%
    );
}

/* Floating hearts */
.heart {
    position: fixed;
    bottom: -40px;
    font-size: 24px;
    animation: floatUp 10s linear infinite;
    pointer-events: none;
    z-index: 999;
}

.heart:nth-of-type(1) {
    left: 10%;
    animation-delay: 0s;
}

.heart:nth-of-type(2) {
    left: 35%;
    animation-delay: 3s;
}

.heart:nth-of-type(3) {
    left: 65%;
    animation-delay: 1s;
}

.heart:nth-of-type(4) {
    left: 85%;
    animation-delay: 5s;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }
    15% {
        opacity: 0.7;
    }
    85% {
        opacity: 0.7;
    }
    100% {
        transform: translateY(-110vh) rotate(25deg);
        opacity: 0;
    }
}
    .stApp h1,
    .stApp h2,
    .stApp h3 {
    text-align: center !important;
    width: 100%;
}
    .stApp h1 {
    margin-left: auto;
    margin-right: auto;
}
</style>

<div class="heart">♡</div>
<div class="heart">💗</div>
<div class="heart">✧</div>
<div class="heart">♡</div>
""", unsafe_allow_html=True)

st.divider()

if st.button("Open our little scrapbook 💌"):
    st.session_state["opened"] = True

if st.session_state["opened"]:
    st.write("A little place to show appreciation to my fave people hehe")

    st.markdown("🎵 **A little soundtrack for our memories**")
    st.audio("music/background.mp3", format="audio/mp3")

    @st.dialog("A little memory 📸")
    def show_photo(photo_path, caption):
        st.image(photo_path, use_container_width=True)
        st.caption(caption)


if st.session_state["opened"]:
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/mm1.jpg", use_container_width=True)
        if st.button("🔍 Zoom in 1"):
            show_photo("images/mm1.jpg", "Ban SA iuu<3")

        st.image("images/mm3.jpg", use_container_width=True)
        if st.button("🔍 Zoom in 3"):
            show_photo("images/mm3.jpg", "samba cat keo")

    with col2:
        st.image("images/mm2.jpg", use_container_width=True)
        if st.button("🔍 Zoom in 2"):
            show_photo("images/mm2.jpg", "Organizer gang")

        st.image("images/mm4.jpg", use_container_width=True)
        if st.button("🔍 Zoom in 4"):
            show_photo("images/mm4.jpg", "Guider kho s1tg")

    tab_phuong, tab_ha = st.tabs(["Chị Phương 💌", "Chị Hạ 💌"])

    with tab_phuong:
     with st.expander("Open your letter"):
        st.markdown('<p style="color: #25212B;">Dear Phuong Pham</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #25212B;">Happy womens day chị Phươn nhoooo, em Win chỉ mong chị Phươn lúc nào cũng healthy, beautiful và perform well in academics nèee. Rất biết ơn Phươn Phạm lúc nào cũng quan tâm chăm sóc em Win nek hj, kể cả khi em bướng với ẩm ương vl. Cạm ơn Phươn Phạm đã put up và iu thương với đứa em ẩm ương này, iu Phươn nhắm nhắm my beautiful ghệ >< </p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #25212B;">Love from em Win <3</p>', unsafe_allow_html=True)

    with tab_ha:
         with st.expander("Open your letter"):
            st.markdown('<p style="color: #8F6AB8;">Dear Khanh Ha</p>', unsafe_allow_html=True)
            st.markdown('<p style="color: #8F6AB8;">Happy womens day chị Hạ nhoooo, em Win chỉ mong chị Hạ lúc nào cũng healthy, beautiful và không bị burnout vì chạy sự kiện nèee. Rất biết ơn Khánh Hạ lúc nào cũng quan tâm và đồng ý với chuyến đi xe hảdco của em Win nek hj. Cạm ơn Khánh Hạ đã chơi cùng và lắng nghe đứa em ẩm ương này, iu Hạ nhắm nhắm my người tình cắt kéo >< </p>', unsafe_allow_html=True)
            st.markdown('<p style="color: #8F6AB8;">Love from em Win <3</p>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(
        "<h3 style='text-align: center;'>💌 One last thing...</h3>",
        unsafe_allow_html=True
    )

    if st.button("💗 Open this little secret", use_container_width=True):
        st.session_state["secret_open"] = True

    if st.session_state.get("secret_open", False):
        st.markdown(
            """
            <div style="
                background-color: #FFF3F6;
                padding: 25px;
                border-radius: 15px;
                border: 1px solid #F2C6D2;
                text-align: center;
            ">
                <h3 style="color: #B83D4B;">For my favourite people ♡</h3>
                <p style="color: #25212B;">
                    The way we met was random, yet you two
                    managed to an unfamiliar place feel a little more like home for me.
                </p>
                <p style="color: #25212B;">
                    Thank you for being part of my little world. 💗
                </p>
                <p style="color: #B83D4B;">With love, always ♡</p>
            </div>
            """,
            unsafe_allow_html=True
        )
