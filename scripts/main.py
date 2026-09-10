from actuarial_engine.mortality.mortality_table import MortalityTable
from actuarial_engine.mortality.mortality import Mortality
from actuarial_engine.finance.interest import Interest
from actuarial_engine.actuarial.actuarial_values import ActuarialValues
from actuarial_engine.insurance import WholeLifeAssurance

processedFilePath = r'data\processed\mortality_data.csv'


table = MortalityTable(r'data\processed\mortality_data.csv')

mortality = Mortality(table)

interest = Interest(0.05)

actuarialTools = ActuarialValues(mortality, interest)

whole = WholeLifeAssurance(actuarialTools)

print(whole.premium(88, "Male", 2024, 5000000))