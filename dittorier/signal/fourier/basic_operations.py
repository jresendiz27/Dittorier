__author__ = 'alberto'

from dittorier.config import np


def convolve(signal_a, signal_b):
    return np.convolve(signal_a, signal_b)


def sum(signal_a, signal_b):
    pass


def subtract(signal_a, signal_b):
    pass


def multiply(signal_a, signal_b):
    pass


def divide(signal_a, signal_b):
    pass


def reflex(signal_a):
    return signal_a[::-1]


def decimate(signal_a, factor, center=0):
    decimated_signal = []
    for index in range(0, center):
        if index % factor == 0:
            decimated_signal.append(signal_a[index])

    for index in range(center, len(signal_a)):
        if index % factor == 0:
            decimated_signal.append(signal_a[index])

    return decimated_signal


def interpolate(signal_a, factor, **kwargs):
    interpolated_signal = []
    for index in range(0, len(signal_a)):
        interpolated_signal.append(signal_a[index])
        for i in range(0, factor - 1):
            if kwargs['filter'] == 'step':
                interpolated_signal.append(signal_a[index])
            if kwargs['filter'] == 'zero':
                interpolated_signal.append(0)
    return interpolated_signal