SAMPLE="$1"
INDEX="$2"
NMAX="$3"
SEED="$4"
M0="$5"


source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

if [ -r CMSSW_9_3_6 ] ; then
    echo "release CMSSW_7_1_26 already exists"
else
    scram p CMSSW CMSSW_9_3_6
fi

cd CMSSW_9_3_6/src
eval `scram runtime -sh` 
cd -


echo "--------------------------"
echo "sample name = $SAMPLE"
echo "index = $INDEX"
echo "max events = $NMAX"
echo "seed = $SEED"
echo "M0 = $M0"
echo "--------------------------"

echo "================= [LOG] GS step1 starts ===================="
cmsRun GS_step1_template.py $SAMPLE $INDEX $NMAX $SEED $M0
echo "================= [LOG] GS step1 ends ===================="

if [ -r CMSSW_9_4_0_patch1/src ] ; then
    echo "release CMSSW_8_0_21 already exists"
else
    scram p CMSSW CMSSW_9_4_0_patch1
fi

cd CMSSW_9_4_0_patch1/src
eval `scram runtime -sh`
cd -


echo "================= [LOG] DR step1 starts ===================="
cmsRun DR_step1_template.py ${SAMPLE}_M${M0} $INDEX
echo "================= [LOG] DR step1 ends ===================="

echo "removing GS sample ..."
rm GS_${SAMPLE}_M${M0}_${INDEX}.root

echo "================= [LOG] DR step2 starts ===================="
cmsRun DR_step2_template.py ${SAMPLE}_M${M0} $INDEX
echo "================= [LOG] DR step2 ends ===================="

echo "removing DR step1 sample ..."
rm DR_step1_${SAMPLE}_M${M0}_${INDEX}.root
mv DR_step2_${SAMPLE}_M${M0}_${INDEX}.root AOD_${SAMPLE}_M${M0}_${INDEX}.root
echo "saved AOD file"

