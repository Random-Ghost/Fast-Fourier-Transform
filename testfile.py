from FastFourierTransform import *
from SparseFourierTransform import SparseFFT

print(FFT([3, 3, 3, 3, 3, 3, 3, 3]))

print(IFFT([6, 0, 6, 0, 6, 0, 6, 0]))

print(SparseFFT([3, 0, 0, 0, 3, 0, 0, 0], 4, non_zero=False))

print(SparseFFT([3, 3], k=4, non_zero=True))
