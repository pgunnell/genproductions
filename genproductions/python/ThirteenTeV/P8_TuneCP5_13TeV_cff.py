import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("Pythia8GeneratorFilter",
				 comEnergy = cms.double(13000.0),
				 crossSection = cms.untracked.double(9.573213e+08),
				 filterEfficiency = cms.untracked.double(1),
				 maxEventsToPrint = cms.untracked.int32(0),
				 pythiaHepMCVerbosity = cms.untracked.bool(False),
				 pythiaPylistVerbosity = cms.untracked.int32(0),
				 PythiaParameters = cms.PSet(
	processParameters = cms.vstring(
	'Main:timesAllowErrors    = 10000',
	'ParticleDecays:limitTau0 = on',
	'ParticleDecays:tau0Max = 10',
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
	'Tune:pp 14',
	'Tune:ee 7',
	'MultipartonInteractions:pT0Ref=2.4024',
        'MultipartonInteractions:ecmPow=0.25208',
        'MultipartonInteractions:expPow=1.6',
	),
	parameterSets = cms.vstring('processParameters')
	)
				 )

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\$Revision: 1.1 $'),
    name = cms.untracked.string('https://github.com/pgunnell/genproductions/edit/DASRivet-P8/genproductions/python/ThirteenTeV/P8_TuneCUETP8M1_13TeV_cff.py'),
    annotation = cms.untracked.string('Sample with PYTHIA8 for RIVET exercise')
)
