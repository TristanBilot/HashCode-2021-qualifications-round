def solve(dataset):
    paths = dataset["paths"]
    streets = dataset["streets"]
    time = 0
    solutions = []
    values = []

    for i in range(len(paths)):
        path = paths[i]
        val = 0
        for street in path["paths"]:
            street_data = streets[street]
            val += street_data["L"]
        values.append({"index": i, "val": val})

    sorted_values = sorted(values, key=lambda x: x["val"])
    sorted_paths = []
    for val in sorted_values:
        sorted_paths.append(paths[val["index"]])

    for path in sorted_paths[0:1]:
        for street in path["paths"]:
            street_data = streets[street]
            random_timeout = int(dataset["global"] / len(path)) - 1

            solutions.append([street_data["end_at"], 1, (street, random_timeout)])
            time += street_data["L"]
    return solutions