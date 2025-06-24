import math
import cmath


def FFT(a):
    n = len(a)

    # base case. We do not need to do any calculations.
    if n == 1:
        return a

    # output with the same length as the input vector.
    y = [0] * n

    # divide stage. Splitting the coefficients into odd and even powers.
    a0 = a[0::2]
    a1 = a[1::2]

    # recursive stage.
    y0 = FFT(a0)
    y1 = FFT(a1)

    w_n = cmath.rect(1, 2 * math.pi / n)
    w = 1

    # conquer stage.
    for i in range((n >> 1)):  # I use the bit shift method to divide as it makes it so I do not need an integer check.
        t = w * y1[i]
        y[i] = y0[i] + t
        y[(n >> 1) + i] = y0[i] - t  # this method makes it so we don't calculate for the whole range.
        w = w * w_n

    return y


def neg_FFT(a):
    # the negative fourier transform is a semi-inverse transform. It is the same process as the FFT but it uses
    # the inverse/conjugate of the root of unity instead.
    n = len(a)

    # base case. We do not need to do any calculations.
    if n == 1:
        return a

    y = [0] * n

    a0 = a[0::2]
    a1 = a[1::2]

    y0 = neg_FFT(a0)
    y1 = neg_FFT(a1)

    # unlike in the FFT, we use the inverse of the root of unity.
    w_n = cmath.rect(1, -2 * math.pi / n)
    w = 1

    for i in range((n >> 1)):
        t = w * y1[i]
        y[i] = y0[i] + t
        y[(n >> 1) + i] = y0[i] - t
        w = w * w_n  # this is to get powers without having to use exponentiation.

    return y


def IFFT(a):
    # this completes the inversion of the FFT. We use the neg_FFT but divide by the length of the coefficient vector.
    n = len(a)
    neg = neg_FFT(a)

    y = [0] * n  # not the best way to initialize the array.

    for i in range(n):
        y[i] = neg[i] / n

    return y
