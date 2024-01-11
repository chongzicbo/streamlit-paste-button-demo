import streamlit as st
from utils import set_page_settings, display_linkedin_badge

set_page_settings()
st.sidebar.write("""
    Made in Streamlit with ❤️ by [Lucas Lopes](https://www.linkedin.com/in/o-lucas-lopes/)
    """)
display_linkedin_badge()

st.title('About')

st.write(
    """
    This is a demo of the `streamlit_paste_button` package. It allows you to paste an image from your clipboard into a Streamlit app with a button click.

    You can also customize the button label and style, as well as the error handling.
    """
)
st.write(
    """
    #### Browser requirements
    - The browser must support the Clipboard API.
    - Secure contexts (HTTPS) are required for clipboard access in most browsers.
    """
)
st.write('#### Demo source code')
st.code(
    '''
    import streamlit as st
    from streamlit_paste_button import paste_image_button

    paste_result = paste_image_button(
        label="📋 Paste an image",
        background_color="#FF0000",
        hover_background_color="#380909",
        errors='raise')

    if paste_result.image_data is not None:
        st.write('Pasted image:')
        st.image(paste_result.image_data)
    ''',
    language='python'
)