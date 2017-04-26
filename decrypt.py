from __future__ import print_function, division, unicode_literals
import wave
import functions as fnc
import numpy as np

def decryptMessage( path ):

    wr = wave.open(path, 'r')
    par = list(wr.getparams())
    par[3] = 0


    lowpass = 200

    sz = wr.getframerate()
    c = int(wr.getnframes()/sz)

    da = np.fromstring(wr.readframes(sz), dtype=np.int16)
    left, right = da[0::2], da[1::2]
    lf, rf = np.fft.rfft(left), np.fft.rfft(right)
    nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)

    iterations = int(da[0]) + 1
    finalMessage = []

    for j in range(1, iterations):
        finalMessage.append( fnc.decryptValue( nl[j] ) );


    wr.close()


    decryptedMessage = ''.join(finalMessage)
    return decryptedMessage
