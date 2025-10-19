
  SELECT *,
         ROW_NUMBER() OVER(PARTITION BY id ORDER BY ingested_at DESC) AS rn
  FROM brbelajardata.data_gempa_indonesia.raw_data
)
WHERE rn = 1;