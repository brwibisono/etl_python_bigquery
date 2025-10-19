CASE
    WHEN SAFE_CAST(mag AS FLOAT64) >= 7 THEN 'Major (≥7.0)'
    WHEN SAFE_CAST(mag AS FLOAT64) >= 6 THEN 'Strong (6.0-6.9)'
    WHEN SAFE_CAST(mag AS FLOAT64) >= 5 THEN 'Moderate (5.0-5.9)'
    WHEN SAFE_CAST(mag AS FLOAT64) >= 4 THEN 'Light (4.0-4.9)'
    ELSE 'Minor (<4.0)'
  END AS magnitude_class,
  CASE
    WHEN SAFE_CAST(depth_km AS FLOAT64) < 70 THEN 'Shallow (<70km)'
    WHEN SAFE_CAST(depth_km AS FLOAT64) < 300 THEN 'Intermediate (70-300km)'
    ELSE 'Deep (>300km)'
  END AS depth_class,