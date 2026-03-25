# 📜 WP Sticker Automator

### Streamlining Government & Legal Document Labeling with Python

> In a high-volume GST Office, filing and labeling writ petitions is a critical — and painfully manual — task. This tool transforms raw CSV data into perfectly formatted, print-ready A4 sticker sheets in seconds.

---

## 🖼️ Visual Preview

When you upload your data, the app generates professional, standardized stickers formatted for A4 printing:

```
┌─────────────────────────────┐
│                             │
│    WP/1234/2024             │
│                             │
│    ABC Traders Pvt. Ltd.    │
│    vs Union of India        │
│                             │
│  (Bengaluru Commissionerate)│
│                             │
└─────────────────────────────┘
```

---

## 🚀 Features

- **Batch Processing** — Upload a CSV with hundreds of cases and generate stickers instantly
- **Print-Optimized** — Custom CSS ensures 3 stickers per A4 page with perfect margins
- **Zero Formatting Required** — Automatically handles font sizing and alignment
- **One-Click Printing** — Embedded "Print" button triggers the browser's native print engine

---

## 🛠️ Tech Stack

| Layer         | Technology                          |
|---------------|-------------------------------------|
| Language      | Python 3.x                          |
| Framework     | Streamlit                           |
| Data Handling | Pandas                              |
| Output        | Dynamic HTML/CSS (`@media print`)   |

---

## 📂 Data Mapping

The app automatically maps your office CSV headers to the sticker layout:

| CSV Header   | Sticker Field             | Style        |
|--------------|---------------------------|--------------|
| Case Number  | WP Number                 | 34px, Bold   |
| Party Name   | Petitioner vs Respondent  | 28px, Bold   |
| Location     | Commissionerate           | 24px, Italic |

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/skyeverseAI/csv-sticker-automator.git
cd csv-sticker-automator
```

### 2. Install dependencies

```bash
pip install streamlit pandas
```

### 3. Run the app

```bash
streamlit run app.py
```

### 4. Use it

1. Upload your CSV file
2. Download the generated HTML
3. Open in browser → Hit **Print**

> 💡 **Tip:** Set printer margins to **None** or **Minimum** for best results.

---

## 💡 Why This Exists

Big systems often overlook the *"last mile"* of bureaucracy — the physical paperwork.

This tool:

- ✅ Eliminates manual typing
- ✅ Ensures 100% formatting accuracy
- ✅ Standardizes the office filing system across cases

It's a 100-line proof that automation doesn't have to be complex to be impactful.

---

## 📄 License

MIT License — free to use, modify, and distribute.