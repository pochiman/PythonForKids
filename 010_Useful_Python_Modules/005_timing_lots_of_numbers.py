import time

def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    # print('it took %s seconds' % (t2-t1))
    print(f'it took {t2-t1} seconds')
    
lots_of_numbers(1000)