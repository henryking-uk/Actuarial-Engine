from actuarial_engine.mortality.mortality_table import MortalityTable
from actuarial_engine.mortality.mortality import Mortality
from actuarial_engine.finance.interest import Interest
from actuarial_engine.actuarial.actuarial_values import ActuarialValues
from actuarial_engine.actuarial.cashflow import Cashflow
from actuarial_engine.insurance import WholeLifeAssurance, InflationLinkedWholeLife, TermAssurance
from actuarial_engine.client import Client

processedFilePath = r'data\processed\mortality_data.csv'


table = MortalityTable(r'data\processed\mortality_data.csv', 2024)

mortality = Mortality(table)

interest = Interest(0.05)

actuarialTools = ActuarialValues(mortality, interest)

client = Client(40, "Male")

policy_term = TermAssurance(actuarialTools, 500000, client, 40)

print(policy_term.premium())