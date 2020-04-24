import sys
sys.path.append('..')

from _tools import ProgressBarDecoratorArguments

from os import path
from PyQt5 import QtWidgets
import numpy as np


def View3D_setCAxis_button_function(self):
    if not hasattr(self, 'V'):
        self.View3D_plot_button_function()
        
    CAxisMin=float(self.ui.View3D_CAxisMin_lineEdit.text())
    CAxisMax=float(self.ui.View3D_CAxisMax_lineEdit.text())
            
    self.V.caxis=(CAxisMin,CAxisMax)

def View3D_SelectView_QxE_radioButton_function(self):
    if hasattr(self, 'V'):
        self.V.setAxis(1)
        # Redraw the title, then change the viewing plane to render properly
        self.View3D_SetTitle_button_function()
        self.V.setPlane(1)
        self.V.setPlane(0)
            
def View3D_SelectView_QyE_radioButton_function(self):
    if hasattr(self, 'V'):
        self.V.setAxis(0)
        # Redraw the title, then change the viewing plane to render properly
        self.View3D_SetTitle_button_function()
        self.V.setPlane(1)
        self.V.setPlane(0)
    
def View3D_SelectView_QxQy_radioButton_function(self):
    if hasattr(self, 'V'):
        self.V.setAxis(2)
        # Redraw the title, then change the viewing plane to render properly
        self.View3D_SetTitle_button_function()
        self.V.setPlane(1)
        self.V.setPlane(0)
    
def View3D_SetTitle_button_function(self):        
    if hasattr(self, 'V'):
        TitleText=self.ui.View3D_SetTitle_lineEdit.text()        
        self.V.ax.set_title(TitleText)
        
        # Get the value of the slider right now, then change it around a bit and put it back to where it was, to render properly
        currentSliderValue=self.V.Energy_slider.val
        self.V.Energy_slider.set_val(0)
        self.V.Energy_slider.set_val(1)
        self.V.Energy_slider.set_val(currentSliderValue)
                
@ProgressBarDecoratorArguments(runningText='Generating View3D',completedText='View3D Generated')                    
def View3D_plot_button_function(self):
    if not self.stateMachine.requireStateByName('Converted'):
        return False

    # Check if we already have data, otherwise convert current data.
    ds = self.DataSetModel.getCurrentDataSet()
    if len(ds.convertedFiles)==0:
        self.DataSet_convertData_button_function()
    
    QXBin=float(self.ui.View3D_QXBin_lineEdit.text())
    QYBin=float(self.ui.View3D_QYBin_lineEdit.text())
    EBin =float(self.ui.View3D_EBin_lineEdit.text())
    
    if self.ui.View3D_SelectUnits_RLU_radioButton.isChecked():
        rlu=True
        
    if self.ui.View3D_SelectUnits_AA_radioButton.isChecked():
        rlu=False

    if self.ui.View3D_Grid_checkBox.isChecked():
        grid=9
    else:
        grid=False
    
    if self.ui.View3D_LogScale_checkBox.isChecked():
        log=True
    else:
        log=False        
    
    self.V = ds.View3D(QXBin,QYBin,EBin,grid=grid,rlu=rlu,log=log)
    self.windows.append(self.V.ax.get_figure())
    
    # Select the correct view
    if self.ui.View3D_SelectView_QxE_radioButton.isChecked():
        self.View3D_SelectView_QyE_radioButton_function()
    if self.ui.View3D_SelectView_QyE_radioButton.isChecked():
        self.View3D_SelectView_QxE_radioButton_function()
    if self.ui.View3D_SelectView_QxQy_radioButton.isChecked():
        self.View3D_SelectView_QxQy_radioButton_function()
                
    self.View3D_setCAxis_button_function()        
    self.View3D_SetTitle_button_function()
    self.V.setPlane(1)
    self.V.setPlane(0)
    return True



def initView3DManager(guiWindow):
 
    guiWindow.View3D_setCAxis_button_function = lambda:View3D_setCAxis_button_function(guiWindow)
    guiWindow.View3D_SelectView_QxE_radioButton_function = lambda:View3D_SelectView_QxE_radioButton_function(guiWindow)
    guiWindow.View3D_SelectView_QyE_radioButton_function = lambda:View3D_SelectView_QyE_radioButton_function(guiWindow)
    guiWindow.View3D_SelectView_QxQy_radioButton_function = lambda:View3D_SelectView_QxQy_radioButton_function(guiWindow)
    guiWindow.View3D_SetTitle_button_function = lambda:View3D_SetTitle_button_function(guiWindow)
    guiWindow.View3D_plot_button_function = lambda:View3D_plot_button_function(guiWindow)



def setupView3DManager(guiWindow):
    guiWindow.ui.View3D_plot_button.clicked.connect(guiWindow.View3D_plot_button_function)
    guiWindow.ui.View3D_setCAxis_button.clicked.connect(guiWindow.View3D_setCAxis_button_function)
    guiWindow.ui.View3D_SetTitle_button.clicked.connect(guiWindow.View3D_SetTitle_button_function)
    
    # Radiobutton to select viewing type
    guiWindow.ui.View3D_SelectView_QxE_radioButton.clicked.connect(guiWindow.View3D_SelectView_QxE_radioButton_function)
    guiWindow.ui.View3D_SelectView_QyE_radioButton.clicked.connect(guiWindow.View3D_SelectView_QyE_radioButton_function)
    guiWindow.ui.View3D_SelectView_QxQy_radioButton.clicked.connect(guiWindow.View3D_SelectView_QxQy_radioButton_function)
