a=0
while a<5:
    income=int(input("Enter the gross income:"))
    dependent=int(input("Enter the number of dependents:"))
    taxable_income=income-10000-(3000*dependent)

    Tax=taxable_income*0.2
    print("The income tax is:$", Tax)