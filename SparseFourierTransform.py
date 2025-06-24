from FastFourierTransform import FFT


def SparseFFT(a, k):
    n = len(a)

    # case where just every coefficient is valid. This is just the FFT case.
    if k == 1:
        return FFT(a)

    # case where only the first one is valid. This is a special case.
    if k == n:
        return [a[0]] * n

    y = [0] * n

    a0 = a[0::2]  # there is probably a way to get this with just the non-zero coefficients.
    y0 = SparseFFT(a0, (k >> 1))  # we only need this since a1 = [...0]

    for i in range((n >> 1)):
        y[i] = y0[i]
        y[(n >> 1) + i] = y0[i]

    return y
