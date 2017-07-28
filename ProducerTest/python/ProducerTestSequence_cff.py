import FWCore.ParameterSet.Config as cms
from electrons.ProducerTest.ProducerTestElectrons_cfi import ProducerTestElectrons


#from flashgg.MicroAOD.flashggLeptonSelectors_cff import flashggSelectedMuons,flashggSelectedElectrons


from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry
from RecoEgamma.ElectronIdentification.ElectronMVAValueMapProducer_cfi import *
from RecoEgamma.PhotonIdentification.PhotonIDValueMapProducer_cfi import *
from RecoEgamma.PhotonIdentification.PhotonMVAValueMapProducer_cfi import *
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

from RecoEgamma.ElectronIdentification.egmGsfElectronIDs_cfi import *



ProducerTestSequence = cms.Sequence(   electronMVAValueMapProducer*egmGsfElectronIDs*ProducerTestElectrons#*flashggSelectedElectrons
                                        )
