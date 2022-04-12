import audiosegment
import matplotlib.pyplot as plt
import numpy as np

def visualize(spect, frequencies, title=""):
    # Visualize the result of calling seg.filter_bank() for any number of filters
    i = 0
    for freq, (index, row) in zip(frequencies[::-1], enumerate(spect[::-1, :])):
        plt.subplot(spect.shape[0], 1, index + 1)
        if i == 0:
            plt.title(title)
            i += 1
        plt.ylabel("{0:.0f}".format(freq))
        plt.plot(row)
    plt.show()

seg = audiosegment.from_file("sound_split/sounds/1_tatarca_1.mp3").resample(sample_rate_Hz=24000, sample_width=2, channels=1)
spec, frequencies = seg.filter_bank(nfilters=5)
visualize(spec, frequencies)