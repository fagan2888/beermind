import numpy as np
import theano

def floatX(X):
    return np.asarray(X, dtype=theano.config.floatX)


def scale(X, max_norm):
    curr_norm = T.sum(T.abs_(X))
    return ifelse(T.lt(curr_norm, max_norm), X, max_norm * (X/curr_norm))

def dropout(X, p=0.):
    if p > 0:
        retain_prob = 1 - p
        X *= srng.binomial(X.shape, p=retain_prob, dtype=theano.config.floatX)
        X /= retain_prob
        return X
