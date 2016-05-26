'''
Tax Simulator 2017, funded by Futur Media
'''
Gross = 0.00
Owed = 0.00
Net = 0.00

In = input('How much money did you make the last year')
Gross = float(In)
Owed = Gross * 0.30

In = input('You will owe' + str(Owed) + 'Do you want to commit massive tax fraud? (yes or no)')

if In in ['yes','Yes','YES']:
    Owed = 0
    Net = Gross - Owed

if In in ['no','No','NO']:
    Net = Gross - Owed

print('Your net this year is' + str(Net))
    
