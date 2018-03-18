from multiprocessing.pool import Pool, ThreadPool

M = 10

def serial(func, n):
  results = map(func, range(n))
  for r in results:
    r["parallel"] = "serial"
  return results

def multithread(func, n, m=M):
  pool = ThreadPool(m)
  results = pool.map(func, range(n))
  pool.close()
  for r in results:
    r["parallel"] = "multithread"
  return results

def multiprocess(func, n, m=M):
  pool = Pool(m)
  results = pool.map(func, range(n))
  pool.close()
  for r in results:
    r["parallel"] = "multiprocess"
  return results
