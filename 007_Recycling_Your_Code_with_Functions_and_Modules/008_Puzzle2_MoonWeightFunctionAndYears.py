def moon_weight(weight, increase, years):
    years = years + 1
    for year in range(1, years):
        weight = weight + increase
        moon_weight = weight * 0.165
        print(f'Year {year} is {moon_weight:.3f}')

moon_weight(35, 0.3, 5)