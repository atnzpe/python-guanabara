income = 250_000

lowtaxland_rate = 0.05
ripoffland_rate = 0.43

print(
    'Your income is',income,'and you would pay',lowtaxland_rate*income,'income tax in Lowtaxland or',ripoffland_rate,'income tax in Ripoffland. You would save',(income * ripoffland_rate)-(income * lowtaxland_rate),"by paying taxes in Lowtaxland!\n\nYour solution must replace the curly brackets (e.g.",income,") with the actual values (e.g. 250000). The values must be calculated correctly. The tax amount should be calculated as",income * lowtaxland_rate,"for Lowtaxland, and",income * ripoffland_rate,"for Ripoffland, respectively.",)
