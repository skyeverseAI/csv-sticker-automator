import streamlit as st
import pandas as pd

st.write("Hello from stickers!")

# -----------------------------
# HTML generator
# -----------------------------
def generate_html(cases):
    html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>WP Stickers</title>

<style>
@page {
    size: A4;
    margin: 1.5cm;
}

body {
    font-family: "Times New Roman", Times, serif;
}

.page {
    page-break-after: always;
}

.case-item {
    width: 15cm;
    height: 7.2cm;
    border: 3px solid #333;
    border-radius: 20px;
    margin: 0 auto 1.2cm auto;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;

    page-break-inside: avoid;
}

.wp-number {
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 14px;
}

.party-name {
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 12px;
    line-height: 1.25;
}

.commissionerate {
    font-size: 24px;
    font-style: italic;
}

@media print {
    button {
        display: none;
    }
}
</style>
</head>

<body>
<button onclick="window.print()">Print</button>
"""

    for i in range(0, len(cases), 3):
        html += '<div class="page">'
        for j in range(3):
            if i + j < len(cases):
                c = cases[i + j]
                html += f"""
<div class="case-item">
    <div class="wp-number">{c['wp_number']}</div>
    <div class="party-name">{c['party_name']}</div>
    <div class="commissionerate">({c['commissionerate']} Commissionerate)</div>
</div>
"""
        html += "</div>"

    html += "</body></html>"
    return html



# -----------------------------
# UI
# -----------------------------
st.title("WP Sticker Generator (CSV)")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    column_map = {
        "Case Number": "wp_number",
        "Party Name": "party_name",
        "Location": "commissionerate"
    }

    df = df.rename(columns=column_map)

    required = {"wp_number", "party_name", "commissionerate"}

    if not required.issubset(df.columns):
        st.error("CSV must have columns: wp_number, party_name, commissionerate")
    else:
        cases = df[list(required)].to_dict("records")
        st.success(f"{len(cases)} cases loaded")

        html = generate_html(cases)

        st.download_button(
            "Download Stickers HTML",
            html,
            "wp_stickers.html",
            "text/html"
        )

        st.dataframe(df)