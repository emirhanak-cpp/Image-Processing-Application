# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:11:18 2024

@author: Emirhan Ak
"""

from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
from skimage import io
import matplotlib.pyplot as plt

class FileTab:
    
    def __init__(self, sourceGraphicsView, outputGraphicsView):
        """
        Constructor of the FileTab class

        Parameters
        ----------
        sourceGraphicsView : QGraphicsQ object that will display the source image.
        outputGraphicsView : QGraphicsQ object that will display the output image.

        Returns
        -------
        None.

        """
        self.image = None
        self.fileOpenPath = None
        self.fileSavePath = None
        self.sourceScene = QGraphicsScene()
        self.outputScene = QGraphicsScene()
        self.sourceGraphicsView = None
        self.outputGraphicsView = None
        self.grayImageFlag = True
        self.setSourceGraphicsView(sourceGraphicsView, outputGraphicsView)
        
    def openFile(self):
        """
        Function that enables to open files

        Returns
        -------
        None.

        """
        self.clearSourceGraphicsView()
        self.clearOutputGraphicsView()
        self.fileOpenPath, self.extension = QFileDialog.getOpenFileName(caption = "Open", filter = "JPG Files (*.jpg);; PNG Files (*.png);; JPEG Files (*.jpeg)")
        self.image = io.imread(self.fileOpenPath)
        self.imageQt = QImage(self.fileOpenPath)
        self.sourceScene.addPixmap(QPixmap.fromImage(self.imageQt))
        self.sourceGraphicsView.setScene(self.sourceScene)
        
    def sourceExport(self):
        """
        Function that exports the source file

        Returns
        -------
        None.

        """
        self.fileSavePath,_ = QFileDialog.getSaveFileName(caption = "Save", filter = "JPG Files (*.jpg);; PNG Files (*.png);; JPEG Files (*.jpeg)")
        plt.imsave(self.fileSavePath, self.image)
        
    def outputSave(self, outputImage):
        """
        Function that saves the output file

        Parameters
        ----------
        outputImage : The function receives the output image that the user wants to save.

        Returns
        -------
        None.

        """
        if self.getGrayImageFlag() == True:
            plt.imsave(self.fileOpenPath, outputImage, cmap = "gray")
        else:
            plt.imsave(self.fileOpenPath, outputImage)
        
    def outputSaveAs(self, outputImage):
        """
        Function that saves the output file with a different name

        Parameters
        ----------
        outputImage : The function receives the output image that the user wants to save.

        Returns
        -------
        None.

        """
        self.fileSavePath,_ = QFileDialog.getSaveFileName(caption = "Save As", filter = self.extension)
        if self.getGrayImageFlag() == True:
            plt.imsave(self.fileSavePath, outputImage, cmap = "gray")
        else:
            plt.imsave(self.fileSavePath, outputImage)
        
    def outputExport(self, outputImage):
        """
        Function that exports the output value with a different name and format

        Parameters
        ----------
        outputImage : The function receives the output image that the user wants to save.

        Returns
        -------
        None.

        """
        self.fileSavePath,filter_ = QFileDialog.getSaveFileName(caption = "Export As", filter = "JPG Files (*.jpg);; PNG Files (*.png);; JPEG Files (*.jpeg)")
        if self.getGrayImageFlag() == True:
            plt.imsave(self.fileSavePath, outputImage, cmap = "gray")
        else:
            plt.imsave(self.fileSavePath, outputImage)
        
    def getImage(self):
        """
        Function that returns the image file that was read from the computer

        Returns
        -------
        Returns the image file that was read from the computer

        """
        return self.image
    
    def setSourceGraphicsView(self, sourceGraphicsView, outputGraphicsView):
        """
        Function that sets source and output QGraphicsView objects.
        Only called by the __init__() function.

        Parameters
        ----------
        sourceGraphicsView : QGraphicsQ object that will display the source image.
        outputGraphicsView : QGraphicsQ object that will display the output image.

        Returns
        -------
        None.

        """
        self.sourceGraphicsView = sourceGraphicsView
        self.outputGraphicsView = outputGraphicsView
        
    def getSourceGraphicsView(self):
        """
        Function that returns the source QGraphicsView object.

        Returns
        -------
        Returns the source QGraphicsView object.

        """
        return self.sourceGraphicsView
    
    def getOutputGraphicsView(self):
        """
        Function that returns the output QGraphicsView object.

        Returns
        -------
        Returns the output QGraphicsView object.

        """
        return self.outputGraphicsView
    
    def setGrayImageFlag(self, boolValue):
        """
        Function that sets the grayImageFlag variable.

        Parameters
        ----------
        boolValue : Gets set to the grayImageFlag variable.

        Returns
        -------
        None.

        """
        self.grayImageFlag = boolValue
        
    def getGrayImageFlag(self):
        """
        Function that returns the grayImageFlag variable.

        Returns
        -------
        Returns the grayImageFlag variable.

        """
        return self.grayImageFlag
    
        
        
        
        
        
        
        