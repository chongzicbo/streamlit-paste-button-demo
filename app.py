import streamlit as st
from streamlit_paste_button import paste_image_button


def main():
    st.set_page_config(
        page_title="Paste Button Demo",
        page_icon="📋"
    )

    st.title('Paste an image with a button click')

    st.write(
        """
        [![PyPI](https://img.shields.io/pypi/v/streamlit-paste-button)](https://pypi.org/project/streamlit-paste-button/)
        [![Documentation](https://img.shields.io/badge/Documentation%20-%20available%20-%208A2BE2)](https://github.com/olucaslopes/streamlit-paste-button)
        <a href="https://www.buymeacoffee.com/olucaslopes" target="_blank">
        <img align="right" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="125">
        </a>
        """,
        unsafe_allow_html=True
    )

    paste_result = paste_image_button(
        label="📋 Paste an image",
        background_color="#FF0000",
        hover_background_color="#380909",
        errors='raise')

    if paste_result.image_data is not None:
        st.write('Pasted image:')
        st.image(paste_result.image_data)


    st.write('#### Details')
    expander = st.expander('Click to expand', expanded=False)
    expander.write(
        """
        This is a demo of the `streamlit_paste_button` package. It allows you to paste an image from your clipboard into a Streamlit app with a button click.

        You can also customize the button label and style, as well as the error handling.
        """
    )
    expander.write(
        """
        #### Browser requirements
        - The browser must support the Clipboard API.
        - Secure contexts (HTTPS) are required for clipboard access in most browsers.
        """
    )
    expander.write('#### Demo source code')
    expander.code(
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

#TODO: leave the main page with just the button and create a about page with the rest of the info

if __name__ == "__main__":
    main()
