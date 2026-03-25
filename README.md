```
# 📜 WP Sticker Automator  
### Streamlining Government & Legal Document Labeling with Python

In a high-volume GST Office, filing and labeling writ petitions is a critical manual task. This tool transforms raw CSV data into perfectly formatted, print-ready A4 sticker sheets in seconds.

---

## 🖼️ Visual Preview

When you upload your data, the app generates professional, standardized stickers formatted for A4 printing:

> *(Example: Standardized layout with WP Number, Party Name, and Commissionerate)*

---

## 🚀 Features

- **Batch Processing**  
  Upload a CSV with hundreds of cases and generate stickers instantly.

- **Print-Optimized**  
  Custom CSS grid ensures 3 stickers per A4 page with perfect margins.

- **Zero Formatting Required**  
  Automatically handles font sizing and alignment for a professional look.

- **One-Click Printing**  
  Embedded "Print" button triggers the browser's native print engine.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Framework:** Streamlit  
- **Data Handling:** Pandas  
- **Output:** Dynamic HTML/CSS with `@media print` support  

---

## 📂 Data Mapping

The app automatically maps your office CSV headers to the sticker layout:

| CSV Header (System) | Sticker Field             | Style        |
|--------------------|--------------------------|--------------|
| Case Number        | WP Number                | 34px, Bold   |
| Party Name         | Petitioner vs Respondent | 28px, Bold   |
| Location           | Commissionerate          | 24px, Italic |

---

## ⚙️ Installation & Usage

### 1. Clone the repository
https://github.com/skyeverseAI/csv-sticker-automator.git
cd csv-sticker-automator  

### 2. Install dependencies
pip install streamlit pandas  

### 3. Run the app
streamlit run app.py  

### 4. Print
- Upload your CSV  
- Download the generated HTML  
- Hit Print
```