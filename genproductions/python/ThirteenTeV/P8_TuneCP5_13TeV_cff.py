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
			#Common settings P8
			'Tune:preferLHAPDF = 2',
			'Main:timesAllowErrors = 10000',
			'Check:epTolErr = 0.01',
			'Beams:setProductionScalesFromLHEF = off',
			'SLHA:keepSM = on',
			'SLHA:minMassSM = 1000.',
			'ParticleDecays:limitTau0 = on',
			'ParticleDecays:tau0Max = 10',
			'ParticleDecays:allowPhotonRadiation = on',
			#Tune CP5 parameters
			'Tune:pp 14',
			'Tune:ee 7',
			'MultipartonInteractions:ecmPow=0.03344',
			'PDF:pSet=20',
			'MultipartonInteractions:bProfile=2',
			'MultipartonInteractions:pT0Ref=1.41',
			'MultipartonInteractions:coreRadius=0.7634',
			'MultipartonInteractions:coreFraction=0.63',
			'ColourReconnection:range=5.176',
			'SigmaTotal:zeroAXB=off',
			'SpaceShower:alphaSorder=2',
			'SpaceShower:alphaSvalue=0.118',
			'SigmaProcess:alphaSvalue=0.118',
			'SigmaProcess:alphaSorder=2',
			'MultipartonInteractions:alphaSvalue=0.118',
			'MultipartonInteractions:alphaSorder=2',
			'TimeShower:alphaSorder=2',
			'TimeShower:alphaSvalue=0.118',
			),
   		parameterSets = cms.vstring('processParameters'
                                    	)
    		)
)
