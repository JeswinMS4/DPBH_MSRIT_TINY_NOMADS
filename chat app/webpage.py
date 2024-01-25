import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:8501/')

# Access the 'users' collection in the 'streamlit' database
db = client['streamlit']
users = db['users']

def set_background(url):
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("%s");
        background-size: cover;
    }
    </style>
    ''' % url
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('https://wallpaperaccess.com/full/1129028.jpg')

options = ["About Us", "What are Dark Patterns?", "Be aware", "Feedback"]
page = st.sidebar.selectbox("Navigate:", options)


st.title("Tiny Nomads")

st.subheader("''Revealing and Resisting Dark Patterns in Digital Interfaces\n\n")



if page == "About Us":
    st.header("About Us")
    st.write("We are a team Tiny nomads! We created this app to raise awareness and educate users about the prevalence and impact of dark patterns in digital interfaces. We hope that by exposing and resisting these manipulative techniques, we can empower users to make informed and conscious choices online.")

    st.write("[GitHub](https://github.com/JeswinMS4/DPBH_MSRIT_TINY_NOMADS)")
    readme ='''We have developed a browser extension designed to detect various types of dark patterns on websites. The extension is currently capable of identifying static dark patterns such as Sneaking, Urgency, Misdirection, Social Proof, Scarcity, Obstruction, and Forced Action. Additionally, we plan to enhance our system by incorporating a Language Model (LLM) to classify these dark patterns based on contextual analysis. In the near future, our goal is to extend the detection capabilities to include dynamic dark patterns, utilizing information from both the URLs and screenshots of the current webpages. While we are currently focused on static dark pattern detection, we aim to evolve our solution to address the challenges posed by dynamic dark patterns.
    '''
    st.subheader("Our Approach")
    st.write(readme)
elif page == "What are Dark Patterns?":
    st.header("What are Dark Patterns?")
    st.write("Dark patterns are user interface design techniques that manipulate or deceive users into taking actions that they may not have intended. These patterns are often used in digital interfaces, websites, and apps to exploit cognitive biases and nudges, steering users towards choices that benefit the service provider rather than the user[^1^][3].")
    st.write("Some examples of dark patterns are:")
    st.write("- False urgency: creating a sense of scarcity or limited time offer to pressure users into making a purchase or signing up for a service.")
    st.write("- Basket sneaking: adding extra items or fees to the user's shopping cart without their consent or knowledge.")
    st.write("- Confirm shaming: using negative or guilt-inducing language to dissuade users from opting out of a service or offer.")
    st.write("- Subscription trap: making it difficult or impossible for users to cancel a subscription or service.")
    st.write("Dark patterns can have negative consequences for users, such as financial loss, privacy invasion, reduced autonomy, and decreased trust. They can also harm the reputation and credibility of the service provider, as well as violate ethical and legal standards.")
    st.write("To combat dark patterns, users need to be aware of their existence and effects, and be able to recognize and resist them. Service providers need to adopt ethical design principles and practices, and be transparent and accountable for their actions.")
elif page == "Be aware":
    st.header("Be aware of Dark Patterns")
    content='''

Read and Understand Terms of Service:
Before using a service or making a purchase, read the terms of service and privacy policy. Dark patterns often exploit users who don't take the time to review these documents.

*Watch for Pre-Selected Options:*
Be cautious of forms or checkboxes that have options pre-selected for you. Dark patterns might use this to trick you into accepting terms or services you didn't intend to.

Be Skeptical of Urgency and Scarcity:
Dark patterns often use urgency or scarcity tactics to pressure users into quick decisions. Take a moment to evaluate whether the urgency is genuine or an attempt to manipulate.

Check for Transparent Pricing:
When making a purchase, ensure that the pricing is transparent, and any additional fees are clearly disclosed. Watch out for hidden costs during the checkout process.

Look for Clear Cancellation Policies:
Services that make it difficult to cancel subscriptions or memberships may be using dark patterns. Check for clear and accessible cancellation policies.

Use Reputable Platforms:
Stick to reputable websites and platforms. Larger and well-established companies are generally less likely to use dark patterns, as their reputations are at stake.

Stay Informed and Share Knowledge:
Keep yourself informed about current issues related to dark patterns. Share your knowledge with friends and family to help them recognize and avoid manipulative tactics.

Report Dark Patterns:
If you come across websites or apps using dark patterns, consider reporting them. Some organizations and browser extensions allow users to report instances of deceptive design.

Use Browser Extensions:
Consider using browser extensions that help identify and block dark patterns. Some extensions are designed to highlight or prevent interactions with deceptive elements on websites.

By staying informed and being vigilant, you can better protect yourself from falling victim to dark patterns and make more conscious decisions online.'''
    st.write(content)
else:
    st.header("Feedback")
    st.write("We appreciate your feedback . Help us improve your experience.")
    ss=st.text_area("Website or App name:")
    em=st.text_input("Your Email (optional):")
    comments = st.text_area("Let us know if you come across any dark patterns ")
    submit = st.button("Submit")
    if submit:
        users.insert_one({'feedback': comments})
        st.success("Thank you for your feedback!")
