__author__ = 'alberto'

import matplotlib.pyplot as plt


def save_image(signal, name='signal', path='./', ext='png'):
    fig = plt.figure()
    plt.plot(range(0, len(signal)), signal)
    fig.savefig(path + name + '.' + ext)
    return True