import pyinputplus as pyip

cost = 2.00
options = []

# Using inputMenu() for a bread type: wheat, white, or sourdough.
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], 'Please select the type of bread for your sandwich:\n')
if bread != 'white':
    cost += 0.50

# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], 'Please select the type of protein for your sandwich:\n')
if protein == 'Tofu':
    cost += 0.05

# Using inputYesNo() to ask if they want cheese.
cheese = pyip.inputYesNo('Would you like cheese? (y/n)\n')
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], 'Please select the type of bread for your sandwich:\n')
    cost += 0.50
    options.append(cheeseType)

# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
for c in ['Mayo', 'Mustard', 'Lettuce', 'Tomato']:
    if pyip.inputYesNo('Would you like %s? (y/n)\n' %(c)) == 'yes':
        options.append(c)

# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
number = pyip.inputInt('How many sandwiches would you like?\n', min=1)
if number > 1:
    sandwich = 'sandwiches'
else:
    sandwich = 'sandwich'

print('%s %s %s on %s with %s.' %(number, protein, sandwich, bread, ', & '.join([', '.join(options[:-1]),options[-1]])))
print('$%.2f' %(cost * number))