# f = open('test.txt')
# s = f.read()
# f.close()
# f = open('output.txt', 'w')
# f.write(s)
# f.close()

import shutil
shutil.copy('test.txt', 'output.txt')