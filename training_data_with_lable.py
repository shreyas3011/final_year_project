import pandas as pd

df = pd.read_csv("training_data_with_elevation.csv")

# flood condition
df["flood"] = (
    (df["rainfall"] > 80) &
    (df["soil_moisture"] > 0.35)
).astype(int)

df.to_csv("training_data_with_flood.csv", index=False)

print("Flood column created")