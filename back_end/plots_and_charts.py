import matplotlib.pyplot as plt
import librosa
import librosa.display
import scipy
import numpy as np
import seaborn as sns
import pandas as pd
import back_end.data_loading as dl
import math


def plot_single_audio_wave(signal):
    plot1 = plt.subplot(211)
    plot1.plot(signal)
    plot1.set_xlabel('sample rate * time')
    plot1.set_ylabel('energy')


def plot_single_audio_amplitude(signal, rate):
    plt.figure()
    librosa.display.waveplot(y=signal, sr=rate)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")


def plot_single_audio_fft(signal, rate, type=1):
    n = len(signal)
    T = 1 / rate

    if type == 1:
        yf = scipy.fft(signal)
        xf = np.linspace(0.0, 1.0 / (2.0 * T), n // 2)
        fig, ax = plt.subplots()
        ax.plot(xf, 2.0 / n * np.abs(yf[:n // 2]))
        plt.grid()
        plt.xlabel("Frequency")
        plt.ylabel("Magnitude")

    elif type == 2:
        x = np.linspace(0.0, n * T, n)
        yf = scipy.fftpack.fft(signal)
        xf = np.linspace(0.0, 1.0 / (2.0 * T), n // 2)
        fig, ax = plt.subplots()
        ax.plot(xf, 2.0 / n * np.abs(yf[:n // 2]))


default_color_code = "#C2185B"
default_title = "Plot"
def emotion_distribution_bar_plot(df, color_code=default_color_code, title=default_title):
    bar_plot_df = pd.DataFrame()
    bar_plot_df['Emotion'] = list(df.emotion_label.value_counts().keys())
    bar_plot_df['Count'] = list(df.emotion_label.value_counts())
    # print(bar_plot_df)
    fig, ax = plt.subplots(figsize=(14, 7))
    ax = sns.barplot(x="Emotion", y="Count", color=color_code, data=bar_plot_df)
    ax.set_title(title)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.show()


def emotion_distribution_pie_plot(df):
    df1 = df.copy()
    df1 = dl.get_df_with_length(df1)

    class_dist = df1.groupby(['emotion_label'])['length'].mean()
    # print(class_dist)
    fig, ax = plt.subplots()
    ax.set_title('Class Distribution', y=1.08)
    ax.pie(class_dist, labels=class_dist.index, autopct='%1.1f%%', shadow=False, startangle=90)
    ax.axis('equal')
    plt.show()


def rows_and_columns(dict):
    no_of_plots_needed = len(dict)
    rows = math.ceil(no_of_plots_needed / 5)
    columns = 5
    last_row_columns = no_of_plots_needed - ((rows - 1) * 5)

    return rows, last_row_columns


def plot_signals(signals):
    fig, axes = plt.subplots(nrows=2, ncols=5, sharex=False, sharey=True, figsize=(20, 5))
    fig.suptitle('Time Series', size=16)

    rows, lrc = rows_and_columns(signals)
    count = 0
    columns = 5
    for x in range(rows):
        if count == (rows-1):
            columns = lrc
        for y in range(columns):
            axes[x, y].set_title(list(signals.keys())[count])
            axes[x, y].plot(list(signals.values())[count])
            axes[x, y].get_xaxis().set_visible(False)
            axes[x, y].get_yaxis().set_visible(False)
            count += 1


def plot_fft(ffts):
    fig, axes = plt.subplots(nrows=2, ncols=5, sharex=False, sharey=True, figsize=(20, 5))
    fig.suptitle('Fourier Transforms', size=16)

    rows, lrc = rows_and_columns(ffts)
    count = 0
    columns = 5
    for x in range(rows):
        if count == (rows-1):
            columns = lrc
        for y in range(columns):
            data = list(ffts.values())[count]
            Y, freq = data[0], data[1]
            axes[x, y].set_title(list(ffts.keys())[count])
            axes[x, y].plot(freq, Y)
            axes[x, y].get_xaxis().set_visible(False)
            axes[x, y].get_yaxis().set_visible(False)
            count += 1


def plot_fbank(fbanks):
    fig, axes = plt.subplots(nrows=2, ncols=5, sharex=False, sharey=True, figsize=(20, 5))
    fig.suptitle('Filter Bank Coefficients', size=16)

    rows, lrc = rows_and_columns(fbanks)
    count = 0
    columns = 5
    for x in range(rows):
        if count == (rows - 1):
            columns = lrc
        for y in range(columns):
            axes[x, y].set_title(list(fbanks.keys())[count])
            axes[x, y].imshow(list(fbanks.values())[count], cmap='hot', interpolation='nearest')
            axes[x, y].get_xaxis().set_visible(False)
            axes[x, y].get_yaxis().set_visible(False)
            count += 1


def plot_mfccs(mfccs):
    fig, axes = plt.subplots(nrows=2, ncols=5, sharex=False, sharey=True, figsize=(20, 5))
    fig.suptitle('Mel Frequency Cepstrum Coefficients', size=16)

    rows, lrc = rows_and_columns(mfccs)
    count = 0
    columns = 5
    for x in range(rows):
        if count == (rows - 1):
            columns = lrc
        for y in range(columns):
            axes[x, y].set_title(list(mfccs.keys())[count])
            axes[x, y].imshow(list(mfccs.values())[count], cmap='hot', interpolation='nearest')
            axes[x, y].get_xaxis().set_visible(False)
            axes[x, y].get_yaxis().set_visible(False)
            count += 1
