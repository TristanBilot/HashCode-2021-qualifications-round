import glob
import parser, solver, writer

for idx, filename in enumerate(glob.glob('../input/*')):
    fn = "../input/{}".format(filename)
    dataset = parser.parse(fn)
    solution = solver.solve(dataset)
    writer.write(solution, "../output/{}".format(filename.replace(".txt", ".out")))
