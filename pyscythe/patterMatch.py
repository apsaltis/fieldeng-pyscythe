import pandas as pd
import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal



def slope(x1,y1,x2,y2):
    der = 10000
    if (x2 - x1 != 0):
        der = (y2 - y1) / (x2 - x1)
    return der

def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00

# Find exact match based on slope change
def patternFindExact(sig, pattern):
    der1 = derivativeArray(sig)
    der2 = derivativeArray(pattern)
    index = 0
    dom = 0
    a = []
    b = []
    dict = {}

    for i in der1:
        if i == der2[index]:
            a.append(i)
            b.append(dom)
            index = index + 1
            dom = dom + 1
            if len(a) == len(der2):
                c = 0
                print(b)
                print(a)
                for j in a:
                    dict[b[c]] = j
                    c = c + 1
                index = 0
                a = []
                b = []
        elif i != der2[index]:
            index = 0
            dom = dom + 1
            a = []
            b = []
    return dict

def derivativeArray(sig):
    index = 0
    deriv = []
    for i in sig:
        if (index+1)<len(sig):
            deriv.append(slope(index, i, index + 1, sig[index + 1]))
            index = index + 1
    return deriv


def search_sequence_numpy(arr,seq):
    """ Find sequence in an array using NumPy only.

    Parameters
    ----------
    arr    : input 1D array
    seq    : input 1D array

    Output
    ------
    Output : 1D Array of indices in the input array that satisfy the
    matching of input sequence in the input array.
    In case of no match, empty list is returned.
    """

    # Store sizes of input array and sequence
    Na, Nseq = arr.size, seq.size

    # Range of sequence
    r_seq = np.arange(Nseq)

    # Create 2D array of sliding indices across entire length of input array.
    # Match up with the input sequence & get the matching starting indices.
    M = (arr[np.arange(Na-Nseq+1)[:,None] + r_seq] == seq).all(1)

    # Get the range of those indices as final output
    if M.any()>0:
        return np.where(np.convolve(M,np.ones((Nseq),dtype=int))>0)[0]
    else:
        return []

def signal_correlate(sig, pattern):
    """Takes in an array containing the signal values of the signal of interest and and array of values of the pattern you wish to match
        Returns an array of values that correspond to points in the signal where the pattern occures both positive and negative. """
    corr = signal.correlate(sig, pattern, mode='same')

    return corr

def signal_correlate_spark(sig, pattern):

    df1 = sc.parallelize([(0.0, 1.0), (1.0, 0.0)]).toDF(["x", "y"])
    df1.stat.corr("x", "y")


def data_to_dataframe(signal, correlation):
    df = pd.DataFrame()
    df['signal'] = signal
    df['correlation'] = correlation

    return df