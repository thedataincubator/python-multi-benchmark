from multiprocessing.pool import Pool, ThreadPool

def serial(func, n):
  results = map(func, range(n))
  for r in results:
    r["parallel"] = "serial"
  return results

def multithread(func, n, m=3):
  pool = ThreadPool(m)
  results = pool.map(func, range(n))
  pool.close()
  for r in results:
    r["parallel"] = "multithread"
  return results

def multiprocess(func, n, m=3):
  pool = Pool(m)
  results = pool.map(func, range(n))
  pool.close()
  for r in results:
    r["parallel"] = "multiprocess"
  return results
