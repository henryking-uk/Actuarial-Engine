import pandas as pd

file = r'data\raw\nltuk198020223.xlsx'

# Read all sheets without assuming where the headers are
sheets = pd.read_excel(file, sheet_name=None, header=None)

all_data = []

for year, raw in sheets.items():

    # Skipping the non-data sheets
    if year == "Contents" or year == "Notes" or year == "Notation" or year == "Methodology":
        continue

    print(f"Processing: {year}")

    male = raw.iloc[5:, 0:6].copy()

    male.columns = [
        "age",
        "mx",
        "qx",
        "lx",
        "dx",
        "ex"
    ]

    male["sex"] = "Male"
    male["year"] = year

    female = raw.iloc[5:, 7:13].copy()

    female.columns = [
        "age",
        "mx",
        "qx",
        "lx",
        "dx",
        "ex"
    ]

    female["sex"] = "Female"
    female["year"] = year

    year_data = pd.concat(
        [male, female],
        ignore_index=True
    )

    all_data.append(year_data)

# Combine every year
mortality_data = pd.concat(
    all_data,
    ignore_index=True
)

# Put columns in the correct order
mortality_data = mortality_data[
    ["year", "sex", "age", "mx", "qx", "lx", "dx", "ex"]
]


# remove the intermitent colums which repeat top column and cast ages as integers
mortality_data = mortality_data[mortality_data["age"] != "age"]
mortality_data["age"] = mortality_data["age"].astype(int)

# Save to CSV
mortality_data.to_csv(
    "data\processed\mortality_data.csv",
    index=False
)

print("Mortality data successfully saved!")