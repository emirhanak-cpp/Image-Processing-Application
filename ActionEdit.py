# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 01:39:58 2024

@author: Emirhan Ak
"""

from ActionFile import FileTab

class EditTab(FileTab):
    
    def __init__(self, sourceGraphicsView, outputGraphicsView):
        """
        Constructor of the EditTab class.
        Inherits the FileTab class.

        Parameters
        ----------
        sourceGraphicsView : QGraphicsQ object that will display the source image.
        outputGraphicsView : QGraphicsQ object that will display the output image.

        Returns
        -------
        None.

        """
        FileTab.__init__(self, sourceGraphicsView, outputGraphicsView)
        #self.undo = []
        #self.redo = []
        
    def clearSourceGraphicsView(self):
        """
        Function that clears the view of the source QGraphicsView object.

        Returns
        -------
        None.

        """
        self.sourceScene.clear()
        self.sourceGraphicsView.setScene(self.sourceScene)
        
    def clearOutputGraphicsView(self):
        """
        Function that clears the view of the output QGraphicsView object.

        Returns
        -------
        None.

        """
        self.outputScene.clear()
        self.outputGraphicsView.setScene(self.outputScene)

    def outputUndo(self, undoButton, undoAction, redoButton, redoAction):
        """
        Function that undoes the final operation on the output.
        NOT USED IN THE FINAL PROGRAM.

        Parameters
        ----------
        undoButton
        undoAction
        redoButton
        redoAction

        Returns
        -------
        None.

        """
        redoButton.setEnabled(True)
        redoAction.setEnabled(True)
        
        if len(self.undo) == 1:
            undoButton.setEnabled(False)
            undoAction.setEnabled(False)
        elif len(self.undo) == 2:
            self.undo[0].showOutputGraphicsView()
            self.redo.append(self.undo.pop())
            undoButton.setEnabled(False)
            undoAction.setEnabled(False)
        else:
            self.undo[-2].showOutputGraphicsView()
            self.redo.append(self.undo.pop())
            
    def outputRedo(self, undoButton, undoAction, redoButton, redoAction):
        """
        Function that redoes the final operation on the output.
        NOT USED IN THE FINAL PROGRAM.

        Parameters
        ----------
        undoButton
        undoAction
        redoButton
        redoAction

        Returns
        -------
        None.

        """
        if len(self.redo) == 1:
            self.redo[0].showOutputGraphicsView()
            self.undo.append(self.redo.pop())
            redoButton.setEnabled(False)
            redoAction.setEnabled(False)
            undoButton.setEnabled(True)
            undoAction.setEnabled(True)
        elif len(self.redo) > 1:
            self.redo[-1].showOutputGraphicsView()
            self.undo.append(self.redo.pop())
            undoButton.setEnabled(True)
            undoAction.setEnabled(True)
            
        def undoAppend(self, upperObj):
            """
            Function that appends the undo list.
            NOT USED IN THE FINAL PROGRAM.

            Parameters
            ----------
            upperObj

            Returns
            -------
            None.

            """
            self.undo.append(upperObj)
            
        def getUndo(self):
            """
            Function that return the undo list.
            NOT USED IN THE FINAL PROGRAM.

            Returns
            -------
            TYPE
                DESCRIPTION.

            """
            return self.undo
            
            
            
            
            
            