import FWCore.ParameterSet.Config as cms

microAODDefaultOutputCommand = cms.untracked.vstring("drop *",
                                                     "keep *_ProducerTestElectrons*_*_*",
                                                     )
