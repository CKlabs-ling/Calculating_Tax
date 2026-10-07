from libary_tax import function_tax

income = float(input("Enter your gross income: "))
withholding = float(input("Enter your federal tax withheld: "))
filing_status = input("Enter your filing status: Single/Married Filing Separately/Head of Household/Married Filing Jointly/Surviving Spouse\n")

deduction = function_tax.standard_deduction(filing_status)
taxable_income = income - deduction
tax = function_tax.income_tax(taxable_income)
#tax_return = function_tax.tax_return(withholding,tax)

print("Taxable income:", taxable_income)
print("Tax:", tax)

if withholding > tax:
    refund = withholding - tax
    print("Tax refund:", refund) 
elif withholding < tax:
    amount_due = tax - withholding
    print("Tax due:", amount_due)
else:
    print("No refund")