import os
import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
class ProducerTestCustomize(object):

    def __init__(self,*args,**kwargs):
        
        super(ProducerTestCustomize,self).__init__()
    
        self.options = VarParsing.VarParsing()
        
        self.options.register ('fileNames',
                                "", # default value
                               VarParsing.VarParsing.multiplicity.list, # singleton or list
                               VarParsing.VarParsing.varType.string,          # string, int, or float
                               "fileNames")
        self.options.register ('datasetName',
                               "", # default value
                               VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                               VarParsing.VarParsing.varType.string,          # string, int, or float
                               "datasetName")
        self.options.register ('processType',
                               "", # default value
                               VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                               VarParsing.VarParsing.varType.string,          # string, int, or float
                               "processType")
        self.options.register('debug',
                              0, # default value
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.int,          # string, int, or float
                              "debug")
        self.options.register('hlt',
                              0, # default value
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.int,          # string, int, or float
                              "hlt")
        self.options.register('muMuGamma',
                              2, # 0 never, 1 always, 2 for DY and DoubleMuon
                              VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                              VarParsing.VarParsing.varType.int,          # string, int, or float
                              "muMuGamma")
        self.options.register ('globalTag',
                               "", # default value
                               VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                               VarParsing.VarParsing.varType.string,          # string, int, or float
                               "globalTag")
        self.options.register ('timing',
                               0,
                              VarParsing.VarParsing.multiplicity.singleton,
                              VarParsing.VarParsing.varType.int,
                               'timing')
        self.options.register ('puppi',
                               0,
                              VarParsing.VarParsing.multiplicity.singleton,
                              VarParsing.VarParsing.varType.int,
                               'puppi')
        self.options.register ('bunchSpacing',
                               25,
                               VarParsing.VarParsing.multiplicity.singleton,
                               VarParsing.VarParsing.varType.int,
                               'bunchSpacing'
                               )
        self.options.register ('runDec2016Regression',
                               0,
                               VarParsing.VarParsing.multiplicity.singleton,
                               VarParsing.VarParsing.varType.int,
                               'runDec2016Regression'
                               )
        self.options.register('runSummer16EleID',
                              1,
                               VarParsing.VarParsing.multiplicity.singleton,
                               VarParsing.VarParsing.varType.int,
                              'runSummer16EleID'
                              )
        self.options.register('runSummer16EGMPhoID',
                              1,
                               VarParsing.VarParsing.multiplicity.singleton,
                               VarParsing.VarParsing.varType.int,
                              'runSummer16EGMPhoID'
                              )

        self.parsed_ = False

    def __getattr__(self,name):
        ## did not manage to inherit from VarParsing, because of some issues in __init__
        ## this allows to use VarParsing methods on JobConfig
        if hasattr(self.options,name):
            return getattr(self.options,name)
        
        raise AttributeError
    
    def __call__(self,process):
        self.customize(process)
        self.userCustomize(process)
    
    # empty default definition for userCustomize
    def userCustomize(self,process):
        pass 

    def parse(self):
        if self.parsed_:
            return
        self.options.parseArguments()
        self.parsed_ = True

    # process customization
    def customize(self,process):
        self.parse()
        if len(self.globalTag) >0:
            self.customizeGlobalTag(process)
        if len(self.fileNames) >0:
            self.customizeFileNames(process)
        if self.runSummer16EleID:
            self.customizeSummer16EleID(process)
        else:
            self.customizeSpring15EleID(process)
        print "Final customized process:",process.p
            

    def customizeSpring15EleID(self,process):
        from PhysicsTools.SelectorUtils.tools.vid_id_tools import DataFormat,switchOnVIDElectronIdProducer,setupAllVIDIdsInModule,setupVIDElectronSelection
        dataFormat = DataFormat.MiniAOD
        switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
        my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring15_25ns_nonTrig_V1_cff',
                         'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff',
                         'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff']
        for idmod in my_id_modules:
            setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)
            
    def customizeSummer16EleID(self,process):
        from PhysicsTools.SelectorUtils.tools.vid_id_tools import DataFormat,switchOnVIDElectronIdProducer,setupAllVIDIdsInModule,setupVIDElectronSelection
        dataFormat = DataFormat.MiniAOD
        switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)
        my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Spring16_GeneralPurpose_V1_cff',
                         'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff',
                         'RecoEgamma.ElectronIdentification.Identification.heepElectronID_HEEPV60_cff']
        for idmod in my_id_modules:
            setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

        process.ProducerTestElectrons.effAreasConfigFile = cms.FileInPath("RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt")
        process.ProducerTestElectrons.eleVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-veto")  
        process.ProducerTestElectrons.eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-loose")
        process.ProducerTestElectrons.eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-medium")
        process.ProducerTestElectrons.eleTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Summer16-80X-V1-tight")
        process.ProducerTestElectrons.eleMVAMediumIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp90")
        process.ProducerTestElectrons.eleMVATightIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring16-GeneralPurpose-V1-wp80")
        process.ProducerTestElectrons.mvaValuesMap = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values")


    def customizeGlobalTag(self,process):
        process.GlobalTag.globaltag = self.globalTag

    def customizeFileNames(self,process):
        process.source.fileNames = cms.untracked.vstring(self.fileNames)




# customization object
customize = ProducerTestCustomize()
