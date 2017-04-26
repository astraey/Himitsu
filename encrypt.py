from __future__ import print_function, division, unicode_literals
import wave, os
import functions as fnc
import numpy as np


def encryptMessage( path, textInput ):

    head, tail = os.path.split(path)
    fileName = "[200Hz] "+tail

    # Created input file if not exists with:
    wr = wave.open(path, 'r')
    par = list(wr.getparams())
    par[3] = 0

    #output file
    ww = wave.open(fileName, 'w')
    ww.setparams(tuple(par))

    lowpass = 200

    sz = wr.getframerate()
    c = int(wr.getnframes()/sz)

    message = textInput


    for num in range(c):

        da = np.fromstring(wr.readframes(sz), dtype=np.int16)

        # left and right channel
        left, right = da[0::2], da[1::2]
        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
        lf[:lowpass], rf[:lowpass] = 0, 0
        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)

        lenght = len(message)

        nl[0], nr[0] = lenght, lenght

        if len(message) < lowpass:
            k = 1
            for char in message:

                temp = fnc.encryptChar(char)
                nl[k], nr[k] = temp, temp

                k = k + 1


        ns = np.column_stack((nl,nr)).ravel().astype(np.int16)
        ww.writeframes(ns.tostring())

    wr.close()
    ww.close()
