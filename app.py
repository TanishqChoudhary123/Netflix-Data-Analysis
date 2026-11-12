import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st


BACKGROUND = "#080B12"
CARD = "#0D111C"
COBALT = "#2457FF"
LIME = "#C6FF00"
WHITE = "#F5F7FA"
MUTED = "#9299A8"
BORDER = "#20283A"
CHART_COLORS = [COBALT, LIME]

st.set_page_config(
    page_title="Netflix Data Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

sns.set_theme(
    style="darkgrid",
    palette=CHART_COLORS,
    rc={
        "axes.facecolor": CARD,
        "figure.facecolor": CARD,
        "axes.edgecolor": BORDER,
        "axes.labelcolor": WHITE,
        "axes.titlecolor": WHITE,
        "text.color": WHITE,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "grid.color": BORDER,
        "grid.alpha": 0.65,
        "legend.facecolor": CARD,
        "legend.edgecolor": BORDER,
    },
)

st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
        --background-color: #080B12;
        --secondary-background-color: #0D111C;
        --text-color: #F5F7FA;
        --primary-color: #2457FF;
    }
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #080B12;
        color: #F5F7FA;
    }
    [data-testid="stHeader"] { background: #080B12; }
    [data-testid="stSidebar"] {
        background: #0D111C;
        border-right: 1px solid #20283A;
    }
    [data-testid="stSidebar"] > div:first-child { background: #0D111C; }
    .block-container {
        max-width: 1540px;
        padding: 2rem 2.3rem 3rem;
    }
    h1, h2, h3, h4 { color: #F5F7FA; letter-spacing: -0.025em; }
    p, label, li { color: #9299A8; }
    [data-testid="stCaptionContainer"] { color: #9299A8; }
    [data-testid="stMarkdownContainer"] a { color: #C6FF00; }
    .dashboard-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.5rem;
        padding: .3rem 0 1.4rem;
        margin-bottom: 1.4rem;
        border-bottom: 1px solid #20283A;
    }
    .brand-lockup { display: flex; align-items: center; gap: 1rem; }
    .brand-icon {
        display: grid;
        place-items: center;
        width: 3.1rem;
        height: 3.1rem;
        flex: 0 0 3.1rem;
        border: 1px solid #20283A;
        border-radius: 12px;
        background: #0D111C;
        color: #2457FF;
        font-size: 1.65rem;
    }
    .dashboard-header h1 {
        margin: 0;
        color: #F5F7FA;
        font-size: clamp(1.45rem, 2.6vw, 2rem);
        font-weight: 750;
        letter-spacing: -.04em;
    }
    .dashboard-header p {
        margin: .35rem 0 0;
        color: #9299A8;
        font-size: .92rem;
    }
    .dataset-status {
        display: inline-flex;
        align-items: center;
        gap: .55rem;
        padding: .55rem .8rem;
        border: 1px solid #20283A;
        border-radius: 999px;
        background: #0D111C;
        color: #F5F7FA;
        font-size: .78rem;
        font-weight: 650;
        white-space: nowrap;
    }
    .status-dot {
        width: .5rem;
        height: .5rem;
        border-radius: 50%;
        background: #C6FF00;
        box-shadow: 0 0 0 3px rgba(198, 255, 0, .12);
    }
    .sidebar-brand {
        padding: .4rem 0 1.1rem;
        border-bottom: 1px solid #20283A;
        margin-bottom: 1.1rem;
    }
    .sidebar-brand strong { color: #F5F7FA; font-size: 1rem; }
    .sidebar-brand span {
        display: block;
        margin-top: .3rem;
        color: #9299A8;
        font-size: .78rem;
    }
    .kpi-card {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: .65rem;
        height: 156px;
        min-height: 156px;
        padding: 1.05rem 1.15rem;
        border: 1px solid #20283A;
        border-radius: 12px;
        background: #0D111C;
        transition: border-color .18s ease, transform .18s ease;
    }
    .kpi-card > div:last-child { width: 100%; min-width: 0; }
    .kpi-card:hover {
        border-color: #2457FF;
        transform: translateY(-2px);
    }
    .kpi-icon {
        display: grid;
        place-items: center;
        width: 2.7rem;
        height: 2.7rem;
        flex: 0 0 2.7rem;
        border: 1px solid #20283A;
        border-radius: 10px;
        background: rgba(36, 87, 255, .12);
        color: #2457FF;
        font-size: 1.35rem;
    }
    .kpi-label { color: #9299A8; font-size: .82rem; margin-bottom: .35rem; }
    .kpi-value {
        color: #C6FF00;
        font-size: clamp(1.15rem, 1.8vw, 1.75rem);
        font-weight: 780;
        line-height: 1.15;
        letter-spacing: -.04em;
        white-space: nowrap;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: #20283A !important;
        border-radius: 12px;
        background: #0D111C;
    }
    [data-testid="stDataFrame"] {
        overflow: hidden;
        border: 1px solid #20283A;
        border-radius: 10px;
    }
    [data-testid="stDownloadButton"] button,
    [data-testid="stFormSubmitButton"] button {
        border: 1px solid #2457FF;
        border-radius: 8px;
        background: #2457FF;
        color: #F5F7FA;
        font-weight: 650;
        transition: background .18s ease, transform .18s ease;
    }
    [data-testid="stDownloadButton"] button:hover,
    [data-testid="stFormSubmitButton"] button:hover {
        background: #1747EA;
        border-color: #1747EA;
        transform: translateY(-1px);
    }
    [data-testid="stTextInput"] input,
    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div {
        background: #080B12;
        border-color: #20283A;
        color: #F5F7FA;
    }
    span[data-tag] {
        background: #2457FF !important;
        color: #F5F7FA !important;
        border-radius: 6px;
    }
    span[data-tag] span,
    span[data-tag] button { color: #F5F7FA !important; }
    [data-testid="stRadio"] label:has(input:checked) {
        color: #F5F7FA;
        font-weight: 700;
    }
    [data-testid="stRadio"] label:hover { color: #C6FF00; }
    [data-testid="stRadioOption"][data-selected="true"] > div > div:first-child {
        border-color: #2457FF !important;
    }
    [data-testid="stRadioOption"][data-selected="true"] > div > div:first-child > div {
        background: #2457FF !important;
    }
    [data-testid="stFileUploaderDropzone"] {
        background: #080B12;
        border: 1px dashed #20283A;
    }
    [data-testid="stFileUploaderDropzone"] button {
        border-color: #2457FF;
        background: #2457FF;
        color: #F5F7FA;
    }
    [data-testid="stProgressBar"] > div > div { background: #2457FF; }
    .section-eyebrow {
        color: #C6FF00;
        font-size: .72rem;
        font-weight: 750;
        letter-spacing: .13em;
        text-transform: uppercase;
        margin-bottom: .35rem;
    }
    @media (max-width: 800px) {
        .block-container { padding: 1.2rem 1rem 2rem; }
        .dashboard-header { align-items: flex-start; }
        .dataset-status { font-size: .7rem; padding: .45rem .6rem; }
    }
    @media (max-width: 520px) {
        .dashboard-header { flex-direction: column; gap: .8rem; }
        .brand-icon { width: 2.6rem; height: 2.6rem; flex-basis: 2.6rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_data(file):
    data = pd.read_csv(file)
    data = data.drop_duplicates().copy()
    data.columns = data.columns.str.strip()
    if "date_added" in data.columns:
        data["date_added"] = pd.to_datetime(
            data["date_added"].astype(str).str.strip(),
            errors="coerce",
        )
    text_cols = [
        "director",
        "cast",
        "country",
        "rating",
        "duration",
        "listed_in",
        "description",
    ]
    for col in text_cols:
        if col in data.columns:
            data[col] = data[col].fillna("Unknown")
    return data


def style_axis(ax):
    ax.set_facecolor(CARD)
    ax.set_axisbelow(True)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.xaxis.label.set_color(WHITE)
    ax.yaxis.label.set_color(WHITE)
    ax.title.set_color(WHITE)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(axis="y", color=BORDER, linewidth=0.7, alpha=0.8)


def show_chart(fig):
    st.pyplot(fig, width="stretch")
    plt.close(fig)


def plot_ranked(series, title, xlabel, ylabel, color=COBALT):
    fig, ax = plt.subplots(figsize=(8, 4))
    series.sort_values().plot(kind="barh", ax=ax, color=color, width=0.72)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    style_axis(ax)
    ax.grid(axis="x", color=BORDER, linewidth=0.7, alpha=0.8)
    ax.grid(axis="y", visible=False)
    show_chart(fig)


def split_counts(data, column):
    return (
        data.loc[data[column].notna() & (data[column] != "Unknown"), column]
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .loc[lambda values: values.ne("") & values.ne("Unknown")]
        .value_counts()
    )


def total_country_count(data):
    if "country" not in data.columns:
        return 0
    return len(split_counts(data, "country"))


def render_overview(data):
    st.markdown('<p class="section-eyebrow">At a glance</p>', unsafe_allow_html=True)
    st.subheader("Catalog overview")
    preview_col, missing_col = st.columns([1.5, 1], gap="large")
    with preview_col:
        with st.container(border=True):
            st.markdown("#### Recent titles")
            st.dataframe(data.head(), width="stretch", hide_index=True)
    with missing_col:
        with st.container(border=True):
            st.markdown("#### Missing values")
            missing = data.isnull().sum().sort_values(ascending=False)
            st.dataframe(
                missing.rename("Missing values").to_frame(),
                width="stretch",
                height=260,
            )

    st.markdown("#### Movies and TV shows")
    counts = data["type"].value_counts()
    left, right = st.columns(2, gap="large")
    with left:
        with st.container(border=True):
            fig, ax = plt.subplots(figsize=(7, 4))
            ax.bar(counts.index, counts.values, color=CHART_COLORS[: len(counts)])
            ax.set(title="Titles by format", xlabel="Content type", ylabel="Titles")
            style_axis(ax)
            ax.grid(axis="x", visible=False)
            show_chart(fig)
    with right:
        with st.container(border=True):
            fig, ax = plt.subplots(figsize=(7, 4))
            ax.pie(
                counts.values,
                labels=counts.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=CHART_COLORS[: len(counts)],
                textprops={"color": WHITE},
                wedgeprops={"linewidth": 2, "edgecolor": CARD},
            )
            ax.set_title("Catalog mix", color=WHITE)
            for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_color(WHITE)
            show_chart(fig)


def render_countries_genres(data):
    country_col, genre_col = st.columns(2, gap="large")
    with country_col:
        with st.container(border=True):
            st.markdown("#### Top 10 content-producing countries")
            if "country" in data.columns:
                countries = split_counts(data, "country").head(10)
                if not countries.empty:
                    plot_ranked(countries, "Titles by country", "Titles", "Country", LIME)
                    st.dataframe(
                        countries.rename("Titles").to_frame(),
                        width="stretch",
                    )
                else:
                    st.info("Country information is not available for these titles.")
            else:
                st.info("The dataset does not include a country column.")
    with genre_col:
        with st.container(border=True):
            st.markdown("#### Most common genres")
            if "listed_in" in data.columns:
                genres = split_counts(data, "listed_in").head(10)
                if not genres.empty:
                    plot_ranked(genres, "Titles by genre", "Titles", "Genre", COBALT)
                    st.dataframe(
                        genres.rename("Titles").to_frame(),
                        width="stretch",
                    )
                else:
                    st.info("Genre information is not available for these titles.")
            else:
                st.info("The dataset does not include a genre column.")


def render_time_trends(data):
    st.markdown("#### Content added to Netflix over the years")
    if "date_added" in data.columns:
        yearly = data["date_added"].dt.year.value_counts().sort_index().dropna()
        if not yearly.empty:
            with st.container(border=True):
                fig, ax = plt.subplots(figsize=(11, 4))
                ax.plot(
                    yearly.index,
                    yearly.values,
                    color=LIME,
                    marker="o",
                    markersize=4,
                    linewidth=2,
                )
                ax.fill_between(yearly.index, yearly.values, color=LIME, alpha=0.08)
                ax.set(
                    title="Titles added by year",
                    xlabel="Year added",
                    ylabel="Number of titles",
                )
                style_axis(ax)
                ax.grid(axis="x", visible=False)
                show_chart(fig)
        else:
            st.info("No valid date-added values were found in this selection.")
    else:
        st.info("The dataset does not include a date-added column.")

    st.markdown("#### Movie and TV show release years")
    release = data[data["release_year"].notna()].copy()
    release["release_year"] = pd.to_numeric(release["release_year"], errors="coerce")
    release = release[release["release_year"] >= 2000]
    by_year = release.groupby(["release_year", "type"]).size().unstack(fill_value=0)
    if not by_year.empty:
        with st.container(border=True):
            fig, ax = plt.subplots(figsize=(11, 4))
            colors = {
                kind: CHART_COLORS[index % len(CHART_COLORS)]
                for index, kind in enumerate(by_year.columns)
            }
            by_year.plot(ax=ax, marker=".", color=colors, linewidth=2)
            ax.set(
                title="Releases by year (2000 onwards)",
                xlabel="Release year",
                ylabel="Number of titles",
            )
            style_axis(ax)
            ax.grid(axis="x", visible=False)
            legend = ax.legend(frameon=False, labelcolor=WHITE)
            if legend:
                legend.get_frame().set_facecolor(CARD)
            show_chart(fig)
    else:
        st.info("No release-year data is available for this selection.")


def render_ratings_duration(data):
    if "rating" in data.columns:
        with st.container(border=True):
            st.markdown("#### Most common content ratings")
            ratings = data["rating"].value_counts().head(10)
            if not ratings.empty:
                plot_ranked(ratings, "Titles by rating", "Titles", "Rating", LIME)
            else:
                st.info("Rating information is not available for these titles.")

    st.markdown("#### Movie duration")
    if "duration" in data.columns:
        movies = data[data["type"] == "Movie"].copy()
        movies["duration_minutes"] = pd.to_numeric(
            movies["duration"].astype(str).str.extract(r"(\d+)")[0],
            errors="coerce",
        )
        durations = movies["duration_minutes"].dropna()
        if not durations.empty:
            chart_col, stats_col = st.columns([1.6, 1], gap="large")
            with chart_col:
                with st.container(border=True):
                    fig, ax = plt.subplots(figsize=(8, 4))
                    sns.histplot(
                        durations,
                        bins=30,
                        kde=True,
                        color=COBALT,
                        line_kws={"color": LIME, "linewidth": 2},
                        ax=ax,
                    )
                    ax.set(
                        title="Movie runtime distribution",
                        xlabel="Duration (minutes)",
                        ylabel="Number of movies",
                    )
                    style_axis(ax)
                    ax.grid(axis="x", visible=False)
                    show_chart(fig)
            with stats_col:
                with st.container(border=True):
                    st.markdown("#### Runtime summary")
                    summary = durations.describe().reindex(
                        ["count", "mean", "50%", "min", "max"]
                    )
                    summary.index = [
                        "Movies",
                        "Average (min)",
                        "Median (min)",
                        "Shortest (min)",
                        "Longest (min)",
                    ]
                    st.dataframe(
                        summary.round(1).rename("Value").to_frame(),
                        width="stretch",
                    )
        else:
            st.info("No movie duration values are available for this selection.")

    st.markdown("#### Number of seasons in TV shows")
    if "duration" in data.columns:
        shows = data[data["type"] == "TV Show"].copy()
        shows["seasons"] = pd.to_numeric(
            shows["duration"].astype(str).str.extract(r"(\d+)")[0],
            errors="coerce",
        )
        season_counts = shows["seasons"].value_counts().sort_index()
        if not season_counts.empty:
            with st.container(border=True):
                fig, ax = plt.subplots(figsize=(8, 4))
                season_counts.plot(kind="bar", ax=ax, color=COBALT, width=0.72)
                ax.set(
                    title="TV show seasons",
                    xlabel="Number of seasons",
                    ylabel="Number of TV shows",
                )
                style_axis(ax)
                ax.grid(axis="x", visible=False)
                show_chart(fig)
        else:
            st.info("No TV show season data is available for this selection.")


def render_data_explorer(data):
    if "director" in data.columns:
        with st.container(border=True):
            st.markdown("#### Top directors")
            directors = split_counts(data, "director").head(10)
            if not directors.empty:
                plot_ranked(directors, "Titles by director", "Titles", "Director", LIME)
                st.dataframe(
                    directors.rename("Titles").to_frame(),
                    width="stretch",
                )
            else:
                st.info("Director information is not available for these titles.")

    st.markdown("#### Search and inspect the cleaned dataset")
    table_col, search_col = st.columns([1.2, 1], gap="large")
    with table_col:
        selected_columns = st.multiselect(
            "Columns to display",
            options=list(data.columns),
            default=list(data.columns),
            key="table_columns",
        )
    with search_col:
        table_query = st.text_input(
            "Search this table",
            placeholder="Search title, director, country...",
            key="table_search",
        )

    explorer_data = data
    if table_query.strip():
        searchable = explorer_data.astype(str).agg(" ".join, axis=1)
        explorer_data = explorer_data[
            searchable.str.contains(table_query.strip(), case=False, na=False)
        ]
    if selected_columns:
        st.dataframe(
            explorer_data[selected_columns],
            width="stretch",
            hide_index=True,
            height=500,
        )
    else:
        st.info("Choose at least one column to display the dataset.")

    csv = data.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download cleaned CSV",
        csv,
        "netflix_cleaned.csv",
        "text/csv",
        type="primary",
    )


st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <strong>NETFLIX ANALYTICS</strong>
        <span>Catalog intelligence</span>
    </div>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.sidebar.file_uploader(
    "Upload a Netflix titles CSV",
    type=["csv"],
    help="Upload a Netflix titles CSV or use netflix_titles.csv beside app.py.",
)

try:
    with st.spinner("Loading and preparing the catalog..."):
        if uploaded_file is not None:
            all_data = load_data(uploaded_file)
        else:
            all_data = load_data("netflix_titles.csv")
except FileNotFoundError:
    st.info("Upload netflix_titles.csv in the sidebar, or place it beside app.py.")
    st.stop()
except Exception as error:
    st.error("The dataset could not be loaded. Check that the file is a valid CSV.")
    with st.expander("Technical details"):
        st.exception(error)
    st.stop()

required_columns = {"type", "title", "release_year"}
missing_columns = required_columns.difference(all_data.columns)
if missing_columns:
    st.error(
        "This file is missing required Netflix dataset columns: "
        + ", ".join(sorted(missing_columns))
    )
    st.stop()

all_data = all_data.copy()
all_data["release_year"] = pd.to_numeric(all_data["release_year"], errors="coerce")

st.markdown(
    """
    <header class="dashboard-header">
        <div class="brand-lockup">
            <div class="brand-icon" aria-hidden="true">🎬</div>
            <div>
                <h1>Netflix Data Analytics</h1>
                <p>Explore, Analyse &amp; Discover Content Trends</p>
            </div>
        </div>
        <div class="dataset-status"><span class="status-dot"></span>Dataset Loaded</div>
    </header>
    """,
    unsafe_allow_html=True,
)

navigation = [
    "Dashboard Overview",
    "Countries & Genres",
    "Time Trends",
    "Ratings & Duration",
    "Dataset Explorer",
]
st.sidebar.markdown("##### DASHBOARD")
selected_page = st.sidebar.radio(
    "Dashboard sections",
    navigation,
    label_visibility="collapsed",
)

st.sidebar.divider()
st.sidebar.markdown("##### FILTER DATA")
available_types = sorted(all_data["type"].dropna().unique())
selected_types = st.sidebar.multiselect(
    "Content type",
    options=available_types,
    default=available_types,
)
filtered_data = all_data[all_data["type"].isin(selected_types)].copy()

available_years = filtered_data["release_year"].dropna()
if not available_years.empty:
    min_year = int(available_years.min())
    max_year = int(available_years.max())
    selected_years = st.sidebar.slider(
        "Release year",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year),
        key="release_year_{}_{}".format(min_year, max_year),
    )
    filtered_data = filtered_data[
        filtered_data["release_year"].between(*selected_years)
        | filtered_data["release_year"].isna()
    ]

search_query = st.sidebar.text_input(
    "Search titles",
    placeholder="Title or description",
)
if search_query.strip():
    searchable = filtered_data["title"].fillna("").astype(str)
    if "description" in filtered_data.columns:
        searchable = searchable + " " + filtered_data["description"].fillna("").astype(str)
    filtered_data = filtered_data[
        searchable.str.contains(search_query.strip(), case=False, na=False)
    ]

st.sidebar.caption(
    "Showing {:,} of {:,} titles".format(len(filtered_data), len(all_data))
)

total_titles = len(all_data)
total_movies = int((all_data["type"] == "Movie").sum())
total_shows = int((all_data["type"] == "TV Show").sum())
total_countries = total_country_count(all_data)

kpi_columns = st.columns(4, gap="medium")
kpi_values = [
    ("▣", "Total Titles", total_titles),
    ("▶", "Total Movies", total_movies),
    ("▤", "Total TV Shows", total_shows),
    ("◎", "Total Countries", total_countries),
]
for column, (icon, label, value) in zip(kpi_columns, kpi_values):
    with column:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-icon" aria-hidden="true">{icon}</div>
                <div>
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value">{value:,}</div>
                </div>
            </div>
            """.format(icon=icon, label=label, value=value),
            unsafe_allow_html=True,
        )

st.write("")
if filtered_data.empty:
    st.info("No titles match the current filters. Adjust the sidebar to explore the catalog.")
else:
    if selected_page == "Dashboard Overview":
        render_overview(filtered_data)
    elif selected_page == "Countries & Genres":
        render_countries_genres(filtered_data)
    elif selected_page == "Time Trends":
        render_time_trends(filtered_data)
    elif selected_page == "Ratings & Duration":
        render_ratings_duration(filtered_data)
    else:
        render_data_explorer(filtered_data)

st.caption("Netflix Data Analytics · Python · Pandas · NumPy · Matplotlib · Seaborn · Streamlit")
