import sys
sys.path.append('..')

try:
    from MJOLNIRGui.src.main.python._tools import ProgressBarDecoratorArguments,loadUI
    import MJOLNIRGui.src.main.python._tools as _GUItools
    from MJOLNIRGui.src.main.python.DataModels import Cut1DModel
    from MJOLNIRGui.src.main.python.MJOLNIR_Data import Gui1DCutObject
except ImportError:
    from DataModels import Cut1DModel
    from MJOLNIR_Data import Gui1DCutObject
    from _tools import ProgressBarDecoratorArguments,loadUI
    import _tools as _GUItools
from os import path
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import numpy as np
import matplotlib.pyplot as plt

def Cut1D_Delete1D_button_function(self):
    self.Cut1DModel.delete(self.ui.Cut1D_listView.selectedIndexes())
    self.update1DCutLabels()
    self.Cut1DModel.layoutChanged.emit()
    self.stateMachine.run()


def Cut1D_DoubleClick_Selection_function(self,index,*args,**kwargs):
    self.ui.Cut1D_listView.edit(index)

def setupCut1D(self):
    self.ui.Cut1D_plot_button.clicked.connect(self.Cut1D_plot_button_function)
    self.ui.Cut1D_Generate1D_button.clicked.connect(self.Cut1D_Generate1D_button_function)
    self.ui.Cut1D_Delete1D_button.clicked.connect(self.Delete1D_button_function)
    self.ui.Cut1D_SetTitle_button.clicked.connect(self.Cut1D_SetTitle_button_function)
    
    self.Cut1DModel = Cut1DModel(Cut1D_listView=self.ui.Cut1D_listView)
    self.ui.Cut1D_listView.setModel(self.Cut1DModel)

    self.Cut1DSelectionModel = self.ui.Cut1D_listView.selectionModel()
    self.Cut1DSelectionModel.selectionChanged.connect(self.selected1DCutChanged)
    
    self.ui.Cut1D_listView.doubleClicked.connect(self.Cut1D_DoubleClick_Selection_function)

    def contextMenu(view,event,gui):
        # Generate a context menu that opens on right click
        position = event.globalPos()
        idx = view.selectedIndexes()
        if len(idx)!=0:
            items = [gui.Cut1DModel.item(i) for i in idx]
            if event.type() == QtCore.QEvent.ContextMenu:
                menu = QtWidgets.QMenu()
                plot = QtWidgets.QAction('Plot')
                plot.setToolTip('Plot cut(s)') 
                plot.setStatusTip(plot.toolTip())
                plot.triggered.connect(lambda: [self.plotItem(it) for it in items])

                delete = QtWidgets.QAction('Delete')
                delete.setToolTip('Delete cut(s)') 
                delete.setStatusTip(delete.toolTip())
                delete.triggered.connect(lambda: gui.Cut1DModel.delete(idx))

                menu.addAction(plot)
                menu.addAction(delete)
                return menu.exec_(position)

    self.ui.Cut1D_listView.contextMenuEvent = lambda event: contextMenu(self.ui.Cut1D_listView,event,self)

def selected1DCutChanged(self,*args,**kwargs):
    self.update1DCutLabels()


def update1DCutLabels(self):
    cuts = self.Cut1DModel.rowCount()
    if cuts == 0:
        self.ui.Cut1D_Delete1D_button.setEnabled(False)
        self.ui.Cut1D_Export1D_button.setEnabled(False)
        self.ui.Cut1D_ExporCSV_radioButton.setEnabled(False)
        self.ui.Cut1D_ExporUFIT_radioButton.setEnabled(False)
    else:
        self.ui.Cut1D_Delete1D_button.setEnabled(True)
        self.ui.Cut1D_Export1D_button.setEnabled(True)
        self.ui.Cut1D_ExporCSV_radioButton.setEnabled(True)
        self.ui.Cut1D_ExporUFIT_radioButton.setEnabled(True)

