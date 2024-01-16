import streamlit as st
import streamlit.components.v1 as components

def set_page_settings():

    st.set_page_config(
        page_title="Paste Button Demo",
        page_icon="📋",
    )

    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "Navigation";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 90px;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.write(
        """
        [![PyPI](https://img.shields.io/pypi/v/streamlit-paste-button)](https://pypi.org/project/streamlit-paste-button/)
        [![Documentation](https://img.shields.io/badge/Documentation%20-%20available%20-%208A2BE2)](https://github.com/olucaslopes/streamlit-paste-button)

        <a href="https://www.buymeacoffee.com/olucaslopes" target="_blank">
        <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" width="150">
        </a><br><br>
        """,
        unsafe_allow_html=True
    )


def display_linkedin_badge(location="sidebar"):
    embed_component = {
        "linkedin": """
        <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="o-lucas-lopes" data-version="v1">
            <a class="badge-base__link LI-simple-link" href="https://br.linkedin.com/in/o-lucas-lopes?trk=profile-badge"></a>
        </div>
        """
    }

    if location == "sidebar":
        with st.sidebar:
            st.components.v1.html(embed_component["linkedin"], height=310)
    elif location == "page":
        st.components.v1.html(embed_component["linkedin"], height=310)
    else:
        raise ValueError("location must be 'sidebar' or 'page'")