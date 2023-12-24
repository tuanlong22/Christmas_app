from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header 

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION_1 = ASSETS / "Animation1.json"
LOTTIE_ANIMATION_2 = ASSETS / "Animation2.json"
LOTTIE_ANIMATION = ASSETS / "animation_holiday.json"
LOTTIE_ANIMATION_3 = ASSETS / "animation3.json"

# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=16, falling_speed=7, animation_length="infinite")


# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]


# Page configuration
st.set_page_config(page_icon="🧑‍🎄")

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Merry Christmas, {PERSON_NAME}! 🎄", anchor=False)
colored_header(
        label="1. Giáng sinh đã đến với mọi nhà ",
        description="Christmas has come to everyone 💖💖💖",
        color_name="red-70",
    )
st.write("""
Giáng sinh là một ngày lễ vào ngày 25 tháng 12 kỷ niệm sự ra đời của Chúa Giê-su Ki-tô. Giáng sinh ngày càng trở nên phổ biến ở Việt Nam, đặc biệt là giới trẻ. Vào ngày này, mọi người thường trang trí nhà cửa và chuẩn bị quà, ... Mặc dù vậy, nhiều hộ gia đình ở các thành phố lớn vẫn mua cây thông Noel và treo đèn và chuông nhỏ trên đó. Trẻ em cũng rất thích ngày lễ Giáng sinh. Họ chuẩn bị đồ sạch để nhận quà từ ông già Noel.
             """)
# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION_1)
st_lottie(lottie_animation, key="lottie-holiday", height=300)

# Personalized holiday message
st.markdown(
    f"Dear {PERSON_NAME}, wishing you a wonderful holiday season filled with joy and peace. 🌟"
)

colored_header(
        label="2. Gửi những lời yêu thương đến người thân, người thương",
        description="Sending love to other people 💖💖💖",
        color_name="red-70",
    )
st.write("""
Trong ngày lễ Giáng sinh, mọi người giao tiếp với nhau bằng những cử chỉ, lời nói thân mật nhất. Điều này thể hiện sự lịch sự. Mọi người luôn luôn tin rằng điều này làm cuộc sống của họ hạnh phúc hơn. Trong lễ Giáng sinh, mọi người trang trí cây thông và nhà cửa rất đẹp.
""")
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION_3)
st_lottie(lottie_animation, key="lottie-holiday-3", height=300)
title = st.text_input('Gửi gắm những lời yêu thương: ', placeholder="Type here")
st.button("Gửi")
colored_header(
        label="3. Nghe những bản nhạc vào mùa lễ Giáng sinh",
        description="Listening to Christmas song 🎼🎼🎼",
        color_name="red-70",
    )
st.write("""
Giai điệu các bài hát Giáng sinh vang lên trong những ngày cuối năm dương lịch đem lại cảm giác náo nức và không khí ấm áp của mùa lễ hội. Trong không khí Giáng sinh, cùng thưởng thức những ca khúc hay nhất về ngày lễ đặc biệt này. Dưới đây là những bài hát Giáng sinh hay nhất mà bạn không nên bỏ qua.
""")
# option = st.selectbox(
#     'Lựa chọn bài hát 🎄🎄',
#     ('Mistletoe - Justin Beiber', 'Feliz Navidad - Boney M.', 'We Wish You A Merry Christmas - Crazy Frog', 'Jingle Bells - Boney M.', 'Last Christmas - Wham!', 'All I Want For Christmas Is You - Mariah Carey'))
if st.button("Bấm vào đây để nghe nhạc", type="secondary"):
    link = f"##### Playlist nhạc Giáng sinh hay nhất: [Danh sách phát](https://open.spotify.com/playlist/37i9dQZF1DX0Yxoavh5qJV)"
    st.markdown(link, unsafe_allow_html=True)
colored_header(
        label="4. Nhận quà từ Tuấn Long",
        description="Receive gift from Tun Long",
        color_name="red-70",
    )
st.write(
"""
Tặng quà là một trong những phong tục tuyệt vời nhất trong ngày Giáng sinh. Các món quà xinh xắn chúng ta có thể thể hiện tình yêu của mình đối với gia đình và bè bạn. Ðối với một số người quà Giáng sinh còn mang một ý nghĩa tôn giáo sâu đậm. Những món quà giúp cho mọi người nhớ lại ngày sinh của Chúa, là quà tặng của Chúa cho loài người.
"""
)
name = st.text_input("Nhập tên của bạn: ")
if st.button("Click here để nhận quà 🎁🎁", type="primary"):
    lottie_animation = load_lottie_animation(LOTTIE_ANIMATION_2)
    st_lottie(lottie_animation, key="lottie-holiday-2", height=300)
    st.markdown(
    f"Dear :red[{name}], wishing you a wonderful holiday season filled with joy and peace. 🌟"
    ) 














































