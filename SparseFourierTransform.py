from FastFourierTransform import FFT


def SparseFFT(a: list, k: int, non_zero: bool) -> list:
    # while I am sure this works, it is definitely not the most efficient way.
    """
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
    """

    # my new implementation will only consider the non-zero values of the vector.
    if non_zero is False:
        a = a[0::k]  # this will remove all the non-zero elements since the new implementation does not need then.

    y_l = FFT(a)

    y = y_l * k  # this is obviously way faster.

    return y
