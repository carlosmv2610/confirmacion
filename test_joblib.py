import time
from math import sqrt
from joblib import Parallel, delayed

start = time.time()
Parallel(n_jobs=4,prefer="threads")(delayed(sqrt)(i**2) for i in range(1000000))

end = time.time()
print(end-start)
