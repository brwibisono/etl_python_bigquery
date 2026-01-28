# Proyek Analisis Data – E-Commerce (2017–2018)

Proyek ini merupakan bagian dari **Submission Proyek Analisis Data Dicoding**.  
Tujuan proyek adalah menganalisis data e-commerce untuk menjawab pertanyaan bisnis
utama dan menyajikannya dalam bentuk **dashboard sederhana menggunakan Streamlit**.

---

## 🎯 Pertanyaan Bisnis

1. Kategori produk apa yang menjadi kontributor utama pendapatan bisnis selama 2017–2018?
2. Bagaimana tren pendapatan bisnis dari bulan ke bulan selama 2017–2018?

---

## 📦 Dataset

Proyek ini menggunakan **E-Commerce Public Dataset**, yang terdiri dari:
- Orders
- Order Items
- Payments
- Products
- Product Category Translation

Pada tahap *data cleaning*, nama kategori produk dinormalisasi dari bahasa Portugis
ke bahasa Inggris menggunakan dataset terjemahan kategori.

---

## 🔄 Alur Analisis

Proses analisis dilakukan dengan tahapan berikut:

1. **Assessing Data**  
   Pengecekan kelengkapan data, rentang waktu, dan konsistensi kolom utama.

2. **Cleaning Data**  
   Normalisasi nama kategori produk dan penanganan nilai kosong.

3. **Exploratory Data Analysis (EDA)**  
   - Analisis kontribusi pendapatan berdasarkan kategori produk  
   - Analisis tren pendapatan bulanan periode 2017–2018

4. **Data Preparation for Dashboard**  
   Pembuatan dataset agregasi:
   - `product_revenue.csv`
   - `main_data.csv`

5. **Visualization & Dashboard**  
   Visualisasi hasil analisis pada notebook dan dashboard Streamlit.

---

## 📊 Dashboard

Dashboard Streamlit menampilkan visualisasi yang **sama dengan notebook**, yaitu:
- Top kategori produk berdasarkan kontribusi pendapatan
- Tren pendapatan bisnis bulanan (2017–2018)

Dashboard hanya menggunakan dataset hasil agregasi tanpa melakukan analisis ulang.

---

## 🚀 Melihat Dashboard

1. Streamlit Cloud:
   ```bash
   https://brwibisono-dicodingsubmission2.streamlit.app/

---

## 🗂️ Struktur Submission

```
submissions
├── dashboard/
|   ├── dashboard.py
|   ├── main_data.csv
|   ├── product_revenue.csv
|   └── requirements.txt
├── data/                                          
|   ├── customers_dataset.csv
|   ├── order_items_dataset.csv
|   ├── order_payments_dataset.csv
|   ├── orders_dataset.csv
|   ├── product_category_name_translation.csv
|   ├── products_dataset_clean.csv
|   └── products_dataset.csv
├── Proyek_Analisi_Data.ipynb
├── requirements.txt
├── url.txt
└── README.md
```

---

## ✍️ Author
**Bramantya Wibisono**

Submission Dicoding - Proyek Analisis Data

📧 **br.wibisono@gmail.com**
