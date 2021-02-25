def parse(filename):
    with open(filename, 'r') as fi:
        nbPizzas, nbTeam1, nbTeam2, nbTeam3 = map(int,fi.readline().split())
        lines = fi.readlines().split()

        dataset = {
            'nbPizzas': nbPizzas
        }
        return dataset