def solve2(dataset):
    paths = dataset['paths']
    streets = dataset['streets']
    time = 0
    solutions = []
    for path in paths: # [rue1, rue2...]
        for street in path: # rue1
            street_data = streets[street]
            if time == 0:
                solutions.append([street_data['end_at'], 1, (street, 1)])
            else:
                solutions.append([street_data['start_at'], 1, (street, 1)])
                solutions.append([street_data['end_at'], 1, (street, 1)])
            time += street_data['L']
    print(time)
    print(solutions)
    return solutions