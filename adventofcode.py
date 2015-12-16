from hashlib import md5
import libchall as lc
import re

def day1():
    '''
    --- Day 1: Not Quite Lisp ---

    Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

    Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    Here's an easy puzzle to warm you up.

    Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

    The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

    For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.
    To what floor do the instructions take Santa?
    '''

    test = '((((()(()(((((((()))(((()((((()())(())()(((()((((((()((()(()(((()(()((())))()((()()())))))))))()((((((())((()))(((((()(((((((((()()))((()(())()((())((()(()))((()))()))()(((((()(((()()))()())((()((((())()())()((((())()(()(()(((()(())(()(())(((((((())()()(((())(()(()(()(())))(()((((())((()))(((()(()()(((((()()(()(((()(((((())()))()((()(()))()((()((((())((((())(()(((())()()(()()()()()(())((((())((())(()()))()((((())))((((()())()((((())((()())((())(())(((((()((((()(((()((((())(()(((()()))()))((((((()((())()())))(((()(()))(()()(()(((()(()))((()()()())((()()()(((())())()())())())((()))(()(()))(((((()(()(())((()(())(())()((((()())()))((((())(())((())())((((()(((())(())((()()((((()((((((()(())()()(()(()()((((()))(())()())()))(())))(())))())()()(())(()))()((()(()(())()()))(()())))))(()))(()()))(())(((((()(()(()()((())()())))))((())())((())(()(())((()))(())(((()((((((((()()()(()))()()(((()))()((()()(())(())())()(()(())))(((((()(())(())(()))))())()))(()))()(()(((((((()((((())))())())())())()((((((((((((((()()((((((()()()())())()())())())(())(())))())((()())((()(()))))))()))))))))))))))))())((())((())()()))))))(((()((()(()()))((())(()()))()()())))(())))))))(()(((())))())()())))()()(())()))()(()))())((()()))))(()))))()))(()()(())))))))()(((()))))()(()))(())())))))()))((()))((()))())(())))))))))((((())()))()))()))())(())()()(())))())))(()())()))((()()(())))(())((((((()(())((()(((()(()()(())))()))))))()))()(()((()))()(()))(()(((())((((())())(())(()))))))))())))))))())())))))())))))()()(((())()(()))))))))())))))(())()()()))()))()))(()(())()()())())))))))())()(()(()))))()()()))))())(()))))()()))))()())))))(((())()()))(()))))))))))()()))))()()()))))(()())())()()())()(()))))()(()))(())))))))(((((())(())())()()))()()))(())))))()(()))))(())(()()))()())()))()))()))()))))())()()))())())))(()))(()))))))())()(((())()))))))))()))()())))())))())))()))))))))))()()))(()()))))))(())()(()))))())(()))))(()))))(()())))))())())()()))))())()))))))))(()))))()))))))()(()())))))))()))())))())))())))())))))))())(()()))))))(()())())))()())()))))))))))))))())))()(())))()))())()()(())(()()))(())))())()())(()(()(()))))())))))))))))())(()))()))()))))(())()())()())))))))))))()()))))))))))))())())))))(()())))))))))))())(())))()))))))))())())(()))()))(())))()))()()(())()))))))()((((())()))())())))))()))()))))((()())()))))())))(())))))))))))))))))()))))()()())()))()()))))())()))((()())))())))(()))(()())))))))()))()))))(())))))))(())))))())()()(()))())()))()()))))())()()))))())()))())))))))(()))))()())()))))))))(()))())))(()))()))))(())()))())())(())())())))))))((((())))))()))()))()())()(())))()))()))()())(()())()()(()())()))))())())))))(()))()))))())(()()(())))))(())()()((())())))))(())(())))))))())))))))))()(())))))))()())())())()(()))))))))(()))))))))())()()))()(()))))))()))))))())))))))(())))()()(())()())))))(((())))()((())()))())))(()()))())(())())))()(((()())))))()(()()())))()()(()()(()()))())()(()()()))())()()))()())(()))))())))))())))(())()()))))(()))))(())(()))(())))))()()))()))))())()))()()(())())))((()))())()))))))()()))))((()(()))))()()))))))())))))())(()((()())))))))))))()())())))()))(()))))))(()))(())()())))(()))))))))())()()()()))))(()())))))))((())))()))(()))(())(())()())()))))))))(())))())))(()))()()))(()()))(()))())))()(())))())((()((()(())))((())))()))))((((())())()())))(())))()))))))())(()()((())))())()(()())))))(()())()))())))))))((())())))))))(()(()))())()()(()()(((()(((()())))))()))))))()(())(()()((()()(())()()))())()())()))()())())())))))))(((())))))))()()))))))(((())()))(()()))(()()))))(()(()()((((())()())((()()))))(()(())))))()((()()()())()()((()((()()))(()))(((()()()))(((())))()(((())()))))))((()(())())))(()())(((((()(()))(()((()))(()())()))))(()(()))()(()))(())(((())(()()))))()()))(((()))))(()()()()))())))((()()()(())()))()))))()()))()))))))((((((()()()))))())((()()(((()))))(()(())(()()())())())))()(((()()))(())((())))(()))(()()()())((())())())(()))))()))()((()(())()(()()(())(()))(())()))(())(()))))(())(())())(()()(()((()()((())))((()))()((())))(((()()()()((((()))(()()))()()()(((())((())())(()()(()()()))()((())(())()))())(((()()(())))()((()()())()())(()(())())(((())(())())((())(())()(((()()))(())))((())(()())())(())((()()()((((((())))((()(((((())()))()))(())(()()))()))(())()()))(())((()()())()()(()))())()((())))()((()()())((((()())((())())())((()((()))()))((())((()()(()((()()(((())(()()))))((()((())()(((())(()((())())((())(()((((((())())()(()())()(())(((())((((((()(())(()((()()()((()()(()()()())))()()(((((()()))()((((((()))()(()(()(()(((()())((()))())()((()))(())))()))()()))())()()))())((((())(()(()))(((((((())(((()(((((()(((()()((((())(((())())))(()()()(()(()))()))((((((()))((()(((()(())((()((((()((((((())(((((())))(((()(()))))(((()(((())()((())(()((()))(((()()(((())((((()(()(((((()))(((()(((((((()(()()()(()(()(()()())(())(((((()(())())()())(()(()(()))()(()()()())(()()(()((()))()((())())()(()))((())(()))()(()))()(((()(()(()((((((()()()()())()(((((()()(((()()()((()(((((()))((((((((()()()(((((()))))))(()()()(())(()))(()()))))(())()))(((((()(((((()()(()(()())(((()))((((()((()(()(()((()(()((())))()(((()((()))((()))(((((((((()((()((()(())))()((((()((()()))((())(((()(((((()()(()(()()((()(()()()(((((((())())()())))))((((()()(()))()))(()((())()(()(((((((((()()(((()(()())(()((()())((())())((((()(((()(((()((((()((()((((()(()((((((())((((((((((((()()(()()((((((((((((((()((()()))()((((((((((((())((((()(()())((()(()(()))()(((((()()(((()()))()())(())((()(((((()((())(((((()((()(((((()))()()((((())()((((())(((((((((()(())(()(())))())(()((())(((())(())(())())(()(()(())()()((()((())()(((()(((((()(())))()(((()((())))((()()()(((()(((()((()(()(())(()((()())(()(()(((()(((((((((())(()((((()()))(()((((()()()()(((()((((((((()(()()((((((()(()()(()((()((((((((((()()(((((((()())(())))(((()()))(((((()((()()())(()()((((())((()((((()))))(())((()(()()(((()(()(((()((((()(((((()))())())(()((())()))(((()())((())((())((((()((()((((((())(()((((()()))((((((())()(()))((()(((())((((((((((()()(((((()(((((()((()()()((((())))(()))()((()(())()()((()((((((((((()((())(())(((((()(()(()()))((((()((((()()((()(((()(((((((((()(()((()((()))((((((()(((())()()((()(((((((()())))()()(()((()((()()(((()(()()()()((((()((())((((()(((((((((()(((()()(((()(()(((()(((()((())()(()((()(()(()(()))()(((()))(()((((()((())((((())((((((())(()))(()((((())((()(()((((((((()()((((((()(()(()()()(())((()((()()(((()(((((((()()((()(((((((()))(((((()(((()(()()()(()(((()((()()((())(()(((((((((()(()((()((((((()()((())()))(((((()((())()())()(((((((((((()))((((()()()()())(()()(()(()()))()))(()))(()(((()()))())(()(()))()()((())(()())()())()(()))()))(()()(()((((((())((()(((((((((((()(())()((()(()((()((()(()((()((((((((((()()())((())()(())))((())()())()(((((()(()())((((()((()(())(()))(((())()((()))(((((())(()))()()(()))(((())((((()((((()(())))(((((((()))))())()())(())((())()(()()((()(()))()(()()(()()((()())((())((()()))((((()))()()))(()()(())()()(((((()(())((()((((()))()))(()())())(((()()(()()))(())))))(()))((())(((((()((((()))()((((()))()((())(((())))(((()())))((()(()()(('
    print (test.count('(')-test.count(')'))

    '''
    --- Part Two ---

    Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

    For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.
    What is the position of the character that causes Santa to first enter the basement?
    '''
    floor = 0
    for i,c in enumerate(test):
        if c == '(': floor += 1
        if c == ')': floor -= 1
        if floor == -1:
            print i+1
            break

