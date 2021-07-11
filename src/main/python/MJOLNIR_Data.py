from PyQt5 import QtCore
from MJOLNIR.Data import DataSet,DataFile,Mask
import copy
import numpy as np
#from collections import defaultdict

class GuiDataSet(DataSet.DataSet):
    def __init__(self,dataFiles=None,name='No Name',dataSet=None,background=None,**kwargs):
        if not dataSet is None:
            self.updateProperty(dataSet.__dict__)
        else:
            super(GuiDataSet,self).__init__(dataFiles=dataFiles,**kwargs)
        self.name = name
        
        # If generated by subtraction, save the background data file locations here
        self.background = background
        
        for idx,df in enumerate(self):
            df.idx = idx
        
    def setData(self,column,value):
        if column == 0: self.name = value
        
    def convertDataFile(self,dataFiles=None,binning=None,guiWindow=None,setProgressBarMaximum=True,progressUpdate=1,printFunction=None):
        """
        
        Args:

            - dataFiles (list): Files to be update. If None, use self.dataFiles (default None)

            - guiWindow (window): Current guiwindow used to access progressbar

            - setProgressBarMaximum (bool): if True, overwrite curernt progressbar max (default True)

            - progressUpdate (float): Amount to update progress bar (default 1)

            - printFunction (function): Function called with text if any is generated during conversin (Default None, -> warning)
        """
        
        dataFiles = list(self)
        if not guiWindow is None and setProgressBarMaximum:
            guiWindow.setProgressBarMaximum(len(dataFiles)+1)

        convertedFiles = []
        for _,rawfile in enumerate(dataFiles):
            convFile = rawfile.convert(printFunction=printFunction,binning=binning)
                
            convertedFiles.append(convFile)
            if not guiWindow is None:
                guiWindow.addProgressBarValue(progressUpdate)
            
        self._convertedFiles = []
        if len(convertedFiles)!=0:
            self.convertedFiles = convertedFiles    
        
        if len(self)!=0:
            self._getData()
        #if not guiWindow is None:
        #    guiWindow.setProgressBarValue(len(dataFiles))


    def flags(self):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable

    def insert(self,target_row,item,**kwargs):
        if len(self.convertedFiles)>0:
            self.dataFiles.insert(target_row,item.original_file,**kwargs)
            return self.convertedFiles.insert(target_row,item,**kwargs)
        else:
            return self.dataFiles.insert(target_row,item,**kwargs)

    def pop(self,position):
        if len(self.convertedFiles)>0:
            self.dataFiles.pop(position)
            return self.convertedFiles.pop(position)
        else:
            return self.dataFiles.pop(position)

    def append(self,files):
        convert = False # If added files should be converted
        if len(self)>0:
            if self[0].type == 'nxs':
                convert = self[0].binning
        super(GuiDataSet,self).append(files)
        for idx,df in enumerate(self):
            df.idx = idx

        if convert:
            self.convertDataFile(dataFiles=files,binning=convert)

    def updateProperty(self,dictionary):
        if isinstance(dictionary,dict):
            for key in dictionary.keys():
                self.__setattr__(key,copy.deepcopy(dictionary[key]))

    # def undoAbsolutNormalize(self):
    #     if len(self.convertedFiles)>0: # If there are converted files present, undo normalization
    #         super(GuiDataSet,self).undoAbsolutNormalize()

    #     self.normalizationSettings = {}
    #     print(self.normalizationSettings,self.currentNormalizationSettings)
        
    # def isNormalizable(self): # checks if the current data set can be normalized
    #     # If the current normalization settings are non-zero and equal to previously used values, return -1 to signify an allowance for revert of normalization
    #     if self.currentNormalizationSettings != {} and self.currentNormalizationSettings==self.normalizationSettings:
    #         return -1
    #     if self.currentNormalizationSettings == {}:
    #         return 0
    #     else:
    #         return 1

    # def absolutNormalize(self):
    #     if self.normalizationSettings == self.currentNormalizationSettings:
    #         ## Instead of normalize revert normalization
    #         self.undoAbsolutNormalize()
    #         normalizationParams = self.parent().sampleManager.getSampleInputs()
    #         self.currentNormalizationSettings.update(normalizationParams)
    #         return

    #     self.normalizationSettings.update(self.currentNormalizationSettings)

    #     raise NotImplementedError('Currently not implemented')
    #     sampleMass = self.currentNormalizationSettings['sampleMass_spinBox']
    #     units = self.sampleUnitsPerCell_spinBox
    #     gfactor = self.sampleGFactor_spinBox
    #     chemicalFormula = self.sampleFormula_lineEdit
        
    #     print("Normalized DataSet",sampleMass,units,gfactor,chemicalFormula)

    #     if hasattr(self,'SampleManager_normalizationSampleGroupBox_checkBox'):
    #         if self.SampleManager_normalizationSampleGroupBox_checkBox:
    #             #nMolarMass = self.normalizationSampleMolarMass_spinBox
    #             nChemicalFormula = self.normalizationSampleFormula_lineEdit
    #             nSampleMass = self.normalizationSampleMass_spinBox
    #             nUnits = self.normalizationSampleUnitsPerCell_spinBox
    #             nGfactor = self.normalizationSampleGFactor_spinBox
    #             nMonitor = self.normalizationMonitor_spinBox
    #             nSigma = self.normalizationSampleSigmaInc_spinBox
    #             super(GuiDataSet,self).absolutNormalize(sampleMass=sampleMass,sampleChemicalFormula=chemicalFormula,
    #             formulaUnitsPerUnitCell=units,sampleGFactor=gfactor,correctVanadium=True,vanadiumMass=nSampleMass,vanadiumChemicalFormula=nChemicalFormula,
    #             vanadiumMonitor=nMonitor,vanadiumSigmaIncoherent=nSigma,vanadiumGFactor=nGfactor,vanadiumUnitsPerUnitCell=nUnits)

    #     else:
    #         super(GuiDataSet,self).absolutNormalize(sampleMass=sampleMass,sampleChemicalFormula=chemicalFormula,
    #             formulaUnitsPerUnitCell=units,sampleGFactor=gfactor,correctVanadium=False)
                
