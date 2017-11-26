
import numpy as np
from scipy.io import loadmat
from scipy.interpolate import InterpolatedUnivariateSpline, interp2d


class EmptyClass:
            def __init__(self):
                pass


def tran4d_2d(cars):
    [a, b, c, d] = cars.s1.shape

    datamat1 = np.full((a * b * c, d), 0)
    datamat2 = np.full((a * b * c, d), 0)

    ct = 0
    for ai in range(0, a):
        for bi in range(0, b):
            for ci in range(0, c):
                datamat1[ct, :] = cars.s1[ai, bi, ci, :]
                datamat2[ct, :] = cars.s2[ai, bi, ci, :]
                ct = ct + 1

    cars2d = EmptyClass()
    cars2d.s1 = datamat1
    cars2d.s2 = datamat2
    cars2d.a = a
    cars2d.b = b
    cars2d.c = c
    cars2d.d = d

    return cars2d


def cars_anscombe(signal, gauss_std, gauss_mean=0, poisson_multi=1):
    SMALL_VAL = 1
    signal = tran4d_2d(signal)

    fsignal1 = 2 / poisson_multi * np.sqrt(np.fmax(SMALL_VAL, poisson_multi * signal.s1 +
                                                   (3 / 8) * poisson_multi ** 2 +
                                                   gauss_std ** 2 -
                                                   poisson_multi * gauss_mean))

    fsignal2 = 2 / poisson_multi * np.sqrt(np.fmax(SMALL_VAL, poisson_multi * signal.s2 +
                                                   (3 / 8) * poisson_multi ** 2 +
                                                   gauss_std ** 2 -
                                                   poisson_multi * gauss_mean))

    fsignal1 = np.reshape(fsignal1, (signal.a, signal.b, signal.c, signal.d))
    fsignal2 = np.reshape(fsignal2, (signal.a, signal.b, signal.c, signal.d))

    fsignal = EmptyClass()
    fsignal.s1 = fsignal1
    fsignal.s2 = fsignal2

    return fsignal


def cars_invanscombe(fsignal, gauss_std, gauss_mean=0, poisson_multi=1):
    """
    Parameters
    ----------
    fsignal : ndarray
        Forward Anscombe-transformed noisy signal (1-,2-,3D)

    gauss_std : float, int
        Standard deviation of Gaussian noise

    """
    SMALL_VAL = 0
    fsignal = tran4d_2d(fsignal)

    mat_dict = loadmat('ProcessFiles/AnscombeVectors/GenAnscombe_vectors.mat')

    Efzmatrix = np.squeeze(mat_dict['Efzmatrix'])
    Ez = np.squeeze(mat_dict['Ez'])
    sigmas = np.squeeze(mat_dict['sigmas'])

    gauss_std = gauss_std / poisson_multi;

    # interpolate the exact unbiased inverse for the desired gauss_std
    # gauss_std is given as input parameter
    if gauss_std > np.max(sigmas):
        # for very large sigmas, use the exact unbiased inverse of
        # Anscombe modified by a -gauss_std^2 addend
        exact_inverse1 = anscombe_inverse_exact_unbiased(fsignal.s1) - gauss_std ** 2
        exact_inverse2 = anscombe_inverse_exact_unbiased(fsignal.s2) - gauss_std ** 2

        # this should be necessary, since anscombe_inverse_exact_unbiased(fsignal) is >=0 and gauss_std>=0.

        exact_inverse1 = np.fmax(np.zeros(exact_inverse1.shape), exact_inverse1)
        exact_inverse2 = np.fmax(np.zeros(exact_inverse2.shape), exact_inverse2)

    elif gauss_std > 0:
        # interpolate Efz

        Efz = interp2d(sigmas, Ez, Efzmatrix, kind='linear')(gauss_std, Ez)

        # apply the exact unbiased inverse
        exact_inverse1 = InterpolatedUnivariateSpline(Efz, Ez, k=1)(fsignal.s1)
        exact_inverse2 = InterpolatedUnivariateSpline(Efz, Ez, k=1)(fsignal.s2)

        # outside the pre-computed domain, use the exact unbiased inverse
        # of Anscombe modified by a -gauss_std^2 addend
        # (the exact unbiased inverse of Anscombe takes care of asymptotics)
        outside_exact_inverse_domain1 = fsignal.s1 > np.max(Efz.flatten())
        outside_exact_inverse_domain2 = fsignal.s2 > np.max(Efz.flatten())
        asymptotic1 = anscombe_inverse_exact_unbiased(fsignal.s1) - gauss_std ** 2
        asymptotic2 = anscombe_inverse_exact_unbiased(fsignal.s2) - gauss_std ** 2
        exact_inverse1[outside_exact_inverse_domain1] = asymptotic1[outside_exact_inverse_domain1]
        exact_inverse2[outside_exact_inverse_domain2] = asymptotic2[outside_exact_inverse_domain2]
        outside_exact_inverse_domain1 = fsignal.s1 < np.min(Efz);
        outside_exact_inverse_domain2 = fsignal.s2 < np.min(Efz);
        exact_inverse1[outside_exact_inverse_domain1] = 0;
        exact_inverse2[outside_exact_inverse_domain2] = 0;
    elif gauss_std == 0:
        # if gauss_std is zero, then use exact unbiased inverse of Anscombe
        # transformation (higher numerical precision)
        exact_inverse1 = anscombe_inverse_exact_unbiased(fsignal.s1);
        exact_inverse2 = anscombe_inverse_exact_unbiased(fsignal.s2);
    else:  # gauss_std < 0
        raise ValueError('Error: gauss_std must be non-negative!')

    # reverse the initial variable change

    exact_inverse1 *= poisson_multi;
    exact_inverse1 += gauss_mean;

    exact_inverse2 *= poisson_multi;
    exact_inverse2 += gauss_mean;

    exact_inverse = EmptyClass()
    exact_inverse.s1 = np.reshape(exact_inverse1, (fsignal.a, fsignal.b, fsignal.c, fsignal.d))
    exact_inverse.s2 = np.reshape(exact_inverse2, (fsignal.a, fsignal.b, fsignal.c, fsignal.d))

    return exact_inverse


def anscombe_inverse_exact_unbiased(fsignal):
    """
    Parameters
    ----------
    fsignal : ndarray
        Forward Anscombe-transformed noisy signal (1-,2-,3D)

    Returns
    -------
    signal : ndarray (matched to signal shape)
        Inverse Anscombe-transformed signal
    """
    mat_dict = loadmat('ProcessFiles/AnscombeVectors/Anscombe_vectors.mat')

    Efz = mat_dict['Efz']
    Ez = mat_dict['Ez']

    asymptotic = (fsignal / 2) ** 2 - 1 / 8;  # asymptotically unbiased inverse [3]
    #    asymptotic = _ne.evaluate('(fsignal/2)**2 - 1/8')  # asymptotically unbiased inverse [3]

    # start = time.process_time()
    signal = InterpolatedUnivariateSpline(Efz, Ez, k=1)(fsignal)  # exact unbiased inverse [1,2]
    # stop = time.process_time()
    # print(stop-start)

    outside_exact_inverse_domain = fsignal > np.max(
        Efz)  # for large values use asymptotically unbiased inverse instead of linear extrapolation of exact unbiased inverse outside of pre-computed domain

    signal[outside_exact_inverse_domain] = asymptotic[outside_exact_inverse_domain];

    outside_exact_inverse_domain = fsignal < 2 * np.sqrt(3 / 8)  # min(Efz(:));

    signal[outside_exact_inverse_domain] = 0;

    return signal
