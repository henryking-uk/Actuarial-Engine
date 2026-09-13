from actuarial_engine.mortality.mortality_table import MortalityTable
from actuarial_engine.mortality.mortality import Mortality
from actuarial_engine.finance.interest import Interest
from actuarial_engine.actuarial.actuarial_values import ActuarialValues
from actuarial_engine.actuarial.cashflow import Cashflow
from actuarial_engine.insurance import WholeLifeAssurance, InflationLinkedWholeLife, TermAssurance

processedFilePath = r'data\processed\mortality_data.csv'


table = MortalityTable(r'data\processed\mortality_data.csv', 2024)

mortality = Mortality(table)

interest = Interest(0.05)

actuarialTools = ActuarialValues(mortality, interest)

policy_inflation = InflationLinkedWholeLife(actuarialTools, 500000, 40, "Male", -0.03)
policy = WholeLifeAssurance(actuarialTools, 500000, 40, "Male")
term_policy = TermAssurance(actuarialTools, 500000, 40, "Male", 20)
term_policy_ = TermAssurance(actuarialTools, 500000, 40, "Male", 40)


#print(policy_inflation.premium())
#print(policy.premium())

print(term_policy.premium())
print(term_policy_.premium())




# cf = Cashflow(
#     100,
#     whole.premium(19, "Male", 2024, 500000),
#     "Premium",
# )

# print(cf.present_value(interest))#
# print(whole.premium(19, "Male", 2024, 500000))