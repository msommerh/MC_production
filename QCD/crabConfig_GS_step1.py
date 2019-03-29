from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import FWCore.ParameterSet.Config as cms

config = config()

bin_ = 16

bin_list = [('5','10'), ('10','15'), ('15','30'), ('30','50'), ('50','80'), ('80','120'), ('120','170'), ('170','300'), ('300','470'), ('470','600'), ('600','800'), ('800','1000'), ('1000','1400'), ('1400','1800'), ('1800','2400'), ('2400','3200'), ('3200', 'Inf')]
minPT = bin_list[bin_][0]
maxPT = bin_list[bin_][1]

config.General.requestName = 'MC_QCD_{}to{}_0'.format(minPT,maxPT)
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GS_step1.py'
#config.JobType.pyCfgParams = ['large_test','1','5','10']

config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 2

config.Data.outputPrimaryDataset = 'MC_QCD_{}to{}'.format(minPT,maxPT)
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 600
NJOBS = 10000  
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'GEN-SIM'

#config.Site.storageSite = 'T3_CH_PSI'
config.Site.storageSite = 'T2_CH_CSCS'
