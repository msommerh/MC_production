#! /usr/bin/env python

import os, multiprocessing, math, sys
import ROOT as rt


def submitJobs(jobname, jobRange, nEvents, jobflavour, M0):
    additional = "_M"+M0
    jobname_long = jobname + additional
    path = os.getcwd()
    for i in range(jobRange[0],jobRange[1]):
       	workdir = "tmp"+jobname_long+"/job_{}".format(i)
        os.makedirs(workdir)
	os.chdir(workdir)
	   
        #write executable file for submission
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
	    fout.write("M0={}\n".format(M0))
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
	    fout.write("echo 'M0 = {}'\n".format(M0))
	    fout.write("echo '--------------------------'\n")
	    fout.write("echo '================= [LOG] GS step1 starts ===================='\n" )
	    fout.write("cmsRun GS_step1_template.py $SAMPLE $INDEX $NMAX $SEED $M0\n")
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
	    fout.write("cmsRun DR_step1_template.py ${SAMPLE}_M${M0} $INDEX\n")
	    fout.write("echo '================= [LOG] DR step1 ends ===================='\n")
	    fout.write("echo 'removing GS sample ...'\n")
	    fout.write("rm GS_${SAMPLE}_M${M0}_${INDEX}.root\n")
	    fout.write("echo '================= [LOG] DR step2 starts ===================='\n")
	    fout.write("cmsRun DR_step2_template.py ${SAMPLE}_M${M0} $INDEX\n")
	    fout.write("echo '================= [LOG] DR step2 ends ===================='\n")
	    fout.write("echo 'removing DR step1 sample ...'\n")
	    fout.write("rm DR_step1_${SAMPLE}_M${M0}_${INDEX}.root\n")
	    fout.write("mv DR_step2_${SAMPLE}_M${M0}_${INDEX}.root AOD_${SAMPLE}_M${M0}_${INDEX}.root\n")
	    fout.write("echo 'saved AOD file'\n")
	    
	    fout.write("echo 'STOP---------------'\n")
	    fout.write("echo\n")
	    fout.write("echo\n")
       
	#submit job
        os.system("chmod 755 job_%i.sh"%i )
        os.system("mv job_*.sh "+jobname_long+"_"+str(i)+".sh")
        makeSubmitFileCondor(jobname_long+"_"+str(i)+".sh", jobname_long, jobflavour)
        os.system("condor_submit submit.sub")
	print "job {} nr {} submitted".format(jobname_long, i)
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
 
  jobname = "ZPrime_to_BBar_2018"

  #indices of first and second last job
  jobRange = (0,30)

  nEvents = 1000

  #choose priority
  #jobflavour = 'espresso' #max 30min
  #jobflavour = 'microcentury' #max 1h
  #jobflavour = 'longlunch' #max 2h
  #jobflavour = 'workday' #max 8h
  jobflavour = 'tomorrow' #max 1d

  M0_list = ['1000', '1200', '1400', '1600', '1800', '2000', '2500', '3000', '3500', '4000', '4500', '5000', '5500', '6000']
  for n, M0 in enumerate(M0_list):
	if n<3:
	  	submitJobs(jobname, jobRange, nEvents, jobflavour, M0)
 
  print
  print "your jobs:"
  os.system("condor_q")
  userName=os.environ['USER']
  
  print
  print 'Done submitting jobs!'
  print
  
