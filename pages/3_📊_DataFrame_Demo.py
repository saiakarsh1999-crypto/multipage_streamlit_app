import os
from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.dataframe` and `st.altair_chart` to visualize
Pandas DataFrames. Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx)."""
)


@st.cache_data
def get_un_data() -> pd.DataFrame:
    # First attempt local bundled data file
    local_path = os.path.join(os.path.dirname(__file__), "..", "data", "agri.csv.gz")
    if os.path.exists(local_path):
        return pd.read_csv(local_path).set_index("Region")
    # Fallback to remote AWS S3 data bucket
    aws_bucket_url = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    return pd.read_csv(aws_bucket_url + "/agri.csv.gz").set_index("Region")


try:
    df = get_un_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.subheader("Gross Agricultural Production ($B)")
        st.dataframe(data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(f"This demo requires internet access. Connection error: {e.reason}")
