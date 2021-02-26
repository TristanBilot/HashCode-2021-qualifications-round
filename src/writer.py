def write(solution, filename):
    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')
        for ele in solution:
            fo.write(str(ele[0])+'\n')
            fo.write(str(ele[1]) + '\n')
            for x in ele[2: ]:
                fo.write('{} {}\n'.format(x[0], x[1]))
