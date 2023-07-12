def moon_weight(weight, increase):
    for year in range(1, 16):
        weight = weight + increase
        moon_weight = weight * 0.165
        print(f'Year {year} is {moon_weight:.3f}')

moon_weight(40, 0.5)