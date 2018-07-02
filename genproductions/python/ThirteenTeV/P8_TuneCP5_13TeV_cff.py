import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
				 comEnergy = cms.double(13000.0),
				 crossSection = cms.untracked.double(9.573213e+08),
				 filterEfficiency = cms.untracked.double(1),
				 maxEventsToPrint = cms.untracked.int32(0),
				 pythiaHepMCVerbosity = cms.untracked.bool(False),
				 pythiaPylistVerbosity = cms.untracked.int32(0),
				 PythiaParameters = cms.PSet(
					  pythia8CommonSettingsBlock,
 					  pythia8CP5SettingsBlock,
       		processParameters = cms.vstring(
			# Soft QCD
        		'SoftQCD:nonDiffractive = on',
	        	'SoftQCD:singleDiffractive = on',
	        	'SoftQCD:doubleDiffractive = on',
			'SoftQCD:centralDiffractive = on',
			# HardQCD
			#'HardQCD:all = on',
			#'PhaseSpace:bias2Selection = on',
			#'PhaseSpace:bias2SelectionPow = 4',
			#'PhaseSpace:pTHatMin=10',
			#'PhaseSpace:pTHatMax=6500',
			# Heavy flavour production
			#'HardQCD:hardbbbar = on',
			#'PhaseSpace:pTHatMin=10',
			#'PhaseSpace:bias2Selection = on',
			#'PhaseSpace:bias2SelectionPow = 4',
			#'PhaseSpace:pTHatMax=6500',
			# Z production
			#'WeakZ0:gmZmode=0',
			#'WeakBosonExchange:ff2ff(t:gmZ)=on',
			),
   		parameterSets = cms.vstring('pythia8CommonSettings',
                               		    'pythia8CP5Settings',
			                    'processParameters'
                                    	)
    		)
)
