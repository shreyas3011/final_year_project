import requests
import pandas as pd

locations = [
    ("Pune", 18.52, 73.85),
    ("Mumbai", 19.07, 72.87),
    ("Kerala", 10.85, 76.27),
    ("Shimla", 31.10, 77.17),
    ("Dehradun", 30.31, 78.03)
]

all_data = []

for name, lat, lon in locations:

    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date=2020-01-01&end_date=2024-01-01&daily=temperature_2m_mean,precipitation_sum,relative_humidity_2m_mean,pressure_msl_mean,soil_moisture_0_to_7cm_mean"

    response = requests.get(url).json()

    daily = response["daily"]

    df = pd.DataFrame({
        "location": name,
        "temperature": daily["temperature_2m_mean"],
        "rainfall": daily["precipitation_sum"],
        "humidity": daily["relative_humidity_2m_mean"],
        "pressure": daily["pressure_msl_mean"],
        "soil_moisture": daily["soil_moisture_0_to_7cm_mean"]
    })

    all_data.append(df)

final_df = pd.concat(all_data)

final_df.to_csv("training_data.csv", index=False)

print("Dataset size:", len(final_df))