#! /bin/bash

WORD=$1
LENGTH=$2

echo $WORD

for (( c=2; c <= $LENGTH; c++ )); do
  COUNT_1=`ssh gpfs1 "/root/mumbler/count_word.py $WORD"`
  COUNT_2=`ssh gpfs2 "/root/mumbler/count_word.py $WORD"`
  COUNT_3=`ssh gpfs3 "/root/mumbler/count_word.py $WORD"`
  (( TOTAL_COUNT = COUNT_1 + COUNT_2 + COUNT_3 ))
  
  RAND_INDEX=`python -c 'import random as R; print(R.randint(1, '$TOTAL_COUNT'))'`
  if (( COUNT_1 >= RAND_INDEX )); then
    NEXT_WORD=`ssh gpfs1 "/root/mumbler/get_word.py $WORD $RAND_INDEX"`
  else
    (( RAND_INDEX -= COUNT_1 ))
    
    if (( COUNT_2 >= RAND_INDEX )); then
      NEXT_WORD=`ssh gpfs2 "/root/mumbler/get_word.py $WORD $RAND_INDEX"`
    else
      (( RAND_INDEX -= COUNT_2 ))
      NEXT_WORD=`ssh gpfs3 "/root/mumbler/get_word.py $WORD $RAND_INDEX"`
    fi
  fi
  echo $NEXT_WORD
  WORD=$NEXT_WORD
done

exit 0