class GuiDataFile(DataFile.DataFile):
    def __init__(self,fileLocation, **kwargs):
        self._idx = 0
        super(GuiDataFile,self).__init__(fileLocation=fileLocation,**kwargs)
        binning = 1
        calibrationIndex = list(self.possibleBinnings).index(binning) # Only binning 1 is used for raw plotting
        
        if self.instrument == 'CAMEA':
            EPrDetector = 8 
            detectors = 104
        elif self.type == 'MultiFLEXX':
            EPrDetector = 5
            detectors = 31
        elif self.type == 'FlatCone':
            EPrDetector = 1
            detectors = 31
        else:

            totalDetectors = np.array(self.instrumentCalibrations[calibrationIndex][0].shape[:-1])
            if np.mod(totalDetectors,31)==0: # either MultiFLEXX or FlatCone
                EPrDetector = int(totalDetectors/31)
                detectors = 31
            else: # CAMEA
                EPrDetector = 8 
                detectors = 104
        
        self.maxDetectorSelection = detectors
        self.maxAnalyzerSelection = EPrDetector
        self.detectorSelectionOriginal = self.detectorSelection
        self.analyzerSelectionOriginal = self.analyzerSelection

    @property
    def idx(self):
        return self._idx

    @idx.setter
    def idx(self,value):
        if self.type == 'nxs':
            self.original_file.idx = value
        else:
            self._idx = value
    
    @idx.getter
    def idx(self):
        if self.type == 'nxs':
            return self.original_file.idx
        else:
            return self._idx

    def setData(self,column,value):
        if column == 0: self.name = value

    def flags(self):
        return QtCore.Qt.ItemIsEditable

    def convert(self, printFunction,binning=None):
        if self.type == 'nxs':
            df = self.original_file
        else:
            df = self
        if binning is None:
            binning = df.binning
        convertedFile = GuiDataFile(super(GuiDataFile, df).convert(binning = binning,printFunction=printFunction))
        
        return convertedFile

class Gui1DCutObject(object):
    def __init__(self,name,parameters,pdData,bins):
        self.name = name
        self.parameters = parameters
        self._ufit = None
        self.pdData = pdData
        self.bins = bins
    
    def plot(self,*args,**kwargs):
        # redo to capitalize only first letter of the saved method (cut1D -> plotCut1D)
        plotName = 'plot'+self.parameters['method'][0].capitalize()+self.parameters['method'][1:]
        plotFunction = getattr(self.parameters['dataset'],plotName)
        if self.parameters['method'] == 'cut1D':
            #q1=q1,q2=q2,width=width,minPixel=minPixel,Emin=EMin,Emax=EMax,rlu=rlu,constantBins=False,ufit=False
            ax,*_ = plotFunction(q1=self.parameters['q1'],q2=self.parameters['q2'],rlu=self.parameters['rlu'],width=self.parameters['width'],minPixel=self.parameters['width'],
            Emin=self.parameters['EMin'],Emax=self.parameters['EMax'],data=[self.pdData,self.bins],constantBins=self.parameters['constantBins'],ufit=False,**kwargs)
        else:
            # E1=EMin,E2=EMax,q=q1,rlu=rlu,width=width, minPixel = minPixel,ufit=False
            ax,*_ = plotFunction(q=self.parameters['q1'],rlu=self.parameters['rlu'],width=self.parameters['width'],minPixel=self.parameters['width'],
            E1=self.parameters['EMin'],E2=self.parameters['EMax'],data=[self.pdData,self.bins],ufit=False,**kwargs)
        return ax
    
    def save(self,location):
        self.pdData.to_csv(location)
        

    @property
    def ufit(self):
        return self._ufit
    
    @ufit.getter
    def ufit(self):
        if self._ufit is None:
            
            self._ufit = self.parameters['dataset'].generateUFitDataset(self.pdData,q1=self.parameters['q1'],
            q2=self.parameters['q2'],rlu=self.parameters['rlu'],width=self.parameters['width'],minPixel=self.parameters['width'],
            Emin=self.parameters['EMin'],Emax=self.parameters['EMax'],QDirection=self.parameters['method']=='cut1D')
        return self._ufit
        

    

    
class GuiMask(object):
    def __init__(self,name,mask=None):

        self.name = name
        self.mask = mask
