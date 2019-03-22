SAMPLE="$1"
INDEX="$2"
NMAX="$3"
SEED="$4"
M0="$5"


source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630


if [ -r CMSSW_10_2_7/src ] ; then
    echo "release CMSSW_10_2_7 already exists"
else
    scram p CMSSW CMSSW_10_2_7
fi

cd CMSSW_10_2_7/src
eval `scram runtime -sh`
cd -

echo 'cmssw release = ' $CMSSW_BASE

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


if [ -r CMSSW_10_2_5/src ] ; then
    echo "release CMSSW_10_2_5 already exists"
else
    scram p CMSSW CMSSW_10_2_5
fi

cd CMSSW_10_2_5/src
eval `scram runtime -sh`
cd -

echo 'cmssw release = ' $CMSSW_BASE


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
