from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import FWCore.ParameterSet.Config as cms

config = config()

M0_list = ['1000', '1200', '1400', '1600', '1800', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500', '6000']

Dataset_list = ['/MC_ZPrime_to_BBar_2017_M1000/msommerh-GEN-SIM-491ca2d526f6687f10c21747de4d1166/USER',
		'/MC_ZPrime_to_BBar_2017_M1200/msommerh-GEN-SIM-7de7d03dd99f6daad60d6ad5f48589d8/USER',
		'/MC_ZPrime_to_BBar_2017_M1400/msommerh-GEN-SIM-4093308f0850bdebda80f01031297d6b/USER',
		'/MC_ZPrime_to_BBar_2017_M1600/msommerh-GEN-SIM-e1ebd647fdc1a298150b00c222a55265/USER',
		'/MC_ZPrime_to_BBar_2017_M1800/msommerh-GEN-SIM-d5b32718c7dac3ad9a0a5f4ff4e958cd/USER',
		'/MC_ZPrime_to_BBar_2017_M2000/msommerh-GEN-SIM-fb0bb634d4ed82511bfcf3de8b846979/USER',
		'/MC_ZPrime_to_BBar_2017_M2500/msommerh-GEN-SIM-b18a0fd05cbe03140c5b8ed328f38e75/USER',
		'/MC_ZPrime_to_BBar_2017_M3000/msommerh-GEN-SIM-b1789ac7aa80af9f7e1469746ad8900a/USER',
		'/MC_ZPrime_to_BBar_2017_M3500/msommerh-GEN-SIM-e1804c580ea52d1147fd4e7d17e2be87/USER',
		'/MC_ZPrime_to_BBar_2017_M4000/msommerh-GEN-SIM-862e73c609414bd4692add008edfea88/USER',
		'/MC_ZPrime_to_BBar_2017_M4500/msommerh-GEN-SIM-1b62dfe87131d520deafdaf0cc94d2c1/USER',
		'/MC_ZPrime_to_BBar_2017_M5000/msommerh-GEN-SIM-ce79e16d404743ecc1ce3e2a4e682f29/USER',
		'/MC_ZPrime_to_BBar_2017_M5500/msommerh-GEN-SIM-ea456823ed51b29eb25f69cf4a09c14d/USER',
		'/MC_ZPrime_to_BBar_2017_M6000/msommerh-GEN-SIM-5c63a235c3681ff55888b33d50b526e3/USER']

bin_ = 0

M0 = M0_list[bin_]

config.General.requestName = 'MC_DR1_ZPrime_to_BBar_2017_M{}_0'.format(M0)
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
