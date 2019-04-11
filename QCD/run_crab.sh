#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

BASE=$PWD


echo "================= CMSRUN setting up CMSSW_10_2_7 ===================="| tee -a job.log
if [ -r CMSSW_10_2_7/src ] ; then 
     echo release CMSSW_10_2_7 already exists
 else
     scram p CMSSW CMSSW_10_2_7
 fi


cd CMSSW_10_2_7/src
eval `scram runtime -sh`


scram b
cd $BASE

echo "================= CMSRUN starting GS ====================" | tee -a job.log

cmsRun -j FrameworkJobReport.xml -p GS_step1.py


echo "================= CMSRUN setting up CMSSW_10_2_5 ===================="| tee -a job.log
if [ -r CMSSW_10_2_5/src ] ; then 
     echo release CMSSW_10_2_5 already exists
 else
     scram p CMSSW CMSSW_10_2_5
 fi


cd CMSSW_10_2_5/src
eval `scram runtime -sh`


scram b
cd $BASE


echo "================= CMSRUN starting RECO 1 ====================" | tee -a job.log

cmsRun -j FrameworkJobReport.xml -p DR_step1.py 
echo "-> cleaning"
rm -v GS1.root 


echo "================= CMSRUN starting RECO 2 ====================" | tee -a job.log

cmsRun -j FrameworkJobReport.xml -p DR_step2.py 
echo "-> cleaning"
rm -v DR1.root

