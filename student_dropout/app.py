import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="🎓 Prediksi Dropout Mahasiswa",
    layout="wide"
)

st.title("🎓 Prediksi Dropout Mahasiswa")
st.markdown("Dashboard interaktif untuk memprediksi risiko mahasiswa dropout by Bramantya Wibisono")

# LOAD MODEL
model = joblib.load("student_dropout/model/student_dropout_model.pkl")
feature_columns = joblib.load("student_dropout/model/model_features.pkl")

# TABS
tab1, tab2 = st.tabs(
    ["🔍 Prediksi Individu", "📊 Prediksi Batch"]
)

# TAB 1 — PREDIKSI INDIVIDU
with tab1:

    st.subheader("📝 Input Profil Mahasiswa")

    col1, col2 = st.columns(2)

    input_data = {}

    with col1:
        input_data["Admission_grade"] = st.number_input(
            "Nilai Masuk", 0.0, 200.0, 120.0
        )

        input_data["Age_at_enrollment"] = st.number_input(
            "Usia Saat Pendaftaran", 15, 60, 20
        )

        input_data["Tuition_fees_up_to_date"] = st.selectbox(
            "Status Pembayaran UKT",
            [1, 0],
            format_func=lambda x: "Lunas" if x == 1 else "Belum Lunas"
        )

        input_data["Scholarship_holder"] = st.selectbox(
            "Penerima Beasiswa",
            [1, 0],
            format_func=lambda x: "Ya" if x == 1 else "Tidak"
        )

    with col2:
        input_data["Debtor"] = st.selectbox(
            "Status Hutang",
            [1, 0],
            format_func=lambda x: "Punya Hutang" if x == 1 else "Tidak Punya Hutang"
        )

        input_data["Curricular_units_1st_sem_approved"] = st.number_input(
            "Jumlah Matkul Lulus Semester 1", 0, 20, 5
        )

        input_data["Curricular_units_1st_sem_grade"] = st.number_input(
            "Nilai Semester 1", 0.0, 20.0, 12.0
        )

        input_data["Curricular_units_2nd_sem_grade"] = st.number_input(
            "Nilai Semester 2", 0.0, 20.0, 12.0
        )

    # Build dataframe input
    input_df = pd.DataFrame(
        [np.zeros(len(feature_columns))],
        columns=feature_columns
    )

    for col, value in input_data.items():
        if col in input_df.columns:
            input_df[col] = value

    # Tombol prediksi
    if st.button("🚀 Prediksi Risiko Dropout", use_container_width=True):

        probability = model.predict_proba(input_df)[0][1]
        probability_pct = probability * 100

        st.divider()
        st.subheader("📊 Hasil Analisis Risiko")

        col_left, col_right = st.columns([1, 1])

        # KIRI — GAUGE CHART
        with col_left:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=probability_pct,
                number={"suffix": "%"},
                title={"text": "Probabilitas Dropout"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "black"},
                    "steps": [
                        {"range": [0, 30], "color": "#d4edda"},
                        {"range": [30, 60], "color": "#fff3cd"},
                        {"range": [60, 100], "color": "#f8d7da"}
                    ]
                }
            ))

            fig_gauge.update_layout(height=350)

            st.plotly_chart(fig_gauge, use_container_width=True)

        # KANAN — STATUS + BAR CHART
        with col_right:

            st.metric(
                "Probabilitas Prediksi",
                f"{probability_pct:.2f}%"
            )

            if probability >= 0.7:
                st.error("🚨 Risiko Sangat Tinggi")
            elif probability >= 0.5:
                st.warning("⚠️ Risiko Tinggi")
            elif probability >= 0.3:
                st.info("🔍 Risiko Sedang")
            else:
                st.success("✅ Risiko Rendah / Aman")

            # Faktor risiko visual
            risk_factors = {
                "Pembayaran": 100 if input_data["Tuition_fees_up_to_date"] == 0 else 20,
                "Hutang": 100 if input_data["Debtor"] == 1 else 20,
                "Nilai Sem 1": max(0, 100 - input_data["Curricular_units_1st_sem_grade"] * 5),
                "Nilai Sem 2": max(0, 100 - input_data["Curricular_units_2nd_sem_grade"] * 5)
            }

            risk_df = pd.DataFrame({
                "Faktor": list(risk_factors.keys()),
                "Skor Risiko": list(risk_factors.values())
            })

            fig_bar = px.bar(
                risk_df,
                x="Faktor",
                y="Skor Risiko",
                title="Faktor Risiko Utama"
            )

            st.plotly_chart(fig_bar, use_container_width=True)

        # REKOMENDASI
        st.markdown("### 🧠 Rekomendasi Tindakan")

        if probability >= 0.5:
            st.warning(
                """
                Disarankan intervensi akademik segera:
                - mentoring dengan dosen pembimbing
                - follow-up pembayaran UKT
                - evaluasi performa semester
                """
            )
        else:
            st.success(
                """
                Mahasiswa saat ini berada pada kategori aman.
                Tetap lakukan monitoring berkala.
                """
            )

# TAB 2 — PREDIKSI BATCH
with tab2:

    st.subheader("📂 Upload CSV untuk Prediksi Batch")

    uploaded_file = st.file_uploader(
        "Upload file CSV",
        type=["csv"]
    )

    if uploaded_file is not None:
        batch_df = pd.read_csv(uploaded_file, sep=";")

        st.dataframe(batch_df.head())

        batch_input = batch_df[feature_columns]

        batch_prob = model.predict_proba(batch_input)[:, 1]
        batch_pred = np.where(
            batch_prob >= 0.5,
            "Risiko Tinggi",
            "Risiko Rendah"
        )

        batch_df["Probabilitas_Dropout"] = batch_prob
        batch_df["Prediksi"] = batch_pred

        st.dataframe(batch_df.head())

        csv_result = batch_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download Hasil Prediksi",
            csv_result,
            "hasil_prediksi_batch.csv",
            "text/csv"
        )
