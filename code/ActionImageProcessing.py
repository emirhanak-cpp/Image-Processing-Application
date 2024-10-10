# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 02:07:09 2024

@author: Emirhan Ak
"""

import numpy as np
from skimage import filters, img_as_float
from skimage.filters import threshold_multiotsu
from skimage.color import rgb2gray, rgb2hsv
from skimage.segmentation import chan_vese
from skimage.segmentation import (morphological_chan_vese, checkerboard_level_set)
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap, QImage
from ActionEdit import EditTab
from os import remove as removeFile

class ImageProcessingTabs(EditTab):
    
    def __init__(self, sourceGraphicsView, outputGraphicsView):
        """
        Constructor of the ImageProcessingTab class.
        Inherits the EditTab class.

        Parameters
        ----------
        sourceGraphicsView : QGraphicsQ object that will display the source image.
        outputGraphicsView : QGraphicsQ object that will display the output image.

        Returns
        -------
        None.

        """
        EditTab.__init__(self, sourceGraphicsView, outputGraphicsView)
        self.__outputImage = None
        
    def rgbToGrayscale(self):
        """
        Function that converts the RGB image that was read from the computer to
        a grayscale image.

        Returns
        -------
        None.

        """
        self.__outputImage = rgb2gray(self.getImage())
        self.showOutputGraphicsView()
        
    def rgbToHsv(self):
        """
        Function that converts the RGB image that was read from the computer to
        a HSV image.

        Returns
        -------
        None.

        """
        self.__outputImage = rgb2hsv(self.getImage())
        self.setGrayImageFlag(False)
        self.showOutputGraphicsView()
        
    def multiOtsuThresholding(self):
        """
        Function that applies the Multi-Otsu Thresholding image processing method
        on the RGB image that was read from the computer.

        Returns
        -------
        None.

        """
        grayImage = rgb2gray(self.getImage())
        thr = threshold_multiotsu(grayImage)
        self.__outputImage = np.digitize(grayImage, bins = thr)
        self.showOutputGraphicsView()
        
    def chanVeseSegmentation(self):
        """
        Function that applies the Chan-Vese Segmentation image processing method
        on the RGB image that was read from the computer.

        Returns
        -------
        None.

        """
        grayImage = rgb2gray(self.getImage())
        grayImageFloat = img_as_float(grayImage)
        chanVese = chan_vese(grayImageFloat, mu = 0.25, lambda1 = 1, lambda2 = 1, tol = 1e-3, dt = 0.5, init_level_set = "checkerboard", extended_output = True)
        self.__outputImage = chanVese[0]
        self.showOutputGraphicsView()
        
    def morphologicalSnakes(self):
        """
        Function that applies the Morphological Snakes image processing method
        on the RGB image that was read from the computer.

        Returns
        -------
        None.

        """
        def evolution(tempList):
            def _storage(tempVar):
                tempList.append(np.copy(tempVar))
            return _storage
        grayImage = rgb2gray(self.getImage())
        initializeLevelSet = checkerboard_level_set(grayImage.shape, 6)
        evolutionList = []
        feedback = evolution(evolutionList)
        self.__outputImage = morphological_chan_vese(grayImage, num_iter = 35, init_level_set = initializeLevelSet, smoothing = 3, iter_callback = feedback)
        self.showOutputGraphicsView()
        
    def EdgeDetectionRoberts(self):
        """
        Function that applies the Roberts edge detection method on the RGB image
        that was read from the computer.

        Returns
        -------
        None.

        """
        grayImage = rgb2gray(self.getImage())
        self.__outputImage = filters.roberts(grayImage)
        self.showOutputGraphicsView()
        
    def EdgeDetectionSobel(self):
        """
        Function that applies the Sobel edge detection method on the RGB image
        that was read from the computer.

        Returns
        -------
        None.

        """
        grayImage = rgb2gray(self.getImage())
        self.__outputImage = filters.sobel(grayImage)
        self.showOutputGraphicsView()
        
    def EdgeDetectionScharr(self):
        """
        Function that applies the Scharr edge detection method on the RGB image
        that was read from the computer.

        Returns
        -------
        None.

        """
        grayImage = rgb2gray(self.getImage())
        self.__outputImage = filters.scharr(grayImage)
        self.showOutputGraphicsView()
        
    def EdgeDetectionPrewitt(self):
        """
        Function that applies the Prewitt edge detection method on the RGB image
        that was read from the computer.

        Returns
        -------
        None.

        """
        grayImage = rgb2gray(self.getImage())
        self.__outputImage = filters.prewitt(grayImage)
        self.showOutputGraphicsView()
        
    def showOutputGraphicsView(self):
        """
        Function that displays the processed output image on the output QGraphicsView
        object.

        Returns
        -------
        None.

        """
        self.clearOutputGraphicsView()
        plt.imsave("temporaryImage.jpg", self.__outputImage)
        self.__outputImageQt = QImage("temporaryImage.jpg")
        if self.getGrayImageFlag() == True:
            self.__outputImageQt = self.__outputImageQt.convertToFormat(QImage.Format_Grayscale8)
        self.setGrayImageFlag(True)
        self.outputScene.addPixmap(QPixmap.fromImage(self.__outputImageQt))
        self.outputGraphicsView.setScene(self.outputScene)
        removeFile("temporaryImage.jpg")
        
    def getOutputImage(self):
        """
        Functon that returns the processed output image.

        Returns
        -------
        Returns the processed output image.

        """
        return self.__outputImage
        
        
        
        
        
        
        
        
        
        
        
        
        
    