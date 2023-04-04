from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

##
st.set_page_config(page_title="My Webpage",page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css.txt")



# load set
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5yDOjriyKd.json")
img = Image.open("images/nail.png")
img_nails = Image.open("images/nails2.png")

# header section
with st.container():
    st.subheader("Hi, welcome to “Raey’s store & self care beauty salon”:wave:")
    st.title("A Nail Stylist")
    st.write(
        "I am passionate about making it easy and safer to have pretty nails on and still keeping our natural nails "
        "safe and reduce natural nails damages.Pressons: Stress free ways to get nails done good to go in minutes "
        "and very reliable for impromptu occasions/events")
    st.write("[Learn More>](https://instagram.com/raey_nails?igshid=YmMyMTA2M2Y)")

# what I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
            """
            Self-care beauty salon
   We are passionate about relaxing the mind & body of the individual and helping to boost their self
    esteem thus making the individual more vibrant after our services. 
    Our services includes facials, manicure and pedicure, body massage, waxing. 
    Our online store
We make it easy to get sold items here by offering door-to-door delivery services.
-Luxury accessories 
-Affordable accessories 
-Nail art materials/ nail art supplies 
-Lashes materials 
-Hair accessories etc.
            
            If it sounds interesting to you, consider my services
            """
        )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")
    # ----projects ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My services")
        st.write("##")
        st.write(
            """ 
We offer beauty services, luxury manicure & pedicure treatments to people and we run an online store for nail art supplies,
 accessories, lashes materials etc
            """
        )

    with st.container():
        st.write("---")
        st.header("My Products")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img)

    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_nails)

            ## contact
            with st.container():
                st.write("---")
                st.header("Contact Me!")
                st.write("##")

            # documentation
            contact_form = """
             <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
           
            
            
