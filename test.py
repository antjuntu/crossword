from crossword import *
from generate import *


def main():
    structure = 'data\structure0.txt'
    words = 'data\words0.txt'
    output = None
    #output = 'data\image0.jpg'

    # Generate crossword
    crossword = Crossword(structure, words)
    print('Variables:')
    for v in crossword.variables:
        print(v)
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