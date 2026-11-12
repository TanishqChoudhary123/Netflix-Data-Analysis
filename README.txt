NETFLIX DATA ANALYSIS — BROWSER VERSION
========================================

This project opens as a local website in your browser using Streamlit.

FILES
-----
app.py             Main browser dashboard
requirements.txt   Required Python libraries
.streamlit\        Streamlit theme configuration

DATASET
-------
Download netflix_titles.csv from:
https://www.kaggle.com/datasets/shivamb/netflix-shows

Option A: Put netflix_titles.csv in the same folder as app.py.
Option B: Start the app and upload the CSV using the uploader on the page.

RUN IN VS CODE (WINDOWS)
------------------------
1. Extract this ZIP.
2. Open the extracted Netflix_Browser_Project folder in VS Code.
3. Open Terminal > New Terminal.
4. (Optional but recommended) Create and activate a virtual environment:

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

5. Install libraries:

   pip install -r requirements.txt

6. Start the browser app:

   streamlit run app.py

7. Your browser should open automatically at http://localhost:8501.
   If it does not, copy that address into Chrome or Edge.

DASHBOARD
---------
Use the sidebar to navigate between dashboard sections and filter by content
type and release year, or search titles and descriptions. In Dataset Explorer,
search the table and choose which columns to display. Charts, tables, and the
cleaned CSV download reflect the selected catalog filters.

STOP THE APP
------------
Click the terminal and press Ctrl + C.

NOTE
----
This is a local development website. It runs on your computer and is not
automatically published on the public internet.
