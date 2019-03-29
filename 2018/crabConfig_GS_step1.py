from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import FWCore.ParameterSet.Config as cms

config = config()

M0_list = ['1000', '1200', '1400', '1600', '1800', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500', '6000']

bin_ = 0

M0 = M0_list[bin_]

config.General.requestName = 'MC_ZPrime_to_BBar_2018_M{}_0'.format(M0)
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'GS_step1.py'

config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 2

config.Data.outputPrimaryDataset = 'MC_ZPrime_to_BBar_2018_M{}'.format(M0)
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 60  
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'GEN-SIM'

#config.Site.storageSite = 'T3_CH_PSI'
config.Site.storageSite = 'T2_CH_CSCS'
