# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EXO-RunIIFall18wmLHEGS-00486-fragment.py --fileout file:EXO-RunIIFall18wmLHEGS-00486.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN,SIM --nThreads 3 --geometry DB:Extended --era Run2_2018 --python_filename EXO-RunIIFall18wmLHEGS-00486_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(1549620568%100) -n 2175
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

import sys
args = sys.argv

print '.............. enter GS_step1_template.py ............'

nmax = 2

#if len(args)!=8:
#    print 'Provide [sample][index][nmax][seed][minPT][maxPT]', len(args)
#    sys.exit(0)
#else:
#    sample = args[2]
#    index = args[3]
#    nmax = int(args[4])
#    seed = int(args[5])
#    minPT = args[6]
#    maxPT = args[7]
#
#
#print 'sample name = ', sample
#print 'index = ', index
#print 'nmax = ', nmax
#print 'seed = ', seed
#print 'minPT = ', minPT
#print 'maxPT = ', maxPT
#index = '0'

bin_ = 16 

bin_list = [('5','10'), ('10','15'), ('15','30'), ('30','50'), ('50','80'), ('80','120'), ('120','170'), ('170','300'), ('300','470'), ('470','600'), ('600','800'), ('800','1000'), ('1000','1400'), ('1400','1800'), ('1800','2400'), ('2400','3200'), ('3200', 'Inf')]

minPT = bin_list[bin_][0]
maxPT = bin_list[bin_][1]

sample = 'QCD_'+minPT+'to'+maxPT
seed = int(minPT)

process = cms.Process('SIM',eras.Run2_2018)

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
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nmax)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('QCD pthat {}to{} GeV, 13 TeV, TuneCUETP8M1'.format(minPT, maxPT)),
    name = cms.untracked.string('\$Source$'),
    version = cms.untracked.string('\$Revision$')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string("file:GS_" + sample  + ".root"),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v11', '')


if minPT=='5' and maxPT=='10': cross_sec = 6.10183e+10
elif minPT=='10' and maxPT=='15': cross_sec = 5.88758e+09
elif minPT=='15' and maxPT=='30': cross_sec = 1.83741e+09
elif minPT=='30' and maxPT=='50': cross_sec = 1.40932e+08
elif minPT=='50' and maxPT=='80': cross_sec = 1.92043e+07
elif minPT=='80' and maxPT=='120': cross_sec = 2.76253e+06
elif minPT=='120' and maxPT=='170': cross_sec = 4.711e+05
elif minPT=='170' and maxPT=='300': cross_sec = 117276
elif minPT=='300' and maxPT=='470': cross_sec = 7823.28
elif minPT=='470' and maxPT=='600': cross_sec = 648.174
elif minPT=='600' and maxPT=='800': cross_sec = 186.946
elif minPT=='800' and maxPT=='1000': cross_sec = 32.2928
elif minPT=='1000' and maxPT=='1400': cross_sec = 9.41832
elif minPT=='1400' and maxPT=='1800': cross_sec = 0.84265
elif minPT=='1800' and maxPT=='2400': cross_sec = 0.114943
elif minPT=='2400' and maxPT=='3200': cross_sec = 0.00682981
elif minPT=='3200' and maxPT=='Inf': cross_sec = 0.000165445
else: raise ValueError("pt bin does not match predefined selection")

if maxPT == "Inf": params = cms.vstring('HardQCD:all = on', 'PhaseSpace:pTHatMin = 3200  ',)
else: params = cms.vstring('HardQCD:all = on','PhaseSpace:pTHatMin = {}  '.format(minPT),'PhaseSpace:pTHatMax = {}  '.format(maxPT),)

#QCD generator
process.generator = cms.EDFilter("Pythia8GeneratorFilter",
        maxEventsToPrint = cms.untracked.int32(1),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        filterEfficiency = cms.untracked.double(1.0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        comEnergy = cms.double(13000.0),


        crossSection = cms.untracked.double(cross_sec),

        PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CUEP8M1SettingsBlock,
            processParameters = params,
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CUEP8M1Settings',
                                        'processParameters',
                                        )
        )
)

process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(int(seed))


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(2)
process.options.numberOfStreams=cms.untracked.uint32(0)
# filter all path with the production filter sequence

for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
