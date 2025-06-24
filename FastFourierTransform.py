import math
import cmath


def FFT(a):
    n = len(a)
    if n == 1:
        return a

    y = [0] * n

    a0 = a[0::2]
    a1 = a[1::2]

    y0 = FFT(a0)
    y1 = FFT(a1)

    w_n = cmath.rect(1, 2 * math.pi / n)
    w = 1

    for i in range((n >> 1)):
        t = w * y1[i]
        y[i] = y0[i] + t
        y[(n >> 1) + i] = y0[i] - t
        w = w * w_n

    return y


def neg_FFT(a):
    n = len(a)
    if n == 1:
        return a

    y = [0] * n

    a0 = a[0::2]
    a1 = a[1::2]

    y0 = neg_FFT(a0)
    y1 = neg_FFT(a1)

    w_n = cmath.rect(1, -2 * math.pi / n)
    w = 1

    for i in range((n >> 1)):
        t = w * y1[i]
        y[i] = y0[i] + t
        y[(n >> 1) + i] = y0[i] - t
        w = w * w_n

    return y


def IFFT(a):
    n = len(a)
    neg = neg_FFT(a)

    y = [0] * n

    for i in range(n):
        y[i] = neg[i] / n

    return y
