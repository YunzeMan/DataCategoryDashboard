import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Show app title and description.
st.set_page_config(page_title="Task Category Score", page_icon="")
st.title("Task Category Score")
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

    # Make up some fake issue descriptions.
    issue_descriptions = [
        "Office Software",
        "Image Processing Software",
        "Audio Processing Software",
        "Video Processing Software",
        "Development Software",
        "Browser Software",
        "Entertainment Software",
        "Communication and Collaboration Software",
        "System Tools",
        "Network Tools",
        "Web Tools",
        "System Configuration",
    ]

    # Generate the dataframe with 100 rows/tickets.
    data = {
        "Task Category ID": [i for i in range(0, 12, 1)],
        "Task Category": issue_descriptions,
        "Credit Scale": ['100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%', '100%'],
        "Priority": ['High' for _ in range(12)],
        "Date Updated": [
            datetime.date(2025, 3, 20) for _ in range(12)
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

