import glob

import parser, solver2, scorer, writer

# for idx, filename in enumerate(glob.glob('../input/*')):
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt']
for filename in filenames[0: 1]:
    fn = '../input/{}'.format(filename)
    dataset = parser.parse(fn)
    solution = solver2.solve2(dataset)
    writer.write(solution, '../output/{}'.format(filename.replace('.txt', '.out')))