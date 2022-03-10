import custom_module as cm
import time, numpy as np

M = cm.Matrix(5,5, [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])

print("Custom Matrix Module")
t_start1 = time.perf_counter()
print(M.squared())
print("Время работы squared: %s секунд " % (time.perf_counter() - t_start1))

t_start2 = time.perf_counter()
print(M.transpose())
print("Время работы transpose: %s секунд " % (time.perf_counter() - t_start2))

t_start3 = time.perf_counter()
print(M.det())
print("Время работы squared: %s секунд " % (time.perf_counter() - t_start3))

print("––––––––––––––––––––––––––––––––––––––––––––––––––––")
print("NumPy")

A = np.matrix("1 2 3 4 5; 1 2 3 4 5; 1 2 3 4 5; 1 2 3 4 5; 1 2 3 4 5")

t_start1 = time.perf_counter()
print(np.matmul(A, A))
print("Время работы squared: %s секунд " % (time.perf_counter() - t_start1))

t_start2 = time.perf_counter()
print(np.transpose(A))
print("Время работы transpose: %s секунд " % (time.perf_counter() - t_start2))

t_start3 = time.perf_counter()
print(np.linalg.det(A))
print("Время работы det: %s секунд " % (time.perf_counter() - t_start3))

