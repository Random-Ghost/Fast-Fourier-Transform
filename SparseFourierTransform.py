from FastFourierTransform import FFT


def SparseFFT(a, k):
    n = len(a)
    if k == 1:
        return FFT(a)

    if k == n:
        return [a[0]] * n

    y = [0] * n

    a0 = a[0::2]
    y0 = SparseFFT(a0, (k >> 1))

    for i in range((n >> 1)):
        y[i] = y0[i]
        y[(n >> 1) + i] = y0[i]

    return y
