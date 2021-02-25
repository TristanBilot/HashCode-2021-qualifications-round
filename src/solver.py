
import pandas as pd  

def solve3(dataset):
    pass

def sol1(dataset):
    paths = pd.DataFrame(dataset["paths"])
    streets = pd.DataFrame(dataset["streets"])
    for p in paths["paths"]:
        print("P+",p)
        # streets.loc[p]["nb_pass"] = streets.loc[p].get("nb_pass", 0) + 1
        print("A")
        print(streets[p])

        
        
        


def solve(dataset):
    sol1(dataset)
    return [
        [1, 2, ('rue-d-athenes', 2), ('rue-d-amsterdam', 1)],
        [0, 1, ('rue-de-londres', 2)],
        [2, 1, ('rue-de-moscou', 1)]
    ]
