def standard_deduction(filing_status):
    if filing_status == "Single":
        deduction = 16100
    elif filing_status == "Married Filing Separately":
        deduction = 16100
    elif filing_status == "Head of Household":
        deduction = 24150
    elif filing_status == "Married Filing Jointly":
        deduction = 32200
    elif filing_status == "Surviving Spouse":
        deduction = 32200
    else:
        deduction = 0
        print("Invalid filing status")

    return deduction

def income_tax(income):
    if income <= 11925:
        tax = income * 0.10
    elif income <= 48475:
        tax = (11925 * 0.10) + ((income - 11925) * 0.12)
    elif income <= 103350:
        tax = (11925 * 0.10) + (36550 * 0.12) + ((income - 48475) * 0.22)
    elif income <= 197300:
        tax = (11925 * 0.10) + (36550 * 0.12) + (54875 * 0.22) + ((income - 103350) * 0.24)
    elif income <= 250525:
        tax = (11925 * 0.10) + (36550 * 0.12) + (54875 * 0.22) + (93950 * 0.24) + ((income - 197300) * 0.32)
    elif income <= 626350:
        tax = (11925 * 0.10) + (36550 * 0.12) + (54875 * 0.22) + (93950 * 0.24) + (53225 * 0.32) + ((income - 250525) * 0.35)
    else:
        tax = (11925 * 0.10) + (36550 * 0.12) + (54875 * 0.22) + (93950 * 0.24) + (53225 * 0.32) + (375825 * 0.35) + ((income - 626350) * 0.37)
    return tax

#def tax_return(withholding,tax):
    if withholding > tax:
        refund = withholding - tax
        print("Tax refund:", refund) 
    elif withholding < tax:
        amount_due = tax - withholding
        print("Tax due:", amount_due)
    else:
        print("No refund")