def extractCutParameters(self):
    HStart = self.ui.Cut1D_HStart_lineEdit.text()
    HEnd = self.ui.Cut1D_HEnd_lineEdit.text()
    KStart = self.ui.Cut1D_KStart_lineEdit.text()
    KEnd = self.ui.Cut1D_KEnd_lineEdit.text()
    LStart = self.ui.Cut1D_LStart_lineEdit.text()
    LEnd = self.ui.Cut1D_LEnd_lineEdit.text()

    EMax = float(self.ui.Cut1D_EMax_lineEdit.text())
    EMin = float(self.ui.Cut1D_EMin_lineEdit.text())

    width = float(self.ui.Cut1D_Width_lineEdit.text())
    minPixel = float(self.ui.Cut1D_MinPixel_lineEdit.text())

    ds = self.DataSetModel.getCurrentDataSet()
    rlu = self.ui.Cut1D_SelectUnits_RLU_radioButton.isChecked()
    if rlu:
        q1 = np.array([HStart,KStart,LStart],dtype=float)
        q2 = np.array([HEnd,KEnd,LEnd],dtype=float)
    else:
        q1 = np.array([HStart,KStart],dtype=float)
        q2 = np.array([HEnd,KEnd],dtype=float)

    cutQ = self.ui.Cut1D_SelectCut_Q_radioButton.isChecked()

    return ds,q1,q2,width,minPixel,EMax,EMin,cutQ,rlu

@ProgressBarDecoratorArguments(runningText='Save Cut1D to folder',completedText='Cut1D saved')
def Cut1D_Export1D_button_function(self):

    asCSV = self.ui.Cut1D_ExporCSV_radioButton.isChecked()
    saveString = self.ui.Cut1D_ExportName_lineEdit.text()

    if asCSV:
        saveFolder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Save 1D cuts')

        if not saveFolder is None or saveFolder == '':
            
            if not saveString.split('.')[-1] == 'csv':
                saveString = saveString+'.csv'
            if not '#' in saveString: # Require file name to include a #
                saveString=saveString.replace('.csv','_#.csv')
            for cut in self.Cut1DModel.dataCuts1D:
                name = cut.name.replace(' ','_')
                location = path.join(saveFolder,saveString.replace('#',name))
                cut.save(location)
        else:
            return False
    else:
        if not saveString.split('.')[-1] == 'ufit':
            saveString = saveString+'.ufit'
        location,_ = QtWidgets.QFileDialog.getSaveFileName(self,'Save 1D cuts',saveString)
        if location is None or location == '':
            return False
        if not location.split('.')[-1] == 'ufit':
            location = location+'.ufit'
        
        self.Cut1D_Save_To_uFit(location)
        
        


def checker(q1,q2,width,minPixel,EMax,EMin,cutQ):
    """Checker for 1DCuts. Returns False is an error is detected."""
    success = True
    if EMax<EMin:
        _GUItools.dialog(text='1D Cut could not be made. EMax ({}) < EMin ({})!'.format(EMax,EMin))
        success = False
    if width<0:
        _GUItools.dialog(text='1D Cut could not be made. Q width ({}) is negative!'.format(width))
        success = False
    if minPixel<0:
        _GUItools.dialog(text='1D Cut could not be made. Min Pixel ({}) is negative!'.format(minPixel))
        success = False
    if not cutQ: # Cut along E
        if not np.all(np.isclose(q1,q2)):
            _GUItools.dialog(text='1D Cut could not be made. Start ({}) is not equal to End ({}) is negative!'.format(q1,q2))
            success = False
    return success


@ProgressBarDecoratorArguments(runningText='Plotting Cut1D',completedText='Plotting Done')
def Cut1D_plot_button_function(self):
    self.Cut1D_Generate1D_button_function()

    self.Cut1DModel.dataCuts1D[-1].plot() # Generates ax but does not return it -.-
    ax = plt.gca()
    self.windows.append(ax.get_figure())
    
    self.Cut1D=ax
    return True


