import numpy as np
import struct
from scipy.signal import savgol_filter as sg_filt


class EmptyClass:
    def __init__(self):
        pass


def process_cars(filename):
    if not filename == 'none':
        # Reading in the binary CARS file
        fid = open(filename, 'rb')
        data = fid.read()
        HeaderLength = struct.unpack('>H', data[0:2])[0]
        PointsPerSpectrum = struct.unpack('>H', data[2:4])[0]
        SpectraPerPixel = struct.unpack('>H', data[4:6])[0]
        XPixels = struct.unpack('>H', data[6:8])[0]
        YPixels = struct.unpack('>H', data[8:10])[0]
        ZPixels = struct.unpack('>H', data[10:12])[0]
        MSB = struct.unpack('>H', data[12:14])[0]
        LSB = struct.unpack('>H', data[14:16])[0]
        XYStepSize = struct.unpack('>H', data[16:18])[0] / 1000
        ZStepSize = struct.unpack('>H', data[18:20])[0] / 1000

        ExposureTime = (MSB * 2 ^ 16 + LSB) / 1e5

        s1 = np.full((XPixels, YPixels, ZPixels, PointsPerSpectrum), 0, dtype='float')
        s2 = np.full((XPixels, YPixels, ZPixels, PointsPerSpectrum), 0, dtype='float')

        # Creating and reading in the data variables s1 and s2
        a = 20
        for zi in range(0, ZPixels):
            for yi in range(0, YPixels):
                for xi in range(0, XPixels):
                    s1[xi, yi, zi, :] = np.flipud(struct.unpack('>512H', data[a:a + (2 * PointsPerSpectrum)]))
                    s2[xi, yi, zi, :] = np.flipud(
                        struct.unpack('>512H', data[a + (2 * PointsPerSpectrum):a + 2 * (2 * PointsPerSpectrum)]))

                    a = a + 2 * (2 * PointsPerSpectrum)

        # Output variable for the data extracted above
        cars = EmptyClass()
        cars.HeaderLength = HeaderLength
        cars.PointsPerSpectrum = PointsPerSpectrum
        cars.SpectraPerPixel = SpectraPerPixel
        cars.XPixels = XPixels
        cars.YPixels = YPixels
        cars.ZPixels = ZPixels
        cars.XYStepSize = XYStepSize
        cars.ZStepSize = ZStepSize
        cars.ExposureTime = ExposureTime
        cars.s1 = s1.astype(float)
        cars.s2 = s2.astype(float)

        return cars


def process_fl(filename):
    if not filename == 'none':
        fid = open(filename, 'rb')
        data = fid.read()
        HeaderLength = struct.unpack('>H', data[0:2])[0]
        PointsPerSpectrum = struct.unpack('>H', data[2:4])[0]
        SpectraPerPixel = struct.unpack('>H', data[4:6])[0]
        XPixels = struct.unpack('>H', data[6:8])[0]
        YPixels = struct.unpack('>H', data[8:10])[0]
        ZPixels = struct.unpack('>H', data[10:12])[0]
        MSB = struct.unpack('>H', data[12:14])[0]
        LSB = struct.unpack('>H', data[14:16])[0]
        Average = struct.unpack('>H', data[16:18])[0]
        XYStepSize = struct.unpack('>H', data[18:20])[0] / 1000
        ZStepSize = struct.unpack('>H', data[20:22])[0] / 1000

        ExposureTime = (MSB * 2 ^ 16 + LSB) / 1e5

        s1 = np.full((Average, PointsPerSpectrum), 0, dtype='float')
        s2 = np.full((Average, PointsPerSpectrum), 0, dtype='float')

        a = 22
        for fi in range(0, Average):
            s1[fi, :] = np.flipud(struct.unpack('>512H', data[a:a + (2 * PointsPerSpectrum)]))
            s2[fi, :] = np.flipud(
                struct.unpack('>512H', data[a + (2 * PointsPerSpectrum):a + 2 * (2 * PointsPerSpectrum)]))

            a = a + 2 * (2 * PointsPerSpectrum)

        cars = EmptyClass()
        cars.HeaderLength = HeaderLength
        cars.PointsPerSpectrum = PointsPerSpectrum
        cars.SpectraPerPixel = SpectraPerPixel
        cars.XPixels = XPixels
        cars.YPixels = YPixels
        cars.ZPixels = ZPixels
        cars.XYStepSize = XYStepSize
        cars.ZStepSize = ZStepSize
        cars.ExposureTime = ExposureTime
        cars.s1 = s1.astype(float)
        cars.s2 = s2.astype(float)

        return cars


