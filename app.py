%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="🎬 Film Production Dashboard",
    page_icon="Å",
    layout="wide"
)

# -----------------------------
# High Contrast Style
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: #f5f6fa;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #111827 !important;
    }

    .hero {
        background: linear-gradient(135deg, #111827, #991b1b);
        padding: 2.2rem;
        border-radius: 24px;
        margin-bottom: 1.5rem;
        box-shadow: 0 18px 40px rgba(0,0,0,0.18);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        color: #ffffff !important;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        color: #fee2e2 !important;
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #111827 !important;
        margin-top: 1.3rem;
        margin-bottom: 0.8rem;
        border-left: 6px solid #dc2626;
        padding-left: 0.7rem;
    }

    /* Make all markdown headings black */
    .stMarkdown,
    .stMarkdown p,
    .stMarkdown span,
    .stMarkdown div,
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4,
    div[data-testid="stMarkdownContainer"],
    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3,
    div[data-testid="stMarkdownContainer"] h4 {
        color: #111827 !important;
    }

    div[data-testid="stMetric"] {
        background: #ffffff;
        border-radius: 18px;
        padding: 1rem;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }

    div[data-testid="stMetricLabel"] {
        color: #4b5563 !important;
        font-weight: 700;
    }

    div[data-testid="stMetricValue"] {
        color: #111827 !important;
        font-weight: 900;
    }

    div[data-testid="stMetricDelta"] {
        color: #dc2626 !important;
        font-weight: 700;
    }

    .good-card {
        background: #dcfce7;
        border-left: 6px solid #16a34a;
        padding: 1rem;
        border-radius: 14px;
        margin-bottom: 0.8rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    }

    .bad-card {
        background: #fee2e2;
        border-left: 6px solid #dc2626;
        padding: 1rem;
        border-radius: 14px;
        margin-bottom: 0.8rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    }

    .good-card h4,
    .good-card p,
    .good-card b,
    .bad-card h4,
    .bad-card p,
    .bad-card b {
        color: #111827 !important;
    }

    label {
        color: #111827 !important;
        font-weight: 700 !important;
    }

    input {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    .stTextInput input,
    .stNumberInput input {
        border-radius: 12px;
        border: 1px solid #d1d5db;
    }

    div[data-testid="stExpander"] {
        background: #ffffff;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        margin-bottom: 0.75rem;
        box-shadow: 0 8px 18px rgba(0,0,0,0.06);
    }

    div[data-testid="stExpander"] summary {
        color: #111827 !important;
        font-weight: 800;
    }

    .stCaptionContainer,
    .stCaptionContainer p {
        color: #4b5563 !important;
    }

    .stButton > button {
        border-radius: 999px;
        background: linear-gradient(135deg, #dc2626, #7f1d1d);
        color: white !important;
        border: none;
        font-weight: 800;
    }

    .stDownloadButton > button {
        border-radius: 999px;
        background: linear-gradient(135deg, #111827, #dc2626);
        color: white !important;
        border: none;
        font-weight: 800;
    }

    .stDataFrame {
        background: #ffffff;
        border-radius: 16px;
    }

    hr {
        border: none;
        height: 1px;
        background: #e5e7eb;
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="hero-title">🎬 Film Production Dashboard</div>
    <div class="hero-subtitle">
        A clear dashboard for analyzing movie budgets, revenues, genres, and ROI performance.
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Sample Data
# -----------------------------
if "films" not in st.session_state:
    st.session_state.films = pd.DataFrame([
        {
            "Title": "Inception",
            "Director": "Christopher Nolan",
            "Year": 2010,
            "Genre": "Sci-Fi",
            "Budget": 160000000,
            "Revenue": 839000000
        },
        {
            "Title": "Parasite",
            "Director": "Bong Joon-ho",
            "Year": 2019,
            "Genre": "Drama",
            "Budget": 11400000,
            "Revenue": 263000000
        },
        {
            "Title": "La La Land",
            "Director": "Damien Chazelle",
            "Year": 2016,
            "Genre": "Musical",
            "Budget": 30000000,
            "Revenue": 472000000
        },
        {
            "Title": "Titanic",
            "Director": "James Cameron",
            "Year": 1997,
            "Genre": "Romance",
            "Budget": 200000000,
            "Revenue": 2264000000
        },
        {
            "Title": "Everything Everywhere All at Once",
            "Director": "Daniel Kwan and Daniel Scheinert",
            "Year": 2022,
            "Genre": "Sci-Fi",
            "Budget": 25000000,
            "Revenue": 143000000
        }
    ])

# -----------------------------
# Calculation
# -----------------------------
def calculate_film_metrics(data):
    data = data.copy()
    data["Profit"] = data["Revenue"] - data["Budget"]
    data["ROI (%)"] = ((data["Profit"] / data["Budget"]) * 100).round(2)
    data["Performance"] = data["ROI (%)"].apply(
        lambda x: "Good ROI" if x >= 0 else "Bad ROI"
    )
    return data

df = calculate_film_metrics(st.session_state.films)

# -----------------------------
# Sidebar Input
# -----------------------------
with st.sidebar:
    st.header("➕ Add a Film")
    st.caption("Enter film production data below.")

    title = st.text_input("Film Title", placeholder="e.g. Interstellar")
    director = st.text_input("Director", placeholder="e.g. Christopher Nolan")
    year = st.number_input("Release Year", min_value=1900, max_value=2030, value=2024)

    genre = st.selectbox(
        "Genre",
        [
            "Action",
            "Drama",
            "Comedy",
            "Romance",
            "Sci-Fi",
            "Fantasy",
            "Thriller",
            "Horror",
            "Animation",
            "Musical",
            "Other"
        ]
    )

    budget = st.number_input(
        "Budget ($)",
        min_value=1,
        value=10000000,
        step=1000000
    )

    revenue = st.number_input(
        "Revenue ($)",
        min_value=0,
        value=50000000,
        step=1000000
    )

    if st.button("✅ Add Film", use_container_width=True):
        if title.strip() and director.strip():
            new_film = pd.DataFrame([{
                "Title": title,
                "Director": director,
                "Year": year,
                "Genre": genre,
                "Budget": budget,
                "Revenue": revenue
            }])

            st.session_state.films = pd.concat(
                [st.session_state.films, new_film],
                ignore_index=True
            )

            st.success(f"'{title}' has been added!")
            st.rerun()
        else:
            st.warning("Please enter both film title and director.")

df = calculate_film_metrics(st.session_state.films)

# -----------------------------
# Metrics
# -----------------------------
st.markdown('<div class="section-title">📊 Production Overview</div>', unsafe_allow_html=True)

total_budget = df["Budget"].sum()
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
avg_roi = df["ROI (%)"].mean()

m1, m2, m3, m4 = st.columns(4)

m1.metric("🎬 Total Films", len(df), delta="films in dataset")
m2.metric("💰 Total Budget", f"${total_budget:,.0f}", delta="production cost")
m3.metric("📈 Total Revenue", f"${total_revenue:,.0f}", delta=f"${total_profit:,.0f} profit")
m4.metric("🚀 Avg ROI", f"{avg_roi:.2f}%", delta="Good" if avg_roi >= 0 else "Needs improvement")

st.markdown("---")

# -----------------------------
# Film Performance Cards
# -----------------------------
st.markdown('<div class="section-title">🏆 Film Performance</div>', unsafe_allow_html=True)

for i, row in df.iterrows():
    card_class = "good-card" if row["ROI (%)"] >= 0 else "bad-card"
    status_icon = "🟢" if row["ROI (%)"] >= 0 else "🔴"

    st.markdown(f"""
    <div class="{card_class}">
        <h4>{status_icon} {row['Title']} ({row['Year']}) — {row['Genre']}</h4>
        <p>
            <b>Director:</b> {row['Director']} &nbsp; | &nbsp;
            <b>Budget:</b> ${row['Budget']:,.0f} &nbsp; | &nbsp;
            <b>Revenue:</b> ${row['Revenue']:,.0f} &nbsp; | &nbsp;
            <b>Profit:</b> ${row['Profit']:,.0f} &nbsp; | &nbsp;
            <b>ROI:</b> {row['ROI (%)']}%
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# Search and Filter
# -----------------------------
st.markdown('<div class="section-title">🔍 Search & Filter</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    search = st.text_input("Search by title or director", placeholder="Type film title or director...")

with f2:
    genre_filter = st.multiselect(
        "Filter by genre",
        options=sorted(df["Genre"].unique()),
        default=[]
    )

with f3:
    sort_by = st.selectbox(
        "Sort by",
        ["Revenue High to Low", "Budget High to Low", "ROI High to Low", "Year Newest", "Title A to Z"]
    )

df_filtered = df.copy()

if search:
    df_filtered = df_filtered[
        df_filtered["Title"].str.contains(search, case=False, na=False) |
        df_filtered["Director"].str.contains(search, case=False, na=False)
    ]

if genre_filter:
    df_filtered = df_filtered[df_filtered["Genre"].isin(genre_filter)]

if sort_by == "Revenue High to Low":
    df_filtered = df_filtered.sort_values("Revenue", ascending=False)
elif sort_by == "Budget High to Low":
    df_filtered = df_filtered.sort_values("Budget", ascending=False)
elif sort_by == "ROI High to Low":
    df_filtered = df_filtered.sort_values("ROI (%)", ascending=False)
elif sort_by == "Year Newest":
    df_filtered = df_filtered.sort_values("Year", ascending=False)
else:
    df_filtered = df_filtered.sort_values("Title", ascending=True)

st.caption(f"Showing {len(df_filtered)} film(s).")

# -----------------------------
# Data Table
# -----------------------------
st.markdown('<div class="section-title">📋 Film Data Table</div>', unsafe_allow_html=True)

st.dataframe(
    df_filtered,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Film Cards with Delete
# -----------------------------
st.markdown('<div class="section-title">🎞️ Film Cards</div>', unsafe_allow_html=True)

for i, row in df_filtered.reset_index().iterrows():
    original_index = row["index"]

    with st.expander(f"🎬 {row['Title']} — {row['Director']} ({row['Year']})"):
        c1, c2 = st.columns([4, 1])

        with c1:
            st.write(f"**Title:** {row['Title']}")
            st.write(f"**Director:** {row['Director']}")
            st.write(f"**Year:** {row['Year']}")
            st.write(f"**Genre:** {row['Genre']}")
            st.write(f"**Budget:** ${row['Budget']:,.0f}")
            st.write(f"**Revenue:** ${row['Revenue']:,.0f}")
            st.write(f"**Profit:** ${row['Profit']:,.0f}")
            st.write(f"**ROI:** {row['ROI (%)']}%")

        with c2:
            if st.button("🗑️ Delete", key=f"delete_{original_index}", use_container_width=True):
                st.session_state.films = (
                    st.session_state.films
                    .drop(index=original_index)
                    .reset_index(drop=True)
                )
                st.rerun()

st.markdown("---")

# -----------------------------
# Chart Helper
# -----------------------------
def clean_chart(fig):
    fig.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#111827"),
        title_font=dict(color="#111827"),
        legend_font=dict(color="#111827"),
        xaxis=dict(
            title_font=dict(color="#111827"),
            tickfont=dict(color="#111827"),
            gridcolor="#e5e7eb"
        ),
        yaxis=dict(
            title_font=dict(color="#111827"),
            tickfont=dict(color="#111827"),
            gridcolor="#e5e7eb"
        ),
        margin=dict(l=20, r=20, t=50, b=40)
    )
    return fig

# -----------------------------
# Charts
# -----------------------------
st.markdown("---")
st.markdown('<div class="section-title">📈 Film Data Visualization</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("<h3 style='color:#111827;'>💰 Budget vs Revenue</h3>", unsafe_allow_html=True)

    budget_revenue = df.melt(
        id_vars="Title",
        value_vars=["Budget", "Revenue"],
        var_name="Type",
        value_name="Amount"
    )

    fig1 = px.bar(
        budget_revenue,
        x="Title",
        y="Amount",
        color="Type",
        barmode="group",
        color_discrete_sequence=["#111827", "#dc2626"]
    )

    fig1.update_layout(
        xaxis_title="Film",
        yaxis_title="Amount ($)"
    )

    st.plotly_chart(clean_chart(fig1), use_container_width=True)

with c2:
    st.markdown("<h3 style='color:#111827;'>🎭 Genre Distribution</h3>", unsafe_allow_html=True)

    genre_count = df["Genre"].value_counts().reset_index()
    genre_count.columns = ["Genre", "Count"]

    fig2 = px.pie(
        genre_count,
        names="Genre",
        values="Count",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig2.update_layout(
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        font=dict(color="#111827"),
        title_font=dict(color="#111827"),
        legend_font=dict(color="#111827")
    )

    st.plotly_chart(fig2, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    st.markdown("<h3 style='color:#111827;'>🚀 ROI by Film</h3>", unsafe_allow_html=True)

    fig3 = px.bar(
        df.sort_values("ROI (%)", ascending=True),
        x="ROI (%)",
        y="Title",
        orientation="h",
        color="Performance",
        color_discrete_map={
            "Good ROI": "#16a34a",
            "Bad ROI": "#dc2626"
        },
        text="ROI (%)"
    )

    fig3.update_layout(
        xaxis_title="ROI (%)",
        yaxis_title=""
    )

    st.plotly_chart(clean_chart(fig3), use_container_width=True)

with c4:
    st.markdown("<h3 style='color:#111827;'>📅 Films by Release Year</h3>", unsafe_allow_html=True)

    year_count = df["Year"].value_counts().sort_index().reset_index()
    year_count.columns = ["Year", "Count"]

    fig4 = px.bar(
        year_count,
        x="Year",
        y="Count",
        color="Count",
        color_continuous_scale="Reds"
    )

    fig4.update_layout(
        xaxis_title="Year",
        yaxis_title="Number of Films"
    )

    st.plotly_chart(clean_chart(fig4), use_container_width=True)

# -----------------------------
# Download
# -----------------------------
st.markdown("---")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📤 Download Film Data as CSV",
    csv,
    "film_dashboard_data.csv",
    "text/csv",
    use_container_width=True
)
