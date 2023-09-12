earned_income = float(input('Enter the amount of earned income in 2023: '))
print('Are you married or single?')
marital_status = input('Type m for married and s for single: ')

if marital_status == 's':
    if earned_income <= 11000:
        total_tax = earned_income * (10 / 100)
    elif earned_income <= 44725:
        total_tax = (11000 * (10 / 100)) + ((earned_income - 11000) * (12 / 100))
    elif earned_income <= 95375:
        total_tax = (11000 * (10 / 100)) + ((44725 - 11000) * (12 / 100)) + ((earned_income - 44725) * (22 / 100))
    elif earned_income <= 182100:
        total_tax = ((11000 * (10 / 100)) + ((44725 - 11000) * (12 / 100)) + ((95375 - 44725) * (22 / 100)) + (earned_income - 95375) * (24 / 100))

elif marital_status == 'm':
    if earned_income <= 22000:
        total_tax = earned_income * (10 / 100)
    elif earned_income <= 89450:
        total_tax = (22000 * (10 / 100)) + ((earned_income - 22000) * (12 / 100))
    elif earned_income <= 190750:
        total_tax = (22000 * (10 / 100)) + ((89450 - 22000) * (12 / 100)) + ((earned_income - 89450) * (22 / 100))
    elif earned_income > 190750:
        total_tax = ((22000 * (10 / 100)) + ((89450 - 22000) * (12 / 100)) + ((190750 - 89450) * (22 / 100)) + (earned_income - 190750) * (24 / 100))

else:
    print('Marital status error. Please choose "m" for married or "s" for single.')
    total_tax = 0

if total_tax > 0:
    print(f'This year you owe {total_tax:.2f} in taxes.')
