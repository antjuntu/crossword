from crossword import *
from generate import *


def main():
    structure = 'data\structure0.txt'
    words = 'data\words0.txt'
    output = None
    #output = 'data\image0.jpg'

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)

    print('Domains before:')
    for v, domain in creator.domains.items():
        print(v, ':', domain)


    # print('OVERLAPS:')
    # print(crossword.overlaps)
    # for key, value in crossword.overlaps.items():
    #     print(key, value)

    assignment = creator.solve()

    print('Domains after:')
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