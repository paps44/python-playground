#if applicant has high income AND good credit
    #Eligible for loan
#the logical operator and is used to combine two conditions

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

#if applicant has high income OR good credit
    #Eligible for loan
#if one of the conditions is true the customer is eligible but if both are false customer will not be eligible

has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

# AND: operator both should true
# OR: at least one should be true
# NOT

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")