def day2():
    '''
    --- Day 2: I Was Told There Would Be No Math ---

    The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

    Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

    For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
    All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
    '''

    f = open('files/adventofcode-day2.txt', 'r')
    a = 0
    for line in f:
        line = line[:-1] # trim newline
        if len(line) > 0:
            line = line.split('x')
            l = int(line[0])
            w = int(line[1])
            h = int(line[2])
            s = min([l*w,w*h,h*l])
            a += 2*l*w + 2*w*h + 2*h*l + s
    print a

    '''
    --- Part Two ---

    The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

    For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
    How many total feet of ribbon should they order?
    '''
    f = open('files/adventofcode-day2.txt', 'r')
    a = 0
    for line in f:
        line = line[:-1] # trim newline
        if len(line) > 0:
            line = line.split('x')
            l = int(line[0]) * 2 + int(line[1]) * 2
            w = int(line[1]) * 2 + int(line[2]) * 2
            h = int(line[2]) * 2 + int(line[0]) * 2
            s = min([l,w,h])
            a += s + (int(line[0]) * int(line[1]) * int(line[2]))
    print a

def day3():
    '''
    --- Day 3: Perfectly Spherical Houses in a Vacuum ---

    Santa is delivering presents to an infinite two-dimensional grid of houses.

    He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

    However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

    For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
    '''
    test='^^<<v<<v><v^^<><>^^<v<v^>>^^^><^>v^>v><><><<vv^^<^>^^<v^>v>v^v>>>^<>v<^<v^><^>>>>><<v>>^>>^>v^>><<^>v>v<>^v^v^vvv><>^^>v><v<><>^><^^<vv^v<v>^v>>^v^>v><>v^<vv>^><<v^>vv^<<>v>>><<<>>^<vv<^<>^^vv>>>^><<<<vv^v^>>><><^>v<>^>v<v^v<^vv><^v^><<<<>^<>v>^v>v<v<v<<>v<^<<<v>>>>>^^v>vv^^<>^<>^^^^<^^^v<v^^>v<^^v^^>v>^v^^^^>><<v<>v<>^v^<v<>><>^^><<^^<^^>vv<>v^<^v<vv<<<>^>^^>^<>v^^vv<>>v><<<>vvv<>v<>><^<^v<>^vv>^^v<v<v><^<>>vv<^>>^>>vv^v<vv^vv<^<<>>^v^<>^>>>>vv>^^>v>vv>v><^vv^<<v>^<<^^<v<v>vv<v^^<>^^v>^>>v><^<<vv<<v^vv^^^v>>v<<v^><vv^><vv<^vv<<vv^v<<^v<^^v>><<v^>>^^<>v>><<v<>>^^<v>>^^>>vvv^><<<<<^<^vv<^<><v<<>^^^<<<^>^^^<v<<vv>vv<>^<>v<^v>^<<<v<v<v>>^v<>>v<<^<<v<<>^<<<><><>^>>>>^>v^v<<v<v<<>>vv<^vvv^^^^<vv>vv>^v^^v^<v^v><^vv<^vv>v<^>vv<>>^>^><vv<><^>v>^v>vvv<>^>^v<><>vv>><^v^<><><v>>v^v^><^<^>vv>v<^>vvv>v<<<<<^<v<<vv<^^^<<>>^v<vv<^<>v>^<v<>><><>^<<v>v^>^<vv>><><>>^>^>><^<v>^^>^^>^^v^^<^v^^>v^^>>><<><v<v<<v^vv<><><>^<v>^<<^^v^>v>><>^^^><^vvv<^^^^^v><<><v<^^v><><>>^>vv<vvvv<<>>><v<^^^^v<<^><v>^vv<v^^v^vv<^^>^^<v>><<v^>v<^^>^<^<v<^^v>^<<v>^>>>^v<>v<^^^>vvv^v<<^><>>><vvv^<^^^<^>>v>>><v>^^vvv^vvv<^^^^v^v^<vv^<v>^<<^>v^v^<<><>><^v><v<><<>><<<>^v>v<>^<v^v>^vv>>^<>v^^<<v><^v>>v<>>^v^^>><^>v^<^v^^>><>v^>^v^v<<<v^<v^^v<^>v<><>vv>>>>^>v<>v<<<>^^>vv^v<><v^<>^<<<<>>^^>^v<v^v<<><>^v<>>^v^<<^<^>>>^vv<><v<^^<>v^>>v<^^v<v>>>^>><<><<<>><vv<v>>^v>><^<v><vv>^vv<v<>>><>v^><>vv<^^v^^^v<>><^vvv<<^<>v>>>v>><v><>>><>><v^><v^v<v>^v>v<v>>^^<^>^>v><>vv>^v><<>>>>>>>^<<^vv^^vvvv<^^><<<v<<>vvv<>^><<v<v^v^<<v>v<>>^<vv^<v<v>^<<^^vv>v>^<vv<<>v<v^<>v>>^v^^vvvv>^^>>v^v^^><<^>v>>^^>^<^^<>v<v>vv^vv>v<v>>^v<><^vv^<vv<v^^^v<^v^>>^v>>>^^<^<^>^v^>^>>>^v>^>^^^>>^<>v^^<>^v<<^^>^^<vv<>v<^v^>><^v^>^<>>^vv^vv^>v^<vvvvvv^>><^^<^v<^<v^<<^^<<v^<^>><>v><^v^v^^^v>v^<>^<<v<^^vvv<v>^^>^v^^<><vv^v^>v^<<>>vv<>>>>v>v<>^>>>v<>^^><v<v^^^<>^<^><>^><<v>><>^<<>>><<^<vvv<^><v>>^vv^v>><v<>vv^<<^^<<><v><<^<v<vv<<^v^vv>v^>>>v<<<<v<<>v>^vv<^v><v<v>v<^>^^vv>v><v>><<v<<v^v>>><>^<>><><<^<<^v^v<<v>v>v<v<^^>vv<^v^^^<v^<<<v<>v^><^v>^<^<v>>^<<<v>>v^<><>>^v<>vvv<vvvvv<^^><^>><^^>^>^v^vv<^><<^v>><^^v>^v<>^>vvvv><^>^<<v^^vv<v^^<><>v>^>>^<^<<<^v^^^>^>>^>><><<^>v^^<v>>v<<<<vvv<vvvv^<^<v^^<>^>vvv^<vv^v^v>^<<><v><^v^v^^^>^^>^vv<>v>>v^>vv^vv>v<^v^^>>^v^v<>>^^><<v<<>><>>>^>^<>^^v^^><^<>><<^<vv^^^^^>>vv^<v^<^>>>>v<<><<^>vv>vvv>^<><>>>>vv><<v^v<^^^<<^^^vv^<v<><><<<<>><<v^<>v>v^><>v^v^^><>v>v>^^v<^v<>>^^^^^<v>><v^>^^<v>><v^^>v<^<^>>>^><^^>><<>>^><>^^^>v^^^>^^v^<>^^><^>>><><^>>v<v^>v<^><v<v^<>v<^v>v^<^vv^^><<<><><^v^<v<^^>v>v^>>^^vv^<v>^v>^<^v<>^>^><^<v>^v><^<^<>v^^>^><>>><<v><<><>v<<^v^^<^><>^<><><v>v<^^<v<v>>^^<<>>^<v>><^><^<^>^^v<>v>>><><<>^>v><><<<<v^^^^v<>>^^^v>><<^v>^>>><vv^>>^vv<^<>>^<^^<^v>v<v<<<<<>^<<^<<<<<^<^>>^><<>><>v^v>^<^>v^<><vvv^>^v^v^v><^<v<>vv<<^<>^^^<>^v>^<v^^<v^v>v<>>^>v<<>v<>v^v>v<<<>>v>vv>>v<<>v<>v<^>^>^<v>>v>^>^^^<vv>v<<>>><v>^vvv^^>^^<^vv^^^^>v>^v^>v^^v^>>^v>^vv>^^v^<<<<>^<><^<^<<^^>v^^^v<>>vvv<v>>vv><v<v>^<^v>>^v<vv^<<v<vv><^^v^v>v<>^v<<<^^v^^^<^v>v^v^v>><vvv<<>v<>^v>vv^v>vv<<^v<v>^v>v>><^v<v<>v>>>><<<><vv><>^v^<^vvv>v<>><^v>^>><v>vv<><><>v><>>><^>vv>>^<>v^>>^><<<^><<>^v^>>><><>vv>^<>^>^v^^><^>>><<>v^<^vv>^<^vv>><v<>vv<v><><<^><>v<^^<^>vv^^^^vv<<v><>vv<><v>v<>>>>^><v><>^<><>v<>><<>^^vvv>^^^<><>>vvv^v>><>vv<vv>^^^v^<<>^^v<><<^^v<>^^>^<^^v>>v^v^^>>v>>>^<<^<>^>^^v>>>><vv<<>^v<<vv><<^^vv><^>vv<>>v<v>v^>v>>v^<vv<<<v><v^>vvv^^>vv^<<v>v^>>v^<>>><><<^^<^v>^>>>v>v>^v<>vv><vv<vvv<<v>v>^v<<<>><<><><>v^>>>v^>v^>>vv^^<v>^<>>><^>v^<>^^><v>v<><<<><v^v<<<v<v^>v^v>^>v<^<>v>v^^>>v>vv^v<>>^^^^<>v^>>>>>>>><v<^<<vvv<^v^>^v<^<<>>><<<^<<^>^>v^<>^<<<>v>><^vv^>^>^>>>^<vv><v^^^<v^<v<><v^vvv<>v<vvv^vv<<<v^<^<^vvvv^<<vv<^v><<>^>^<v^v^<^>v^><>>v^>v^>^>>v<>vv^v<<>^^>>vv<>vv>>^v<^vv>^v>v<v^vvv^<<^><>v^<><vv><>v^^><<<><>^>^v^<>><vv<^>v^v>v<>><v<<^>^<vv<^v>^<<v><^<^^vv^<>><v^>^vv^<>>^^^^v>v><^^^v^<<<>^<^<<>><>>v<<^v^>><><v^>>^vv^v>vv>>>>>>^^<<>v^>v^v>^^>>><vv^^^v>^v>>^^^<>><>v^<<<v<vv^^<v^<<<>v>v^^^<vv<>>^v>^v<^<<><>vv>^^^<^^vv<v<<vv>^^>vv>v<<^>^vv><^><v>^^^^v<<vv>v^<<^^>>^^vvvv^v^>vv>>v^<v>vvv<>>^><>>v^^>>^<>>vvvv^>><v^v<^^<^vv>>v<<^<<^><v^^><v^>v^>><<<v>v>v^>^v<v^vv<^^^v<^<vvvvv<<vvv>><>v<v<v<<^v<><<>vv>><v>><^>>^^v>^>><>vv^><<>>vv<<<^<^^>^<<^>>>><v<^v<<<>>v>vv<^>^v><>>v<v^v<>v^vvvv>v^>>v><<^<v>^^v>>vv^^>v>^v>^v^^>^<^vv<v<<^>vv<<^>>^<<^^>>^<^>v^><^vv>^^v><v^>>><>v^v>^v<^><<<>vv><v>v<><>>v^<>^^>^<>^<<^>>vv^><^<v<^^vvv>>v^>>v^>v>vv><>>v<^>><<<v<<vv><v<v<v>v<v>vv^vvv^vv^>^>v><vv<v^^<>>>>vv^>^<>v<^>^<^v>vv<^<<>>^<^<vv><^^<>^<<v^v^>v<<><v>v>><^v<<^vvv>v>v<<^^<^^>v<vv<v<v^v>^^^>^>vv<v<<^^v^<v<^>^^^vv>v<>>>vv>><><^><><<<vvv<<^^v^<v^<<^>>vv>vv^v^>>><v><<v^v>>v>>vv>^^vvv^>^^>^>^>^v<<^vv^>vvv^^vv><^>^v^>^><>v<^^vv<v><v^<><^<>><v>^^v^v>v^vv<>><^v>^<^v>^<>^v>>>><<vv^^^vv^>>><vv^v>>v><^v^vv><<^v<<>^^<v><^v>vvv<><^^><<^v><>^<^v<^^<^vvvv^^>>>>vv>v>>>v<v^><<<<v>>v^><v>>vv^v<vv<>vv<>vvv>>>><>>><>^v<v^v><vvv<<v^^v^v<>>><>>^vv<<v<><<vv<v^>^^vv><^v^v<v^vvv^v>v^^^vv>^><^vvv<<>^vvv^<v<v^v>>>>^<<<><<<<<^v<^^>>>>^>^<v^^^v<vvv<vv^<>v<<<^<^>>v^<v><<><<^^vvv^>v<>>^^>v>^v>>v<v><v>>>>^<^<^>v^v<vv<>^>><>^<<^vvv^^<>^<vvv<>v^>^^<<^>^vv><vvv>>v^v^>v><v>^<^^<>^>^>>>^^vvv^<<>v^<<>><>v<^<^>v^>^vv><v<^<<<^v>^>>^<^v^<<<<^v^><v^v>v^><<v<><<v^<<^<<v<<v><v><><^^^^>v>^^<v>>v<vvv<<<>><>>^><<><^<>>^^>vv<^><^v^><vvv>>>vvv<<vv^<^^^<^>^<>>^>>^v^<^^v>^<v<<>^^v<^vv^><vvv>>^v><<^<v^<><><>>^>vv<<>^^^v^^<v<>><>>vv>v^>vvv^^v<vv<^<^>>^>>^>>v^<<<v^>v^<^v^vv^><^<^v<<v<<>v>^v^<<<v^vv<v<<>^^<v>>>^<v<^>^^v<v>>>><vv<^^<<>><<v<v>^^v^>>^^>>^v^<^v>v^v^v^v^>v^vv<><>^^<>^><^^^<<<^<v>v<<>^<^^^^^v^<^<<^^>^vv<>v^>><>>^>v>v<>^>v<v^>>><>^<><v>>>^>^>>v^><v<>v><^vv^>v<<v>v<><<vv<<v>^><^<v^>v<<v^v<<><v><>v<v><>^^<v<>><<>v>vv<<v>^v<v>vv><><>vv^<<>^>^<^>>>^v>v<^v^^^vv<>>>^<<^>>><<^^v^>v^<^v>vvv>v^^vv>^^>>v<>^<<>^<><^^v^>><>^>v>>^^^<<^^v<>^^>^<>^>><^>^vvv><^>^<^>^>>vv<^>>^v>>^<>>^^>>>v^<v>>v<<v<^>>v^^vv>v><^v^^><vv^v<^>v<<>v^^<><>^>vvv><^^^>^v^>v>>^vvv<^vv>^^>^>>v<>><<^v<<v^>^><>vv^<<^^vv><v>>^<^><^<v>^v<v>^<<>^v^^>v^>>^^^<^vv>v^>>>vv<<>v>>>^>v^^<v^v^^v^>>v<v<<v>^<<>>vv<<^v>v<<vv<<^<^v<^<><^^>v>>v>v^>><vv<^v<^>^>>v>^><<^<<>^v<v>>><^^<^<<<v^^>^>vv<<>^<>^<v^<<^v>vv>^^^v<^v><v<<<<<vv>vv>^^^^>v>v><<^<<<^vv><^<<<><v>><v^v>v<<v^^<v^>v>^v^v^<^<^vv>vvv<^^v<>v<<<<>v<v^<vvv^^^<<^<^<<>^<<><<<>v<^>^^v<^^v^>vv>vvv>v><v^^<<>>^><^>>v<<vv>v<<^^^v<<^v^^><><<<><<>v>^<<>v<<<^v>><v^v<^v<v^vv>v>><<^<><^v^^v<v>^>^>vvvv<<><<>>^<vv>^^><v<>v>v<v^^>^><>>><^><<><<<^<>v^><vv^^^^>>^v^>v^<>>v>^^><^<^v^<v^>>v>^vvv<>>v<v^v><>^vvvv<v^<<v^<<^^vv>><<<<<<v><<<v<v^v^^<v^^<>v<<<<^v<<><<v^<^><v<vv<v^v^<v^^vv<v^v<<<>^<<>vv<v<^>^<<><vv<<vv<v<^<^<>><^^<<>>>vv>>>>>>^v<v<>>v^v^^<v^<<<<>><<^v^^^<>^<vv>>>><>v^v^vvv^>>v>><v^v<<<^v>>^^<<^^vv><<<^^^<<<v><^^>>>>vvv^v<^>^^>v<^<><vv<v<>v>>>^vv<<^<v>^v^>^>^v>v>v^v^>v<<v>><>><v^^<<^>>>><<^v^<>^v<vv><>vvv^>v>v<v<v^>^<><><>^>>><v<<<v^vv><>^>^^<<v^>>v^^>^<v>><>><>v^v^^v>>>>vv>>^v<<^v^<>^>v^^>^^<<vvvvvvv>^<v^<<^<<>><<<^^^v^^^^v<^<>v<^^<>vv^^v^<>^<<^>>v>v<<<^^^^vvv^<^<><>v<<v^<^<>>><<><<<v<v<v><vv>^^<vv<<vv<<<v<^>^^vv<v<>><<>>>^v<<>^>>>v^>v>^^<>^<vv<><^>v>^>>>><>^^>v^^v>^vv^^v^><<<>>v<>v<vv<vv^v^v<^v^<^^><<<><vv^^>^<^<<>v>>>>^<<v>v<v>vv<^><^<v><<^>v>>v><<v<<^v^<>>^>>>^v^v>v^^vv^>^<^^>>^><^vv^^vv^<>>^^^^<^^><><v<>>^>>^><vv^>^vvv<^<<v^^<<<>^><>>>^^<><v<v<><<v^^^^^<^<^<<>><<>>>>^<<>>>^<^v^>><<^>>>^<<v>^>><>^<v>^<><v>^v^^vv<><^>vv^^v^<^^^v^vvv^>><>>v<<vv<>>^<^vvv<<^^><vvv^^<v<>vv^^<<>><v>><^^vvv<<<^>^<><^>vv^><^<<>vv<<v>>vv>v>v^<vv><vv><<>^^^^v^^^^<v>^<<^><><^^v^>v>^>><^><<>v^<v>>>^vvv>>^<^<>^^v^vv^^v><<vv^<>>>v<<<>v>^<>v<<>v^>^<<><<><v<v<v<>v^>v<><^^>^<^v^^><^>vv>^>vv<v<^v>vv>^^><<>vv^>^v<<^<<^<<>v<v<^<v>v>>^><v^^v^v>>>><v^v^<<<vv<<^^<>>v^v<^v>v>^^^v<v><v^^^vv<>v^v<^<>v><><v^<>>vv>v><>v>^v<><<<<<<v<>>v^vv<<<<v<<v><^<>^>><>^^vv>^<^<<>vv>>vv<vvv>><><v<>><^<v>^><^<<v>><v><v>^<v>><>v^^^^v<v^^v<>^^vv<>v<>v>^vv^><v^<<^<>^<>^^^>v^>>>v><<^>>v<^v<>^^<v<><v^v<v>v<><v<vv><<>v<^<^>v<>v^>v>^^<<<^^vv^<><<<>>v>^^<>v>>>><v<v<^^^v<v<v^><<>v^v<>v>><<<<v^<><^<<^>^<vvv<v^^v>>v^vv^><^v^^<>^^><<v^>>vv>^<v^vv<^^v<>>vvv<^v^>>^<v<v>>^>^^<<^>^>^v><>>^<^^v>^>>^^<><>>>^^>^^vvv>v<^^<>v^v^^<v<<^<v^v^<<>v^v<v<<v<>>><<^^^>>v>^vv>^>^^v<>^^<>v^^<><v<v<vvv^<vv<<>v^><<><v<>vv<<^vvvv><<<v>v>v^>v^<>v^>^<v<vvv^>^<>^>^^v<>><<<><v<^^>^v<v>^^v^v<<<^v^<>^<>v>^^>v<v<v>v>^^<<<><<^>v<v<^vv^v><^^<<vv>^<<v><>^>>>>><v^v<<<^>^v^v<<v<>vvv<<>v>v>>^v^v^>><<<<>v^<v<><<>>>^>>^>><<v>'
    map={}
    x = 0
    y = 0
    map['0-0'] = 1 # seed origin
    for c in test:
        if c == '^': y += 1
        elif c == 'v': y -= 1
        elif c == '<': x -= 1
        elif c == '>': x += 1
        try:
            map[str(x) + '-' + str(y)] += 1
        except KeyError:
            map[str(x) + '-' + str(y)] = 1
    count = 0
    for i in map:
        count += 1
    print count

    '''
    --- Part Two ---

    The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

    Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

    This year, how many houses receive at least one present?

    For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
    '''
    robo = False
    map2={}
    map2['0-0'] = 2 # seed origin
    coords = [0,0,0,0] # robo_x, robo_y, santa_x, santa_y
    loop = 0
    for c in test:
        robo = not robo
        if robo:
            offset = 0
        else:
            offset = 2
        if c == '^': coords[offset+1] += 1
        elif c == 'v': coords[offset+1] -= 1
        elif c == '<': coords[offset+0] -= 1
        elif c == '>': coords[offset+0] += 1
        try:
            map2[str(coords[offset+0]) + '-' + str(coords[offset+1])] += 1
        except KeyError:
            map2[str(coords[offset+0]) + '-' + str(coords[offset+1])] = 1
    count = 0
    for i in map2:
        count += 1
    print count

