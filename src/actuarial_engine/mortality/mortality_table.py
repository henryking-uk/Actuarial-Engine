import pandas as pd


class MortalityTable:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def _get_row(self, age, sex, year):
        self._validate_inputs(age, sex, year)
        row = self.data[
            (self.data["year"] == f"{year - 2}-{year}") &
            (self.data["sex"] == sex) &
            (self.data["age"] == age) 
        ]

        if len(row) != 1:
            raise ValueError("No unique mortality table row found for these inputs.")

        return row

    def _validate_inputs(self, age, sex, year):
        if sex not in ("Male", "Female"):
            raise ValueError("Invalid sex. Must be 'Male' or 'Female'.")
        if age not in range(0, 101):
            raise ValueError("Invalid age. Must be between 0 - 100 inclusive.")
        if year not in range(1982, 2025):
            raise ValueError("Invalid year. Must be between 1982 - 2024 inclusive.")

    def mx(self, age, sex, year):
        """Central mortality rate at a given age."""

        row = self._get_row(age, sex, year)
        return row["mx"].iloc[0]

    def qx(self, age, sex, year):
        """Probability of dying between age x and age x+1."""

        row = self._get_row(age, sex, year)
        return row["qx"].iloc[0]

    def lx(self, age, sex, year):
        """Number of people alive at exact age x."""
        row = self._get_row(age, sex, year)
        return row["lx"].iloc[0]

    def dx(self, age, sex, year):
        """Number of people dying between age x and age x+1."""
        row = self._get_row(age, sex, year)
        return row["dx"].iloc[0]

    def ex(self, age, sex, year):
        """Expected remaining lifetime at a given age."""
        row = self._get_row(age, sex, year)
        return row["ex"].iloc[0]


    
