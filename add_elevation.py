import pandas as pd
import requests

# load dataset
df = pd.read_csv("training_data.csv")

# your location
lat = 18.52
lon = 73.85

# get elevation
url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"

response = requests.get(url).json()

elevation = response["results"][0]["elevation"]

# add elevation column
df["elevation"] = elevation

# save updated dataset
df.to_csv("training_data_with_elevation.csv", index=False)

print("Elevation added successfully")