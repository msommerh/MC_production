from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import FWCore.ParameterSet.Config as cms

config = config()

M0_list = ['1000', '1200', '1400', '1600', '1800', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500', '6000']

Dataset_list = ['/MC_ZPrime_to_BBar_2018_M1000/msommerh-GEN-SIM-4a9a405e3bffdd8cb55564418d089976/USER', 
		'/MC_ZPrime_to_BBar_2018_M1200/msommerh-GEN-SIM-ac404970ceaf7c9eb944bc5c634099ed/USER',
		'/MC_ZPrime_to_BBar_2018_M1400/msommerh-GEN-SIM-85c85ff648b6eb4ec94599d39c5f2d1e/USER',
		'/MC_ZPrime_to_BBar_2018_M1600/msommerh-GEN-SIM-54d005baafc3ce12664c406971a793d3/USER',
		'/MC_ZPrime_to_BBar_2018_M1800/msommerh-GEN-SIM-24ecf076897091371720d5d597434a7a/USER',
		'/MC_ZPrime_to_BBar_2018_M2000/msommerh-GEN-SIM-565e60ab8c8eb3fe4fec679b8099864d/USER',
		'/MC_ZPrime_to_BBar_2018_M2500/msommerh-GEN-SIM-2e1e95102621a6e5f5cbb4a0111c4510/USER',
		'/MC_ZPrime_to_BBar_2018_M3000/msommerh-GEN-SIM-97cc969bf0081118c26ad60da340ce4b/USER',
		'/MC_ZPrime_to_BBar_2018_M3500/msommerh-GEN-SIM-923841a1fec767b72bc31853b06bd543/USER',
		'/MC_ZPrime_to_BBar_2018_M4000/msommerh-GEN-SIM-e9c4b70449b9dc2293f96d9966ec58f1/USER',
		'/MC_ZPrime_to_BBar_2018_M4500/msommerh-GEN-SIM-23ecefe11555da62a7f1706f8ba61fb1/USER',
		'/MC_ZPrime_to_BBar_2018_M5000/msommerh-GEN-SIM-a4f539663273f1691a728c18a9631b2b/USER',
		'/MC_ZPrime_to_BBar_2018_M5500/msommerh-GEN-SIM-244052f242a86fa671822f4e1f4d8f75/USER',
		'/MC_ZPrime_to_BBar_2018_M6000/msommerh-GEN-SIM-e3e6b4302554f2c0e16157e5f5652753/USER'] 

bin_ = 0

M0 = M0_list[bin_]

config.General.requestName = 'MC_DR1_ZPrime_to_BBar_2018_M{}_0'.format(M0)
config.General.workArea = 'crab_projects/DR1'
config.General.transferOutputs = True
config.General.transferLogs = True 

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DR_step1.py'
config.JobType.maxMemoryMB = 4000
config.JobType.numCores = 2

config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_CH*", "T2_FR*", "T2_IT*", "T2_DE*", "T2_AT*", "T2_BE*", "T2_ES*"]

config.Data.inputDataset = Dataset_list[bin_]
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'DIGI-RECO'

#config.Site.storageSite = 'T3_CH_PSI'
config.Site.storageSite = 'T2_CH_CSCS'
