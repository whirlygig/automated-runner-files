import random
import sys

letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0'.split()
f = open(sys.argv[1], 'w')
for i in range (0, int(sys.argv[2])):
    rand_name1 = ''.join(random.sample(letters, random.randint(3, 20)))
    rand_name2 = ''.join(random.sample(letters, random.randint(3, 20)))
    rand_name3 = ''.join(random.sample(letters, random.randint(3, 20)))
    str = (rand_name1 + "--" + rand_name2 + "--" + rand_name3 + '\n')
    f.write(str)
f.close()
