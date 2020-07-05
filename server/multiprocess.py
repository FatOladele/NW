import multiprocessing
import time


# def myfunc(abc, rdict):
#   time.sleep(5)
#   rdict['mydict'] = ''.join([abc, '1234'])

# if __name__ == "__main__":

#   manager = multiprocessing.Manager()
#   rdict = manager.dict()
#   print(rdict)
#   jobs = []
#   p = multiprocessing.Process(target= myfunc, args= ('1234',rdict))
#   jobs.append(p)
#   p.start()

#   print('ssdsd')
#   while True:
#     if p.is_alive():
#       print ('I am doing something else')
#       time.sleep(1)
#     else:
#       p.join()
#       print(rdict.values())
#       break
#   print('finished')


print(multiprocessing.cpu_count())
