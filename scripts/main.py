from mortality.mortality_table import MortalityTable
from mortality.mortality import Mortality
from finance.interest import Interest
from actuarial.actuarial_values import ActuarialValues
from insurance import WholeLifeAssurance

processedFilePath = r'data\processed\mortality_data.csv'


table = MortalityTable(r'data\processed\mortality_data.csv')

mortality = Mortality(table)

interest = Interest(0.05)

actuarialTools = ActuarialValues(mortality, interest)

whole = WholeLifeAssurance(actuarialTools)

print(whole.premium(88, "Male", 2024, 5000000))






