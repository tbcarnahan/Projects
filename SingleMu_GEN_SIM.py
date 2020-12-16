# Auto generated configuration file                                             
# using:                                                                        
# Revision: 1.19                                                                
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v                                                                         
# with command line options: Configuration/Generator/python/SingleMuPt10_pythia8_cfi.py --fileout file:step1.root --mc --eventcontent FEVTDEBUG --datatier GEN-SIM --conditions auto:phase1_2021_realistic --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step GEN,SIM --geometry DB:Extended --era Run3 --python_filename SingleMu_GEN_SIM.py --no_exec -n 100                                             

import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('SIM',Run3)

# attempting to modify this file to produce a 1/pT spectrum with mu in endcap region; adding lines:                                                            

#https://github.com/msd14/GEMCode/blob/DecaroTools/GEMValidation/test/SingleMu_GEN_SIM.py#L28                              

#https://github.com/msd14/GEMCode/blob/DecaroTools/GEMValidation/test/SingleMu_GEN_SIM.py#L111-L112                                                            


# import of standard configurations                                             
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRun3RoundOptics25ns13TeVLowS\
igmaZ_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('GEMCode.GEMValidation.randomizeMuonGun') #IMPORTANT FOR eta range = can find change to range here in GEMCode/GEMValidation/python/randomizeMuonGun.py
process.load('Configuration.Generator.SingleMuFlatLogPt_100MeVto2TeV_cfi')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1000),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source                                                                  
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info                                                               
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/Generator/python/SingleMuPt10_pythia8_cfi.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition                                                             

process.FEVTDEBUGoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step1.root'),
    outputCommands = process.FEVTDEBUGEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition                                                  

# Other statements                                                              
process.XMLDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic','')

#gives full range
generator = cms.EDProducer("FlatRandomOneOverPtGunProducer",
    PGunParameters = cms.PSet(
        # This specifies range in 1/Pt                                                       
        # It coresponds to Pt = 0.1 to 2000 GeV                                              
        MinOneOverPt = cms.double(0.1),
        MaxOneOverPt = cms.double(1.),
        PartID = cms.vint32(-13),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359) ## in radians                                    
    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts              
    psethack = cms.string('single mu pt 0.1to10'),
    AddAntiParticle = cms.bool(True),
    firstRun = cms.untracked.uint32(1)
)

process.generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(10.01),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(9.99),
        ParticleID = cms.vint32(-13)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single mu pt 10')
)


# Path and EndPath definitions                                                  
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGoutput_step = cms.EndPath(process.FEVTDEBUGoutput)

# Schedule definition                                                           
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummar\
y_step,process.simulation_step,process.endjob_step,process.FEVTDEBUGoutput_step\
)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence                           
for path in process.paths:
        getattr(process,path).insert(0, process.generator)

# Customisation from command line                                               
from GEMCode.GEMValidation.randomizeMuonGun import randomizeMuonGunGEM
process = randomizeMuonGunGEM(process)

# Add early deletion of temporary data products to reduce peak memory need      
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEa\
rlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion  
