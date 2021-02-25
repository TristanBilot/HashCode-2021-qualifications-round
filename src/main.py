import glob

import parser, solver, scorer, writer

for idx, filename in enumerate(glob.glob('../input/*')):
    dataset = parser.parse(filename)
    solution = solver.solve(dataset)
    score = scorer.score(solution, dataset)
    print('Score for %s: %s/%s (%s to perfect score)' % (filename, score, dataset['knapsize'], dataset['knapsize'] - score))
    writer.write(solution, filename.replace('datasets','solutions'))