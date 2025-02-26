import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path
file_path = r"C:\Users\sahit\OneDrive\Documents\SkillCraft Internship\Task1\API_SP.POP.TOTL_DS2_en_csv_v2_87\API_SP.POP.TOTL_DS2_en_csv_v2_87.csv"

# Load dataset and skip metadata rows
df = pd.read_csv(file_path, skiprows=4)

# Drop irrelevant columns
df = df.drop(columns=["Indicator Name", "Indicator Code", "Unnamed: 68"], errors="ignore")

# Convert data to long format (melt)
year_columns = df.columns[2:]  # Only numeric year columns
df_melted = df.melt(id_vars=["Country Name", "Country Code"], 
                    value_vars=year_columns, 
                    var_name="Year", 
                    value_name="Population")

# Convert Year column to integer
df_melted = df_melted[df_melted["Year"].str.isnumeric()]  # Keep only numeric years
df_melted["Year"] = df_melted["Year"].astype(int)

# Filter for a specific country (e.g., India)
country = "India"
df_india = df_melted[df_melted["Country Name"] == country]

# Plot Population Trend as a Bar Chart
plt.figure(figsize=(12, 6))
sns.barplot(x="Year", y="Population", data=df_india, color="blue")

plt.title(f"Population Trend of {country} Over Years", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Population", fontsize=12)
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

# Customizing Grid Line Color
plt.grid(axis="y", linestyle="--", linewidth=0.7, color="red")  # Grid lines are now red

plt.show()
