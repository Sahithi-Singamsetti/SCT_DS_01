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

# Plot Population Trend
plt.figure(figsize=(10, 6))
sns.lineplot(x="Year", y="Population", data=df_india, marker="o", color="b")

plt.title(f"Population Trend of {country} Over Years")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid()
plt.show()