@ProgressBarDecoratorArguments(runningText='Cutting Cut1D',completedText='Cutting Done')
def Cut1D_Generate1D_button_function(self):
    if not self.stateMachine.requireStateByName('Converted'):
        return False

    ds,q1,q2,width,minPixel,EMax,EMin,cutQ,rlu = extractCutParameters(self)
    if checker(q1,q2,width,minPixel,EMax,EMin,cutQ) is False:
        return False
    try:
        if cutQ:
            pdData,bins = ds.cut1D(q1=q1,q2=q2,width=width,minPixel=minPixel,Emin=EMin,Emax=EMax,rlu=rlu,constantBins=False,ufit=False)
            parameters = {'q1':q1,'q2':q2,'EMin':EMin,'EMax':EMax,'rlu':rlu,'width':width,'constantBins':False,'minPixel':minPixel,'method':'cut1D','dataset':ds}
        else: # else along E
            pdData,bins = ds.cut1DE(E1=EMin,E2=EMax,q=q1,rlu=rlu,width=width, minPixel = minPixel,ufit=False)
            parameters = {'EMin':EMin,'EMax':EMax,'q1':q1,'q2':None,'rlu':rlu,'width':width,'minPixel':minPixel,'method':'cut1DE','dataset':ds}
            
        
        # Generate a Gui1DCutObject
        if not hasattr(self,'cutNumber'):
            self.cutNumber = 1
        gui1DCut = Gui1DCutObject(name='Cut {}'.format(self.cutNumber),parameters=parameters,pdData=pdData,bins=bins)
        
        self.cutNumber+=1
        self.Cut1DModel.append(gui1DCut)
    except AttributeError as e:
        raise e
        #_GUItools.dialog(text='1D Cut could not be made. Check the limits for the cut and try again!')
        return False


def Cut1D_SetTitle_button_function(self):
    TitleText=self.ui.Cut1D_SetTitle_lineEdit.text()        
    if hasattr(self, 'Cut1D'):
        TitleText=self.ui.Cut1D_SetTitle_lineEdit.text()        
        self.Cut1D.set_title(TitleText)
        fig = self.Cut1D.get_figure()
        fig.canvas.draw()


def Cut1D_toggle_units_function(self):
    if self.ui.Cut1D_SelectUnits_RLU_radioButton.isChecked(): # changed to RLU
        # Change titles
        self.ui.Cut1D_Hlabel.setText('H')
        self.ui.Cut1D_Klabel.setText('K')
        self.ui.Cut1D_Llabel.setText('L')
        self.ui.Cut1D_LStart_lineEdit.setEnabled(True)
        self.ui.Cut1D_LEnd_lineEdit.setEnabled(True)
    else: # Changing to AA
        self.ui.Cut1D_Hlabel.setText('Qx')
        self.ui.Cut1D_Klabel.setText('Qy')
        self.ui.Cut1D_Llabel.setText('N/A')
        self.ui.Cut1D_LStart_lineEdit.setEnabled(False)
        self.ui.Cut1D_LEnd_lineEdit.setEnabled(False)


#@ProgressBarDecoratorArguments(runningText='Saving to file',completedText='Saving Done')
def Cut1D_Save_To_uFit(self,saveFile):
    from ufit.gui.session import UfitSession
    from ufit.gui.scanitem import ScanDataItem
    if self.Cut1DModel.rowCount() == 0:
        return

    datasets = self.Cut1DModel.dataCuts1D
    for data in datasets:
        data.ufit.meta['title'] = data.name
    
    #if not hasattr(self,'ufitsaveFile'):
    #    folder = path.dirname(self.loadedSettingsFile)
    #    fileName = path.join(folder,datasets[0].uFitDataset.meta['title']+'.ufit')
    #self.ufitsaveFile = fileName
    #
    #saveFile,_ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',self.ufitsaveFile)

    self.ufitsaveFile = saveFile
    session = UfitSession()
    session.add_items([ScanDataItem(data.ufit) for data in datasets])

    if saveFile is None or saveFile == '':
        return False

    if not saveFile.split('.')[-1] == 'ufit':
        saveFile+='.ufit'

    session.set_filename(saveFile)
    session.save()


