#! /usr/bin/env python

import os, multiprocessing, math, sys
import ROOT as rt


def submitJobs(jobname, jobRange, nEvents, jobflavour, minPT, maxPT):
    additional = str(minPT)+"to"+str(maxPT)
    jobname += additional
    path = os.getcwd()
    for i in range(jobRange[0],jobRange[1]):
       	workdir = "tmp"+jobname+"/job_{}".format(i)
        os.makedirs(workdir)
	os.chdir(workdir)
	   
	with open('job_{}.sh'.format(i), 'w') as fout:
	    fout.write("#!/bin/sh\n")
	    fout.write("echo\n")
	    fout.write("echo\n")
	    fout.write("echo 'START---------------'\n")
	    fout.write("echo 'WORKDIR ' ${PWD}\n")

	    fout.write("SAMPLE={}\n".format(jobname)) 
	    fout.write("INDEX={}\n".format(i))
	    fout.write("NMAX={}\n".format(nEvents))
	    fout.write("SEED={}\n".format(i+1))
	    fout.write("MINPT={}\n".format(minPT))
	    fout.write("MAXPT={}\n".format(maxPT))
	    fout.write("cd "+str(path)+"\n")
	    fout.write("export SCRAM_ARCH=slc6_amd64_gcc630\n" )
	    fout.write("if [ -r CMSSW_10_2_7/src ] ; then\n")
	    fout.write("    echo 'release CMSSW_10_2_7 already exists'\n")
	    fout.write("else\n")
	    fout.write("    scram p CMSSW CMSSW_10_2_7\n")
	    fout.write("fi\n")
	    fout.write("cd CMSSW_10_2_7/src\n")
	    fout.write("eval `scram runtime -sh`\n")
     	    fout.write("cd -\n" )
	    fout.write("echo 'cmssw release = ' $CMSSW_BASE\n")
	    fout.write("echo '--------------------------'\n")
	    fout.write("echo 'sample name = {}'\n".format(jobname))
	    fout.write("echo 'index = {}'\n".format(i))
	    fout.write("echo 'max events = {}'\n".format(nEvents))
	    fout.write("echo 'seed = {}'\n".format(i+1))
	    fout.write("echo 'mminPT = {}'\n".format(minPT))
	    fout.write("echo 'maxPT = {}'\n".format(maxPT))
	    fout.write("echo '--------------------------'\n")
	    fout.write("echo '================= [LOG] GS step1 starts ===================='\n" )
	    fout.write("cmsRun GS_step1_template.py $SAMPLE $INDEX $NMAX $SEED $MINPT $MAXPT\n")
	    fout.write("echo '================= [LOG] GS step1 ends ===================='\n")
	    fout.write("if [ -r CMSSW_10_2_5/src ] ; then\n")
	    fout.write("    echo 'release CMSSW_10_2_5 already exists'\n")
	    fout.write("else\n")
	    fout.write("    scram p CMSSW CMSSW_10_2_5\n")
	    fout.write("fi\n")
	    fout.write("cd CMSSW_10_2_5/src\n" )
	    fout.write("eval `scram runtime -sh`\n")
	    fout.write("cd -\n")
	    fout.write("echo 'cmssw release = ' $CMSSW_BASE\n")
	    fout.write("echo '================= [LOG] DR step1 starts ===================='\n")
	    fout.write("cmsRun DR_step1_template.py ${SAMPLE}_${MINPT}to${MAXPT} $INDEX\n")
	    fout.write("echo '================= [LOG] DR step1 ends ===================='\n")
	    fout.write("echo 'removing GS sample ...'\n")
	    fout.write("rm GS_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root\n")
	    fout.write("echo '================= [LOG] DR step2 starts ===================='\n")
	    fout.write("cmsRun DR_step2_template.py ${SAMPLE}_${MINPT}to${MAXPT} $INDEX\n")
	    fout.write("echo '================= [LOG] DR step2 ends ===================='\n")
	    fout.write("echo 'removing DR step1 sample ...'\n")
	    fout.write("rm DR_step1_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root\n")
	    fout.write("mv DR_step2_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root AOD_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root\n")
	    fout.write("echo 'saved AOD file'\n")
	    
	    fout.write("echo 'STOP---------------'\n")
	    fout.write("echo\n")
	    fout.write("echo\n")
       
        os.system("chmod 755 job_%i.sh"%i )
        os.system("mv job_*.sh "+jobname+".sh")
        makeSubmitFileCondor(jobname+".sh", jobname, jobflavour)
        os.system("condor_submit submit.sub")
	print "job {} nr {} submitted".format(jobname, i)
        os.chdir("../..")

def makeSubmitFileCondor(exe, jobname, jobflavour):
    print "make options file for condor job submission"
    submitfile = open("submit.sub", "w")
    submitfile.write("executable  = "+exe+"\n")
    submitfile.write("arguments             = $(ClusterID) $(ProcId)\n")
    submitfile.write("output                = "+jobname+".$(ClusterId).$(ProcId).out\n")
    submitfile.write("error                 = "+jobname+".$(ClusterId).$(ProcId).err\n")
    submitfile.write("log                   = "+jobname+".$(ClusterId).log\n")
    submitfile.write('+JobFlavour           = "'+jobflavour+'"\n')
    submitfile.write("queue")
    submitfile.close()
        

if __name__ == "__main__":
 
  jobname = "QCD_GRID_test"
  jobRange = (0,3)
  nEvents = 10
  #jobflavour = 'espresso'
  jobflavour = 'microcentury'
  #jobflavour = 'longlunch'
  #jobflavour = 'workday'

  pT_bins = [(5,10), (10,15), (15,30), (30,50), (50,80), (80,120), (120,170), (170,300), (300,470), (470,600), (600,800), (800,1000), (1000,1400), (1400,1800), (1800,2400), (2400,3200), (3200, 'Inf')]
  
  for pT_bin in pT_bins: submitJobs(jobname, jobRange, nEvents, jobflavour, pT_bin[0], pT_bin[1])
 
  print
  print "your jobs:"
  os.system("condor_q")
  userName=os.environ['USER']
  
  print
  print 'Done submitting jobs!'
  print
  