def day4():
    '''
    --- Day 4: The Ideal Stocking Stuffer ---

    Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

    For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
    Your puzzle input is ckczppom.
    '''
    i = 0
    test = 'ckczppom'
    m = ''
    while True:
        m = md5(test + str(i)).hexdigest()
        if m[:5] == '00000': break
        i += 1
    print i, m

    '''
    --- Part Two ---

    Now find one that starts with six zeroes.
    '''
    i = 0
    m = ''
    while True:
        m = md5(test + str(i)).hexdigest()
        if m[:6] == '000000': break
        i += 1
    print i, m

def day5():
    '''
    --- Day 5: Doesn't He Have Intern-Elves For This? ---

    Santa needs help figuring out which strings in his text file are naughty or nice.

    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.
    How many strings are nice?
    '''
    nice = []
    # nice, naughty, naughty, naughty
    # test = ['ugknbfddgicrmopn', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb', 'aaa']
    with open('files/adventofcode-day5.txt', 'r') as test:
        for line in test:
            state = 0
            while state <> -1:
                if state == 0:
                    state = 1
                    for sub in ['ab','cb','pq','xy']:
                        if line.find(sub) <> -1: state = -1
                if state == 1:
                    state = -1
                    for c in line:
                        if line.count(c) > 1: state = 2
                if state == 2:
                    state = -1
                    for c in line:
                        if line.count(c+c) > 0: state = 3
                if state == 3:
                    state = -1
                    vowel_count = 0
                    for c in ['a','e','i','o','u']:
                        if line.count(c) > 0: vowel_count += line.count(c)
                    if vowel_count >= 3: nice.append(line)
    print len(nice)+1

    '''
    --- Part Two ---

    Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
    How many strings are nice under these new rules?
    '''
    '''

    '''

    nice=[]
    # test = ['qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy']
    with open('files/adventofcode-day5.txt', 'r') as test:
        for line in test:
            state = 0
            while state <> -1:
                if state == 0:
                    state = -1
                    for i,c in enumerate(line):
                        if line.count(line[i:i+2]) > 1:
                            state = 1
                            break
                if state == 1:
                    state = -1
                    for c in line:
                        if len(re.findall(c+'.'+c,line)) > 0:
                            state = 2
                            break
                if state == 2:
                    nice.append(line)
                    # print line
                    break
    print len(nice)

def lights(action,left,right):
    left = left.split(',')
    right = right.split(',')

    if action == 'on':
        print 'on'
    elif action == 'off':
        print 'off'
    elif action == 'toggle':
        print 'toggle'

def day6():
    '''
    --- Day 6: Probably a Fire Hazard ---

    Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

    Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

    Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

    To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

    For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
    After following the instructions, how many lights are lit?
    '''
    grid = [[0 for x in range(999)] for x in range(999)]
    with open('files/adventofcode-day6.txt', 'r') as f:
        for line in f:
            word = line.split(' ')
            if len(word[0]) == 4:
                lights(word[1],word[2],word[4])
            elif split[0] == 'toggle':
                lights(word[0],word[1],word[3])

day6()
