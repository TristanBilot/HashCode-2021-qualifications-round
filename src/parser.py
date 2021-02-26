import pandas as pd
from collections import defaultdict

def parse(filename):
    with open(filename, "r") as fi:
        global_time, nb_inter, nb_streets, nb_cars, car_score = map(
            int, fi.readline().split()
        )

        lines = fi.readlines()
        streets = {}
        paths = []
        for line in lines[0:nb_streets]:
            line = line.split(" ")
            streets[line[2]] = {
                "start_at": int(line[0]),
                "end_at": int(line[1]),
                "L": int(line[3].replace("\n", "")),
            }
        for line in lines[nb_streets:]:
            paths.append(
                {"P": int(line[0]), "paths": line[1:].replace("\n", "").split(" ")[1:]}
            )
        graph = defaultdict(dict)
        for street in streets.values():
            graph[street["start_at"]][street["end_at"]] = street["L"]

        dataset = {
            "global": global_time,
            "nb_car": nb_cars,
            "streets": streets,
            "paths": paths,
            "graph": graph,
            "nb_street": nb_streets,
            "nb_inter": nb_inter,
        }
        return dataset
