import sys
import mainwindow
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
# sys.path.insert(0, 'E:/KCL/PhD/1-Software/CARS Analysis/cars_analysis_notebooks/cars_analysis_tb')
from cars_analysis_tb.cars_analysis_tb import CARS
from cars_analysis_tb.cars_analysis_tb.preprocess import process as pf
import tkinter.filedialog
tkinter.Tk().withdraw()


class DataViewer(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(DataViewer, self).__init__(parent)
        self.setupUi(self)

        # TODO Consider making a function to plot a spectrum and image (to avoid repeating the lines and ROI)
        # TODO Make a function that resets all the variables and call it here to start them

        # Creating CARS variables
        self.bkfreecars = None
        self.bkfreecars_im_track1 = None
        self.bkfreecars_im_track2 = None
        self.bkfreecars_im_sum = None
        self.bkfreecars_im_sipcars = None
        self.bkfreecars_pl_track1 = None
        self.bkfreecars_pl_track2 = None
        self.bkfreecars_pl_sum = None
        self.bkfreecars_pl_sipcars = None

        self.normcars = None
        self.normcars_im_track1 = None
        self.normcars_im_track2 = None
        self.normcars_im_sum = None
        self.normcars_im_sipcars = None
        self.normcars_pl_track1 = None
        self.normcars_pl_track2 = None
        self.normcars_pl_sum = None
        self.normcars_pl_sipcars = None

        self.pump = None
        self.stokes = None
        self.etalon = None
        self.etpump = None
        self.etstokes = None
        self.etfree = None
        self.etSumfree = None
        self.cars_ansc2d = None

        # Plot/Image section: connecting buttons to functions
        self.RESET.clicked.connect(lambda: self.reset_viewer())
        # self.update_image.clicked.connect(self.update_image_func())
        self.update_spectrum.clicked.connect(lambda: self.update_spec_func())
        self.load_file.clicked.connect(lambda: self.load_cars())
        self.cars_data_type.activated.connect(lambda: self.choose_cars_type())
        self.track1_image_select.clicked.connect(lambda: self.select_image_type())
        self.track2_image_select.clicked.connect(lambda: self.select_image_type())
        self.sum_image_select.clicked.connect(lambda: self.select_image_type())
        self.sipcars_image_select.clicked.connect(lambda: self.select_image_type())
        self.track1_plot_select.clicked.connect(lambda: self.select_plot_type())
        self.track2_plot_select.clicked.connect(lambda: self.select_plot_type())
        self.sum_plot_select.clicked.connect(lambda: self.select_plot_type())
        self.sipcars_plot_select.clicked.connect(lambda: self.select_plot_type())

        # Normalisation tab: connecting buttons to functions
        self.load_pump_file.clicked.connect(lambda: self.load_norm_files(type='pump'))
        self.load_stokes_file.clicked.connect(lambda: self.load_norm_files(type='stokes'))
        self.load_etalon_file.clicked.connect(lambda: self.load_norm_files(type='etalon'))
        self.load_etalonpump_file.clicked.connect(lambda: self.load_norm_files(type='etpump'))
        self.load_etalonstokes_file.clicked.connect(lambda: self.load_norm_files(type='etstokes'))
        self.run_normalisation.clicked.connect(lambda: self.do_normalisation())
        self.pca_comp_enter.clicked.connect(lambda: self.do_pca_cars_part2(self.cars_ansc2d, 0))
        self.nrb_enter.clicked.connect(lambda: self.enter_nrb_region())

        # Unsupervised clustering tab: connecting buttons to functions
        self.pca_cluster_run.clicked.connect(lambda: self.run_pca_clustering())

        # Connect menu bar actions
        self.actionExit.triggered.connect(lambda: self.user_exit())

        # TODO Get rid of the spectrum window things everywhere apart from initialising it here

        # Setting up plotting and image pyqtgraph settings -------------------------------------------------------------
        pg.ImageView(view=pg.PlotItem())
        self.spec_lo = 0
        self.spec_hi = 0

        def spec_region_updated(regionItem):
            self.spec_lo, self.spec_hi = regionItem.getRegion()

        self.pgLRI = pg.LinearRegionItem()
        self.spectrum_win.addItem(self.pgLRI)
        self.pgLRI.sigRegionChanged.connect(spec_region_updated)
        # --------------------------------------------------------------------------------------------------------------

    # Functions to process menu bar actions
    def user_exit(self):
        sys.exit(0)

    # Function to load and process the CARS data file
    def load_cars(self):
        self.show_busy()

        file_name = tkinter.filedialog.askopenfilename(initialdir='E:/KCL/PhD/Data', defaultextension='.cars')
        file_name_bk = file_name[:-5] + '_fl_traces.cars'

        self.cars_file_name.setText(file_name)
        cars_data = pf.process_cars(file_name)
        cars_bk_data = pf.process_fl(file_name_bk)

        # Resetting CARS variables
        self.bkfreecars = None
        self.bkfreecars_im_track1 = None
        self.bkfreecars_im_track2 = None
        self.bkfreecars_im_sum = None
        self.bkfreecars_im_sipcars = None
        self.bkfreecars_pl_track1 = None
        self.bkfreecars_pl_track2 = None
        self.bkfreecars_pl_sum = None
        self.bkfreecars_pl_sipcars = None

        self.normcars = None
        self.normcars_im_track1 = None
        self.normcars_im_track2 = None
        self.normcars_im_sum = None
        self.normcars_im_sipcars = None
        self.normcars_pl_track1 = None
        self.normcars_pl_track2 = None
        self.normcars_pl_sum = None
        self.normcars_pl_sipcars = None

        self.pump = None
        self.stokes = None
        self.etalon = None
        self.etpump = None
        self.etstokes = None
        self.etfree = None
        self.etSumfree = None
        self.cars_ansc2d = None

        # Resetting plot/image selection buttons
        self.track1_image_select.setChecked(False)
        self.track2_image_select.setChecked(False)
        self.sum_image_select.setChecked(False)
        self.sipcars_image_select.setChecked(True)

        self.track1_plot_select.setChecked(False)
        self.track2_plot_select.setChecked(False)
        self.sum_plot_select.setChecked(False)
        self.sipcars_plot_select.setChecked(True)

        # Closing current plots and image
        self.spectrum_win.clear()

        self.bkfreecars = pf.remove_background(cars_data, cars_bk_data)
        self.bkfreecars_im_track1 = np.squeeze(np.mean(self.bkfreecars.s1, 3))
        self.bkfreecars_im_track2 = np.squeeze(np.mean(self.bkfreecars.s2, 3))
        self.bkfreecars_im_sum = np.squeeze(np.mean((self.bkfreecars.s1 + self.bkfreecars.s2), 3))
        self.bkfreecars_im_sipcars = np.squeeze(np.mean((self.bkfreecars.s2 - self.bkfreecars.s1), 3))
        self.bkfreecars_pl_track1 = np.squeeze(np.mean(np.mean(self.bkfreecars.s1, 1), 0))
        self.bkfreecars_pl_track2 = np.squeeze(np.mean(np.mean(self.bkfreecars.s2, 1), 0))
        self.bkfreecars_pl_sum = np.squeeze(np.mean(np.mean((self.bkfreecars.s1 + self.bkfreecars.s2), 1), 0))
        self.bkfreecars_pl_sipcars = np.squeeze(np.mean(np.mean((self.bkfreecars.s2 - self.bkfreecars.s1), 1), 0))

        # Plotting image and spectrum
        self.image_win.setImage(self.bkfreecars_im_sipcars)
        self.spectrum_win.plot(self.bkfreecars_pl_sipcars)

        self.spec_window_change()

        self.show_idle()

    # Functions to control the plot and image windows
    def spec_window_change(self):
        def spec_region_updated(regionItem):
            self.spec_lo, self.spec_hi = regionItem.getRegion()

        self.pgLRI = pg.LinearRegionItem()
        self.spectrum_win.addItem(self.pgLRI)
        self.pgLRI.sigRegionChanged.connect(spec_region_updated)

    def update_spec_func(self):
        # Obtaining coordinates of ROI graphic in the image plot
        image_coord_handles = self.image_win.roi.getState()
        posimage = image_coord_handles['pos']
        sizeimage = image_coord_handles['size']

        posx = int(posimage[0])
        sizex = int(sizeimage[0])
        posy = int(posimage[1])
        sizey = int(sizeimage[1])
        image_xmin = posx
        image_xmax = posx + sizex
        image_ymin = posy
        image_ymax = posy + sizey

        # Resetting plot window
        self.spectrum_win.clear()

        choose_id = int(self.cars_data_type.currentIndex())

        if choose_id == 0:
            if self.track1_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        self.bkfreecars.s1[image_ymin:image_ymax, image_xmin:image_xmax, :, :], 1), 0)),
                    pen='r', name='track1')

            if self.track2_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        self.bkfreecars.s2[image_ymin:image_ymax, image_xmin:image_xmax, :, :], 1), 0)),
                    pen='g', name='track2')

            if self.sum_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        (self.bkfreecars.s1[image_ymin:image_ymax, image_xmin:image_xmax, :, :] +
                         self.bkfreecars.s2[image_ymin:image_ymax, image_xmin:image_xmax, :, :]), 1), 0)),
                    pen='b', name='sum')

            if self.sipcars_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        (self.bkfreecars.s2[image_ymin:image_ymax, image_xmin:image_xmax, :, :] -
                         self.bkfreecars.s1[image_ymin:image_ymax, image_xmin:image_xmax, :, :]), 1), 0)),
                    pen='w', name='sipcars')

        elif choose_id == 1:
            if self.track1_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        self.normcars.s1[image_ymin:image_ymax, image_xmin:image_xmax, :, :], 1), 0)),
                    pen='r', name='track1')

            if self.track2_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        self.normcars.s2[image_ymin:image_ymax, image_xmin:image_xmax, :, :], 1), 0)),
                    pen='g', name='track2')

            if self.sum_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        (self.normcars.s1[image_ymin:image_ymax, image_xmin:image_xmax, :, :] +
                         self.normcars.s2[image_ymin:image_ymax, image_xmin:image_xmax, :, :]), 1), 0)),
                    pen='b', name='sum')

            if self.sipcars_plot_select.isChecked():
                self.spectrum_win.plot(
                    np.squeeze(np.mean(np.mean(
                        (self.normcars.s2[image_ymin:image_ymax, image_xmin:image_xmax, :, :] -
                         self.normcars.s1[image_ymin:image_ymax, image_xmin:image_xmax, :, :]), 1), 0)),
                    pen='w', name='sipcars')

        self.spec_window_change()

    def update_image_func(self):
        choose_id = int(self.cars_data_type.currentIndex())

        if choose_id == 0:
            if self.track1_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean(
                    self.bkfreecars.s1[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

            elif self.track2_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean(
                    self.bkfreecars.s2[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

            elif self.sum_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean((
                    self.bkfreecars.s1[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3) +
                    self.bkfreecars.s2[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

            elif self.sipcars_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean((
                    self.bkfreecars.s2[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3) -
                    self.bkfreecars.s1[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

        elif choose_id == 1:
            if self.track1_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean(
                    self.normcars.s1[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

            elif self.track2_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean(
                    self.normcars.s2[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

            elif self.sum_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean((
                    self.normcars.s1[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3) +
                    self.normcars.s2[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

            elif self.sipcars_image_select.isChecked():
                carsImage_update = np.squeeze(np.mean((
                    self.normcars.s2[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3) -
                    self.normcars.s1[:, :, :, int(self.spec_lo):int(self.spec_hi)], 3))
                self.image_win.clear()
                self.image_win.setImage(carsImage_update)

    def reset_viewer(self):
        choose_id = int(self.cars_data_type.currentIndex())

        if choose_id == 0:
            # Resetting plot/image selection buttons
            self.track1_image_select.setChecked(False)
            self.track2_image_select.setChecked(False)
            self.sum_image_select.setChecked(False)
            self.sipcars_image_select.setChecked(True)

            self.track1_plot_select.setChecked(False)
            self.track2_plot_select.setChecked(False)
            self.sum_plot_select.setChecked(False)
            self.sipcars_plot_select.setChecked(True)

            # Plotting image and spectrum
            self.image_win.setImage(self.bkfreecars_im_sipcars)
            self.spectrum_win.clear()
            self.spectrum_win.plot(self.bkfreecars_pl_sipcars)

        elif choose_id == 1:
            # Resetting plot/image selection buttons
            self.track1_image_select.setChecked(False)
            self.track2_image_select.setChecked(False)
            self.sum_image_select.setChecked(False)
            self.sipcars_image_select.setChecked(True)

            self.track1_plot_select.setChecked(False)
            self.track2_plot_select.setChecked(False)
            self.sum_plot_select.setChecked(False)
            self.sipcars_plot_select.setChecked(True)

            # Plotting image and spectrum
            self.image_win.setImage(self.normcars_im_sipcars)
            self.spectrum_win.clear()
            self.spectrum_win.plot(self.normcars_pl_sipcars)

    def image_selection(self):
        pass

    def plot_selection(self):
        pass

    def select_image_type(self):
        choose_id = int(self.cars_data_type.currentIndex())

        if choose_id == 0:
            if self.track1_image_select.isChecked():
                self.image_win.setImage(self.bkfreecars_im_track1)

            elif self.track2_image_select.isChecked():
                self.image_win.setImage(self.bkfreecars_im_track2)

            elif self.sum_image_select.isChecked():
                self.image_win.setImage(self.bkfreecars_im_sum)

            elif self.sipcars_image_select.isChecked():
                self.image_win.setImage(self.bkfreecars_im_sipcars)

        elif choose_id == 1:
            if self.track1_image_select.isChecked():
                self.image_win.setImage(self.normcars_im_track1)

            elif self.track2_image_select.isChecked():
                self.image_win.setImage(self.normcars_im_track2)

            elif self.sum_image_select.isChecked():
                self.image_win.setImage(self.normcars_im_sum)

            elif self.sipcars_image_select.isChecked():
                self.image_win.setImage(self.normcars_im_sipcars)

    def select_plot_type(self):
        choose_id = int(self.cars_data_type.currentIndex())

        # TODO Insert if statement to check whether self.bkfreecars is None or not (same with normcars)

        if choose_id == 0:
            self.spectrum_win.clear()
            # self.spectrum_win.getPlotItem().Legend.items = []

            if self.track1_plot_select.isChecked():
                self.spectrum_win.plot(self.bkfreecars_pl_track1, pen='r', name='track1')

            if self.track2_plot_select.isChecked():
                self.spectrum_win.plot(self.bkfreecars_pl_track2, pen='g', name='track2')

            if self.sum_plot_select.isChecked():
                self.spectrum_win.plot(self.bkfreecars_pl_sum, pen='b', name='sum')

            if self.sipcars_plot_select.isChecked():
                self.spectrum_win.plot(self.bkfreecars_pl_sipcars, pen='w', name='sipcars')

        elif choose_id == 1:
            self.spectrum_win.clear()
            # self.spectrum_win.getPlotItem().Legend.items = []

            if self.track1_plot_select.isChecked():
                self.spectrum_win.plot(self.normcars_pl_track1, pen='r', name='track1')

            if self.track2_plot_select.isChecked():
                self.spectrum_win.plot(self.normcars_pl_track2, pen='g', name='track2')

            if self.sum_plot_select.isChecked():
                self.spectrum_win.plot(self.normcars_pl_sum, pen='b', name='sum')

            if self.sipcars_plot_select.isChecked():
                self.spectrum_win.plot(self.normcars_pl_sipcars, pen='w', name='sipcars')

        self.spec_window_change()

    def choose_cars_type(self):
        choose_id = int(self.cars_data_type.currentIndex())

        if choose_id == 0:
            self._message('')
            if self.bkfreecars is None:
                self._message('A CARS data file has not been loaded yet!')

            else:
                self.track1_image_select.setChecked(False)
                self.track2_image_select.setChecked(False)
                self.sum_image_select.setChecked(False)
                self.sipcars_image_select.setChecked(True)

                self.track1_plot_select.setChecked(False)
                self.track2_plot_select.setChecked(False)
                self.sum_plot_select.setChecked(False)
                self.sipcars_plot_select.setChecked(True)

                pg.ImageView(view=pg.PlotItem())
                self.image_win.setImage(self.bkfreecars_im_sipcars)
                self.spectrum_win.clear()
                self.spectrum_win.plot(self.bkfreecars_pl_sipcars)

                self.spec_window_change()

        elif choose_id == 1:
            self._message('')
            if self.normcars is None:
                self._message('Normalisation has not been run yet!')

            else:
                self.track1_image_select.setChecked(False)
                self.track2_image_select.setChecked(False)
                self.sum_image_select.setChecked(False)
                self.sipcars_image_select.setChecked(True)

                self.track1_plot_select.setChecked(False)
                self.track2_plot_select.setChecked(False)
                self.sum_plot_select.setChecked(False)
                self.sipcars_plot_select.setChecked(True)

                pg.ImageView(view=pg.PlotItem())
                self.image_win.setImage(self.normcars_im_sipcars)
                self.spectrum_win.clear()
                self.spectrum_win.plot(self.normcars_pl_sipcars)

                self.spec_window_change()

    # Functions to control the normalisation of the data
    def do_normalisation(self):
        self.show_busy()

        if self.bkfreecars is None:
            self._message('No CARS file has been loaded!')

        else:
            self.bkfreecars = self.do_pca_cars_part1(self.bkfreecars, 0)

        self.show_idle()

    def do_pca_cars_part1(self, bkfreecars, gauss_std):
        from sklearn.decomposition import PCA

        self.show_busy()

        class EmptyClass:
            def __init__(self):
                pass

        cars_ansc = anscombe.cars_anscombe(bkfreecars, gauss_std)
        cars_ansc2d = anscombe.tran4d_2d(cars_ansc)

        cars_diff = cars_ansc2d.s2 - cars_ansc2d.s1

        # PCA carried out on the difference data first to choose the number of components to keep
        pca_tran = PCA()
        pca_tran.fit_transform(cars_diff)
        diff_pca_var = pca_tran.explained_variance_ratio_

        self.normalisation_spectrum_win.clear()
        self.normalisation_spectrum_win.plot(diff_pca_var)

        self.show_idle()

        self._message('Enter number of PCA components to be kept')

        self.cars_ansc2d = cars_ansc2d

    def do_pca_cars_part2(self, cars_ansc2d, gauss_std):
        from sklearn.decomposition import PCA

        self.show_busy()

        class EmptyClass:
            def __init__(self):
                pass

        num_comp = int(self.pca_comp_no.text())

        pca_tran2 = PCA(n_components=int(num_comp))
        cars_pca1 = pca_tran2.fit_transform(cars_ansc2d.s1)
        cars_pca1 = pca_tran2.inverse_transform(cars_pca1)
        cars_pca2 = pca_tran2.fit_transform(cars_ansc2d.s2)
        cars_pca2 = pca_tran2.inverse_transform(cars_pca2)

        cars_pca = EmptyClass()
        cars_pca.s1 = np.reshape(cars_pca1, (cars_ansc2d.a, cars_ansc2d.b, cars_ansc2d.c, cars_ansc2d.d))
        cars_pca.s2 = np.reshape(cars_pca2, (cars_ansc2d.a, cars_ansc2d.b, cars_ansc2d.c, cars_ansc2d.d))

        cars_pcainv = anscombe.cars_invanscombe(cars_pca, gauss_std)

        bkfreecars = EmptyClass()
        bkfreecars.s1 = np.reshape(cars_pcainv.s1, (cars_ansc2d.a, cars_ansc2d.b, cars_ansc2d.c, cars_ansc2d.d))
        bkfreecars.s2 = np.reshape(cars_pcainv.s2, (cars_ansc2d.a, cars_ansc2d.b, cars_ansc2d.c, cars_ansc2d.d))

        self.bkfreecars = bkfreecars

        psfreecars = pf.remove_stokespump(self.bkfreecars, self.stokes, self.pump)
        psfreeetal = pf.remove_stokespump(self.etalon, self.etstokes, self.etpump)

        [self.etfree, self.etSumfree] = pf.remove_etaloning(self.bkfreecars, psfreecars, psfreeetal)

        aid_xnr_plot = np.squeeze(np.mean(np.mean((self.etSumfree.s2 - self.etSumfree.s1), 1), 0))
        self.normalisation_spectrum_win.clear()
        self.normalisation_spectrum_win.plot(aid_xnr_plot)

        self._message('Please set the desired NRB region for the Xnr image:')

        self.show_idle()

    def enter_nrb_region(self):
        self.show_busy()

        class EmptyClass:
            def __init__(self):
                pass

        nrb_min = int(self.nrb_no_min.text())
        nrb_max = int(self.nrb_no_max.text())

        self._message('')

        [a, b, c, d] = self.etfree.s1.shape

        nrb_sum_im = np.squeeze(np.mean(self.etSumfree.s2[:, :, :, int(nrb_min):int(nrb_max)], 3)) - np.squeeze(
            np.mean(self.etSumfree.s1[:, :, :, int(nrb_min):int(nrb_max)], 3))

        nrb_sum_im = nrb_sum_im + np.ceil(np.abs(np.min(np.min(nrb_sum_im))))

        xnr_image = np.sqrt(nrb_sum_im)

        xnrfree1 = np.full((a, b, c, d), 0, dtype='float')
        xnrfree2 = np.full((a, b, c, d), 0, dtype='float')

        if c is 1:
            for ai in range(0, a):
                for bi in range(0, b):
                    for ci in range(0, c):
                        xnrfree1[ai, bi, ci, :] = (np.squeeze(self.etfree.s1[ai, bi, ci, :])) / xnr_image[ai, bi]
                        xnrfree2[ai, bi, ci, :] = (np.squeeze(self.etfree.s2[ai, bi, ci, :])) / xnr_image[ai, bi]
        elif c > 1:
            for ai in range(0, a):
                for bi in range(0, b):
                    for ci in range(0, c):
                        xnrfree1[ai, bi, ci, :] = (np.squeeze(self.etfree.s1[ai, bi, ci, :])) / xnr_image[ai, bi, ci]
                        xnrfree2[ai, bi, ci, :] = (np.squeeze(self.etfree.s2[ai, bi, ci, :])) / xnr_image[ai, bi, ci]

        normcars = EmptyClass()
        normcars.s1 = xnrfree1
        normcars.s2 = xnrfree2

        self.normcars = normcars
        self.normcars_im_track1 = np.squeeze(np.mean(self.normcars.s1, 3))
        self.normcars_im_track2 = np.squeeze(np.mean(self.normcars.s2, 3))
        self.normcars_im_sum = np.squeeze(np.mean((self.normcars.s1 + self.normcars.s2), 3))
        self.normcars_im_sipcars = np.squeeze(np.mean((self.normcars.s2 - self.normcars.s1), 3))
        self.normcars_pl_track1 = np.squeeze(np.mean(np.mean(self.normcars.s1, 1), 0))
        self.normcars_pl_track2 = np.squeeze(np.mean(np.mean(self.normcars.s1, 1), 0))
        self.normcars_pl_sum = np.squeeze(np.mean(np.mean((self.normcars.s1 + self.normcars.s2), 1), 0))
        self.normcars_pl_sipcars = np.squeeze(np.mean(np.mean((self.normcars.s2 - self.normcars.s1), 1), 0))

        # TODO Insert some sort of indicator to show that the data has been normalised

        self.show_idle()

    def load_norm_files(self, type):
        self.show_busy()

        if type == 'pump':
            file_pump = tkinter.filedialog.askopenfilename(initialdir='E:/KCL/PhD/Data', defaultextension='.cars')
            file_pump_bk = file_pump[:-5] + '_fl_traces.cars'

            self.pump_file_name.setText(file_pump)
            pump_data = pf.process_cars(file_pump)
            pump_bk_data = pf.process_fl(file_pump_bk)

            pump = pf.remove_background(pump_data, pump_bk_data)

        elif type == 'stokes':
            file_stokes = tkinter.filedialog.askopenfilename(initialdir='E:/KCL/PhD/Data', defaultextension='.cars')
            file_stokes_bk = file_stokes[:-5] + '_fl_traces.cars'

            self.stokes_file_name.setText(file_stokes)
            stokes_data = pf.process_cars(file_stokes)
            stokes_bk_data = pf.process_fl(file_stokes_bk)

            stokes = pf.remove_background(stokes_data, stokes_bk_data)

        elif type == 'etalon':
            file_etalon = tkinter.filedialog.askopenfilename(initialdir='E:/KCL/PhD/Data', defaultextension='.cars')
            file_etalon_bk = file_etalon[:-5] + '_fl_traces.cars'

            self.etalon_file_name.setText(file_etalon)
            etalon_data = pf.process_cars(file_etalon)
            etalon_bk_data = pf.process_fl(file_etalon_bk)

            etalon = pf.remove_background(etalon_data, etalon_bk_data)

        elif type == 'etpump':
            file_etpump = tkinter.filedialog.askopenfilename(initialdir='E:/KCL/PhD/Data', defaultextension='.cars')
            file_etpump_bk = file_etpump[:-5] + '_fl_traces.cars'

            self.etalonpump_file_name.setText(file_etpump)
            etpump_data = pf.process_cars(file_etpump)
            etpump_bk_data = pf.process_fl(file_etpump_bk)

            etpump = pf.remove_background(etpump_data, etpump_bk_data)

        elif type == 'etstokes':
            file_etstokes = tkinter.filedialog.askopenfilename(initialdir='E:/KCL/PhD/Data', defaultextension='.cars')
            file_etstokes_bk = file_etstokes[:-5] + '_fl_traces.cars'

            self.etalonstokes_file_name.setText(file_etstokes)
            etstokes_data = pf.process_cars(file_etstokes)
            etstokes_bk_data = pf.process_fl(file_etstokes_bk)

            etstokes = pf.remove_background(etstokes_data, etstokes_bk_data)

        self.show_idle()

    # Functions for unsupervised clustering
    # TODO Need to implement way of checking whether to run on raw or normalised data
    def run_pca_clustering(self):
        from sklearn.decomposition import PCA as pca

        comp_no_required = int(self.pca_cluster_comp_no.text())
        bkfreecars_2d = anscombe.tran4d_2d(self.bkfreecars)

        if self.pca_cluster_whiten.checkState is True:
            pca_model = pca(n_components=comp_no_required, whiten=True)

        elif self.pca_cluster_whiten.checkState is False:
            pca_model = pca(n_components=comp_no_required, whiten=False)

        self.pca_clusterW = pca_model.fit_transform(bkfreecars_2d.s2 - bkfreecars_2d.s1)
        self.pca_clusterH = pca_model.components_

        yi, xi, zi, si = self.bkfreecars.shape
        self.pca_clusterW = np.reshape(self.pca_clusterW, (yi, xi, comp_no_required))

        self.pca_cluster_choose.setValue(1)
        self.pca_cluster_choose.setMinimum(1)
        self.pca_cluster_choose.setMaximum(comp_no_required)

        self.pca_cluster_image_win.setImage(self.pca_clusterW[:, :, 0])
        self.pca_cluster_spectrum_win.plot(self.pca_clusterH[:, 0])



    def run_kpca_clustering(self):
        pass

    def run_ica_clustering(self):
        pass

    def run_nnmf_clustering(self):
        pass

    # Functions to show busy/idle state of the software
    def show_busy(self):
        self.show_state.setStyleSheet("background: #4a1b15")
        self.show_state_text.setText('Busy')

        # self.statusBar().clearMessage()
        # self.statusBar().showMessage(self, 'Busy...', 2000)

    def show_idle(self):
        self.show_state.setStyleSheet("background: #323e30")
        self.show_state_text.setText('Idle')

        # self.statusBar().clearMessage()
        # self.statusBar().showMessage('Idle')

    # Error message function
    def _message(self, errorm):
        self.error_text.setText(errorm)


def main():
    app = QApplication(sys.argv)
    form = DataViewer()
    form.setWindowTitle('Hyperspectral Data Viewer')
    form.show()
    sys.exit(app.exec_())

# If the file is run directly and not imported, this runs the main function
if __name__ == '__main__':
    # Initiallising the c.elegans cars data as the default data to display
    # cars = np.load('default_carsarray.npy')
    main()