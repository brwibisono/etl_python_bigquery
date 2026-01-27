# E-Commerce Data Analysis Project

This project is part of the **Data Analysis Final Project** and focuses on analyzing
an e-commerce public dataset to extract business insights and present them
through an interactive dashboard.

---

## 📦 Dataset

The project uses an **E-Commerce Public Dataset**, including:
- Orders
- Order items
- Payments
- Customers
- Products
- Product category translation

Product categories were normalized by translating Portuguese category names
into English as part of the data preparation process.

---

## 🔄 Data Analysis Workflow

The analysis follows an end-to-end data analytics process:

1. **Data Gathering**
   - Load raw CSV datasets

2. **Data Preparation**
   - Normalize product category names using translation mapping
   - Handle missing values
   - Prepare clean datasets for analysis

3. **Exploratory & Descriptive Analysis**
   - Analyze order volume and revenue trends
   - Evaluate product category performance
   - Perform customer analysis using RFM (Recency, Frequency, Monetary)

4. **Insight Generation**
   - Identify overall business performance trends
   - Understand customer purchasing behavior

5. **Dashboard Development**
   - Build an interactive dashboard using Streamlit
   - Visualize monthly orders and revenue trends

---

## 📊 Dashboard

The dashboard provides:
- Total Orders
- Total Revenue
- Average Orders per Month
- Average Revenue per Month
- Monthly trend visualization for orders and revenue
- Date range filter for flexible analysis

### Dashboard Preview
![Dashboard](./dashboard/dashboard.png)

---

## 🚀 How to Run the Dashboard

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the Streamlit app:
   ```bash
   streamlit run dashboard/dashboard.py

---

## 🗂️ Submission Structure

```
submissions
├── dashboard/
|   ├── dashboard.py
|   ├── dashboard.png
|   └── main_data.csv
├── data/                                          
|   ├── customers_dataset.csv
|   ├── order_items_dataset.csv
|   ├── order_payments_dataset.csv
|   ├── orders_dataset.csv
|   ├── product_category_name_translation.csv
|   ├── products_dataset_clean.csv
|   └── products_dataset.csv
├── 01_data_preparation.ipynb
├── 02_notebook.ipynb
├── 03_dashboard.ipynb
├── requirements.txt
└── README.md
```

---

## 📝 Notes
- The analysis is performed in a Colab Notebook (.ipynb)
- The dashboard script (.py) is designed to be executed in a local environment
- The dashboard screenshot is provided as part of the submission

---

## ✅ Conclusion

This project demonstrates the complete data analysis process,
from raw data preparation to insight delivery through an interactive dashboard.
```bash
  https://circuital-caitlyn-convolutely.ngrok-free.dev/
```
---

## ✍️ Author
**Bramantya Wibisono**

Submission Dicoding - Proyek Analisis Data

📧 **br.wibisono@gmail.com**





