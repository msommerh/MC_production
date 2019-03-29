from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import FWCore.ParameterSet.Config as cms

config = config()

bin_list = [('5','10'), ('10','15'), ('15','30'), ('30','50'), ('50','80'), ('80','120'), ('120','170'), ('170','300'), ('300','470'), ('470','600'), ('600','800'), ('800','1000'), ('1000','1400'), ('1400','1800'), ('1800','2400'), ('2400','3200'), ('3200', 'Inf')]

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

minPT = bin_list[bin_][0]
maxPT = bin_list[bin_][1]

config.General.requestName = 'MC_DR2_QCD_{}to{}_0'.format(minPT,maxPT)
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
