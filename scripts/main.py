from mortality import MortalityTable

table = MortalityTable(r'data\processed\mortality_data.csv')



print(table.qx(30, "Male", 2026))
