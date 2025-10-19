SELECT
  DATETIME(event_time, "Asia/Jakarta") AS waktu_wib,
  FORMAT_DATETIME('%H:%M', DATETIME(event_time, "Asia/Makassar")) AS waktu_wita,
  magnitude_class AS kategori_gempa,
  ROUND(depth_km, 2) AS kedalaman
FROM brbelajardata.data_gempa_indonesia.clean_data