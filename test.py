from crossword import *
from generate import *


def main():
    # set1 = {1,2,3}
    # set2 = {2,3,4,5,6,7,8,9}
    # set1 -= set2
    # print(set1)
    
    a = [('yksi',1), ('kolme', 3), ('kaksi', 2)]
    print(a)
    a.sort(key=lambda tup: tup[1])
    print(a)

    result = [t[0] for t in a]
    print(result)




    structure = 'data\structure0.txt'
    structure = 'data\structure1.txt'
    structure = 'data\structure2.txt'
    words = 'data\words0.txt'
    words = 'data\words1.txt'
    words = 'data\words2.txt'

    output = None
    #output = 'data\image0.jpg'

    # Generate crossword
    crossword = Crossword(structure, words)
    # print('Variables:')
    # for v in crossword.variables:
    #     print(v)
    creator = CrosswordCreator(crossword)

    # print('Domains before enforce_node_consistency:')
    # for v, domain in creator.domains.items():
    #     print(v, ':', domain)

    # creator.enforce_node_consistency()

    # print('Domains after:')
    # for v, domain in creator.domains.items():
    #     print(v, ':', domain)


    # print('Overlaps before revise:')
    # # for testing creator.revise()
    # x = None
    # y = None
    # for key, value in crossword.overlaps.items():
    #     if value:
    #         print(key, value)
    #         if x is None:
    #             x, y = key
    # print('x,y', x, y)

    # creator.revise(x, y)


    # print('Domains after revise:')
    # for v, domain in creator.domains.items():
    #     print(v, ':', domain)

    assignment = creator.solve()

    print('Domains after solve:')
    for v, domain in creator.domains.items():
        print(v, ':', domain)

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == '__main__':
    main()