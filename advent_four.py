import hashlib
import sys
import time
def advent_of_code_intro(project_num):
    print ""
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ---------------------------- Welcome to ----------------------------------'
    time.sleep(.1)
    print '  -------------------------- Advent of Code --------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------------------ Created by: David Daly 2016 VA ------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------- This project was done as part the adventofcode.com coding --------'
    time.sleep(.1)
    print '  ------- challenges. This is project %s. Each project has two parts. -------' % project_num
    time.sleep(.1)
    print '  ------- This program completes both parts. -------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -------- You can find me on Github at github.com/ddjr --------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    print ""
    time.sleep(.8)
advent_of_code_intro(4)
five_zeros = True
print "My key is: iwrupvqb"
print ""
print"Searching",
for second_half_of_key in range (1, 10000000):
    m = hashlib.md5()
    m.update("iwrupvqb")
    the_string = str(second_half_of_key)
    m.update(the_string)
    the_hash = m.hexdigest()
    if second_half_of_key % 100000 == 0:
        print ".",
    if the_hash.startswith("00000") and five_zeros == True:
        print ""
        print "the five zero hash is %s " % the_hash
        print "key is: %s " % second_half_of_key
        print ""
        print"Searching",
        five_zeros = False
    elif the_hash.startswith("000000"):
        print ""
        print "the six zero hash is %s " % the_hash
        print "key is: %s " % second_half_of_key
        sys.exit()
print "key is over 10,000,000!"
