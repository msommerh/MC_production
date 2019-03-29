from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import FWCore.ParameterSet.Config as cms

config = config()

M0_list = ['1000', '1200', '1400', '1600', '1800', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500', '6000']

Dataset_list = ['', 
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '']

bin_ = 0

M0 = M0_list[bin_]

config.General.requestName = 'MC_DR2_ZPrime_to_BBar_2017_M{}_0'.format(M0)
config.General.workArea = 'crab_projects/DR2'
config.General.transferOutputs = True
config.General.transferLogs = True 

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DR_step2.py'

config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 2

config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH*", "T2_FR*", "T2_IT*", "T2_DE*", "T2_AT*", "T2_BE*", "T2_ES*"]

config.Data.inputDataset = Dataset_list[bin_]
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 #might need to adjust that
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'AOD'

#config.Site.storageSite = 'T3_CH_PSI'
config.Site.storageSite = 'T2_CH_CSCS'
