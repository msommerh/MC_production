from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import time
index = int(time.time())
config = config()

config.General.requestName = 'QCD_sequence_test_'+str(index)
config.General.workArea = 'crab_sequence'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'dummyPSet.py'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 4000
config.JobType.inputFiles = ['run_crab.sh','GS_step1.py','DR_step1.py','DR_step2.py']
config.JobType.scriptExe='run_crab.sh'
#config.JobType.numCores=2

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 3
config.Data.totalUnits = 9
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = '/store/user/msommerh/'
config.Data.publication = True
config.Data.outputPrimaryDataset = 'MC_QCD_sequence_test2'
config.Data.outputDatasetTag ='AOD'

config.Site.storageSite = 'T2_CH_CSCS'