def remove_background(cars, cars_fl):
    if not (type(cars) is None.__class__ or type(cars_fl) is None.__class__):
        meanbk1 = np.mean(cars_fl.s1)
        meanbk2 = np.mean(cars_fl.s2)

        [a, b, c, d] = cars.s1.shape

        bkfree1 = np.full((a, b, c, d), 0, dtype='float')
        bkfree2 = np.full((a, b, c, d), 0, dtype='float')

        for ai in range(0, a):
            for bi in range(0, b):
                for ci in range(0, c):
                    bkfree1[ai, bi, ci, :] = np.squeeze(np.squeeze(np.squeeze(cars.s1[ai, bi, ci, :]))) - meanbk1
                    bkfree2[ai, bi, ci, :] = np.squeeze(np.squeeze(np.squeeze(cars.s2[ai, bi, ci, :]))) - meanbk2

        bkfree = EmptyClass()
        bkfree.s1 = bkfree1
        bkfree.s2 = bkfree2

        return bkfree

    else:
        return cars


def remove_stokespump(cars, stokes, pump):
    if not (type(cars) is None.__class__ or type(stokes) is None.__class__ or type(pump) is None.__class__):
        pumpstokes1 = np.squeeze(np.mean(np.mean(stokes.s1[:, :, :, :], 1), 0)) + np.squeeze(
            np.mean(np.mean(pump.s1[:, :, :, :], 1), 0))
        pumpstokes2 = np.squeeze(np.mean(np.mean(stokes.s2[:, :, :, :], 1), 0)) + np.squeeze(
            np.mean(np.mean(pump.s2[:, :, :, :], 1), 0))

        [a, b, c, d] = cars.s1.shape

        psfree1 = np.full((a, b, c, d), 0, dtype='float')
        psfree2 = np.full((a, b, c, d), 0, dtype='float')

        pumpstokes1 = sg_filt(pumpstokes1, window_length=5, polyorder=3)
        pumpstokes2 = sg_filt(pumpstokes2, window_length=5, polyorder=3)

        max1 = max(pumpstokes1)
        max2 = max(pumpstokes2)

        for ai in range(0, a):
            for bi in range(0, b):
                for ci in range(0, c):
                    psfree1[ai, bi, ci, :] = np.squeeze(cars.s1[ai, bi, ci, :]) - (max(
                        np.squeeze(cars.s1[ai, bi, ci, :])) / max1) * pumpstokes1
                    psfree2[ai, bi, ci, :] = np.squeeze(cars.s2[ai, bi, ci, :]) - (max(
                        np.squeeze(cars.s2[ai, bi, ci, :])) / max2) * pumpstokes2

        psfree = EmptyClass()
        psfree.s1 = psfree1
        psfree.s2 = psfree2

        return psfree

    else:
        return cars


def remove_etaloning(bkfree, psfree, etalon):
    if type(psfree) is None.__class__:
        psfree = bkfree

    if type(etalon) is not None.__class__:
        etmn1 = np.squeeze(np.mean(np.mean(etalon.s1[:, :, :, :], 1), 0))
        etmn2 = np.squeeze(np.mean(np.mean(etalon.s2[:, :, :, :], 1), 0))

        [a, b, c, d] = bkfree.s1.shape

        bkfrees1 = bkfree.s1
        bkfrees2 = bkfree.s2
        psfrees1 = psfree.s1
        psfrees2 = psfree.s2

        etalonfree1 = np.full((a, b, c, d), 0, dtype='float')
        etalonfree2 = np.full((a, b, c, d), 0, dtype='float')
        etalonSumfree1 = np.full((a, b, c, d), 0, dtype='float')
        etalonSumfree2 = np.full((a, b, c, d), 0, dtype='float')

        sgetmn1 = sg_filt(etmn1, window_length=7, polyorder=3)
        sgetmn2 = sg_filt(etmn2, window_length=7, polyorder=3)

        for ai in range(0, a):
            for bi in range(0, b):
                for ci in range(0, c):
                    etalonfree1[ai, bi, ci, :] = (np.squeeze(bkfrees1[ai, bi, ci, :])) / sgetmn1
                    etalonfree2[ai, bi, ci, :] = (np.squeeze(bkfrees2[ai, bi, ci, :])) / sgetmn2

                    etalonSumfree1[ai, bi, ci, :] = (np.squeeze(psfrees1[ai, bi, ci, :])) / sgetmn1
                    etalonSumfree2[ai, bi, ci, :] = (np.squeeze(psfrees2[ai, bi, ci, :])) / sgetmn2

        etfree = EmptyClass()
        etfree.s1 = etalonfree1
        etfree.s2 = etalonfree2

        etSumfree = EmptyClass()
        etSumfree.s1 = etalonSumfree1
        etSumfree.s2 = etalonSumfree2

        return etfree, etSumfree

    else:
        return bkfree, psfree


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
