def fSalesTax(fAmount):
    fTax = 0.06
    fReturn = round(fAmount*fTax,2)
    return fReturn

def fTotal(fAmount,fTax):
    return round(fAmount+fTax,2)