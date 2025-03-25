import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Show app title and description.
st.set_page_config(page_title="Task Category Score", page_icon="")
st.title("Task Collection Score & Priority") 
st.write(
    """
    This website shows how valuable each taks category is at the current status. 
    The task categories of higher priority requires more data, and thus will be rewarded with more credits.
    Please check this website regularly, because the credit scale and priority will change according to the data collection progress.
    """
)

# Create a random Pandas dataframe with existing tickets.
if "df" not in st.session_state:

    # Set seed for reproducibility.
    np.random.seed(42)

    # Data fields: Task Category, Credit Scale, Priority, Example Software
    issue_descriptions = [
        ["Office Software", 100, "High", ["Ubuntu LibreOffice", "Microsoft Office", "Google Docs"]],
        ["Image Processing Software", 100, "High", ["GIMP", "Photoshop"]],
        ["Video Processing Software", 100, "High", ["Adobe Premiere", "Kdenlive"]],
        ["Development and Coding Software", 100, "High", ["VSCode", "PyCharm", "Jupyter Notebook", ]],
        ["Browser Software", 100, "High", ["chrome", "firefox", "edge"]],
        ["Entertainment and Social Media Software", 100, "High", ["Spotify", "Discord", "X", "Steam"]],
        ["Collaboration and Email Software", 100, "High", ["Thunderbird", "email client", "slack", "zoom"]],
        ["Network Tools", 100, "High", ["VPN", "VNC", "AnyConnect"]],
        ["System Tools and Operating System Operation", 100, "High", ["Ubuntu VLC", "terminal", "file manager", "image viewer", "PDF viewer"]],
    ]
    categories_len = len(issue_descriptions)

    # Generate the dataframe with 100 rows/tickets.
    data = {
        "Task Category ID": [i for i in range(0, categories_len, 1)],
        "Task Category": [issue_descriptions[i][0] for i in range(0, categories_len, 1)],
        "Credit Scale": [issue_descriptions[i][1] for i in range(0, categories_len, 1)],
        "Priority": [issue_descriptions[i][2] for i in range(0, categories_len, 1)],
        "Example Software": [issue_descriptions[i][3] for i in range(0, categories_len, 1)],
        "Date Updated": [
            datetime.date(2025, 3, 25) for _ in range(categories_len)
        ],
    }
    df = pd.DataFrame(data)

    # Save the dataframe in session state (a dictionary-like object that persists across
    # page runs). This ensures our data is persisted when the app updates.
    st.session_state.df = df



# Show section to view and edit existing tickets in a table.
# st.header("Existing tickets")
# st.write(f"Number of tickets: `{len(st.session_state.df)}`")

# Show the tickets dataframe with `st.data_editor`. This lets the user edit the table
# cells. The edited data is returned as a new dataframe.
edited_df = st.data_editor(
    st.session_state.df,
    use_container_width=True,
    # use_container_height=True,
    hide_index=True,
    # Disable editing the ID and Date Submitted columns.
    disabled=["Task Category ID", "Task Category", "Credit Scale", "Priority", "Date Updated",]
)

