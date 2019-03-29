SAMPLE="$1"
INDEX="$2"
NMAX="$3"
SEED="$4"
MINPT="$5"
MAXPT="$6"


source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

#cd /afs/cern.ch/work/m/msommerh/public/MC_samples/ZPrime_to_BBar_M4000

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
echo "minPT = $MINPT"
echo "maxPT = $MAXPT"
echo "--------------------------"

echo "================= [LOG] GS step1 starts ===================="
cmsRun GS_step1_template.py $SAMPLE $INDEX $NMAX $SEED $MINPT $MAXPT
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
cmsRun DR_step1_template.py ${SAMPLE}_${MINPT}to${MAXPT} $INDEX
echo "================= [LOG] DR step1 ends ===================="

echo "removing GS sample ..."
rm GS_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root

echo "================= [LOG] DR step2 starts ===================="
cmsRun DR_step2_template.py ${SAMPLE}_${MINPT}to${MAXPT} $INDEX
echo "================= [LOG] DR step2 ends ==========:w=========="

echo "removing DR step1 sample ..."
rm DR_step1_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root
mv DR_step2_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root AOD_${SAMPLE}_${MINPT}to${MAXPT}_${INDEX}.root
echo "saved AOD file"