def plotItem(self,item):
    #plot the selected Gui1DCutObject into a new window
    fig = plt.figure()
    ax = fig.gca()
    item.plot(ax=ax)
    fig.tight_layout()
    self.windows.append(fig)


# if platform.system() == 'Darwin':
#     folder = path.abspath(path.join(path.dirname(__file__),'..','..','Resources','Views'))
# else: 
#     folder = path.join(path.dirname(__file__),'..','..','resources','base','Views')

# try:
#     Cut1DManagerBase, Cut1DManagerForm = uic.loadUiType(path.join(path.dirname(__file__),"Cut1D_new.ui"))
# except:
#     Cut1DManagerBase, Cut1DManagerForm = uic.loadUiType(path.join(folder,"Cut1D_new.ui"))

Cut1DManagerBase, Cut1DManagerForm = loadUI('Cut1D_new.ui')
#try:
#    Cut1DManagerBase, Cut1DManagerForm = uic.loadUiType(path.join(path.dirname(__file__),"Cut1D_new.ui"))
#except:
#    try:
#        Cut1DManagerBase, Cut1DManagerForm = uic.loadUiType(path.join(path.dirname(__file__),'..','..','resources','base','Views',"Cut1D_new.ui"))
#    except:
#        Cut1DManagerBase, Cut1DManagerForm = uic.loadUiType(path.join(path.dirname(__file__),'..','resources','base','Views',"Cut1D_new.ui"))
class Cut1DManager(Cut1DManagerBase, Cut1DManagerForm):
    def __init__(self, parent=None, guiWindow=None):
        super(Cut1DManager, self).__init__(parent)
        self.setupUi(self)
        self.guiWindow = guiWindow
        self.initCut1DManager()

    def initCut1DManager(self):
        self.guiWindow.Cut1D_plot_button_function = lambda: Cut1D_plot_button_function(self.guiWindow)
        self.guiWindow.Cut1D_Generate1D_button_function = lambda: Cut1D_Generate1D_button_function(self.guiWindow)
        self.guiWindow.Cut1D_SetTitle_button_function = lambda: Cut1D_SetTitle_button_function(self.guiWindow)
        self.guiWindow.setupCut1D = lambda: setupCut1D(self.guiWindow)
        self.guiWindow.Cut1D_toggle_units_function = lambda: Cut1D_toggle_units_function(self.guiWindow)
        self.guiWindow.Cut1D_Save_To_uFit = lambda location: Cut1D_Save_To_uFit(self.guiWindow,location)

        self.guiWindow.plotItem = lambda item: plotItem(self.guiWindow,item)

        
        self.guiWindow.Cut1D_DoubleClick_Selection_function = lambda index:Cut1D_DoubleClick_Selection_function(self.guiWindow,index)
        self.guiWindow.Delete1D_button_function = lambda:Cut1D_Delete1D_button_function(self.guiWindow)
        self.guiWindow.selected1DCutChanged = lambda : selected1DCutChanged(self.guiWindow)
        self.guiWindow.update1DCutLabels = lambda:update1DCutLabels(self.guiWindow)
        self.guiWindow.Cut1D_Export1D_button_function = lambda:Cut1D_Export1D_button_function(self.guiWindow)
        for key,value in self.__dict__.items():
                if 'Cut1D' in key:
                    self.guiWindow.ui.__dict__[key] = value
        
    def setup(self):
        self.guiWindow.setupCut1D()
        self.guiWindow.ui.Cut1D_SelectUnits_RLU_radioButton.toggled.connect(self.guiWindow.Cut1D_toggle_units_function)
        #self.guiWindow.ui.Cut1D_fit_button.clicked.connect(self.guiWindow.Cut1D_Save_To_uFit)
        self.guiWindow.ui.Cut1D_Export1D_button.clicked.connect(self.guiWindow.Cut1D_Export1D_button_function)

        self.guiWindow.ui.Cut1D_SetTitle_lineEdit.returnPressed.connect(self.TitleChanged)
    
    
    def TitleChanged(self):
        if self.guiWindow.ui.Cut1D_SetTitle_button.isEnabled():
            self.guiWindow.Cut1D_SetTitle_button_function()