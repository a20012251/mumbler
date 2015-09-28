#! /bin/bash

WORD=$1
LENGTH=$2

echo $WORD

for (( c=2; c <= $LENGTH; c++ )); do
  echo "/root/mumbler/count_word.py '$WORD'" | ssh gpfs1 > /tmp/c1 2>/dev/null
  echo "/root/mumbler/count_word.py '$WORD'" | ssh gpfs2 > /tmp/c2 2>/dev/null
  echo "/root/mumbler/count_word.py '$WORD'" | ssh gpfs3 > /tmp/c3 2>/dev/null
  COUNT_1=`cat /tmp/c1`
  COUNT_2=`cat /tmp/c2`
  COUNT_3=`cat /tmp/c3`
  TOTAL_COUNT=$(( $COUNT_1 + $COUNT_2 + $COUNT_3 ))
  
  RAND_INDEX=`python -c "import random as R; print R.randint(1, $TOTAL_COUNT)"`
  if (( COUNT_1 >= RAND_INDEX )); then
    echo "/root/mumbler/get_word.py '$WORD' $RAND_INDEX" | ssh gpfs1 > /tmp/next_word 2>/dev/null
  else
    (( RAND_INDEX -= COUNT_1 ))
    
    if (( COUNT_2 >= RAND_INDEX )); then
    echo "/root/mumbler/get_word.py '$WORD' $RAND_INDEX" | ssh gpfs2 > /tmp/next_word 2>/dev/null
    else
      (( RAND_INDEX -= COUNT_2 ))
      echo "/root/mumbler/get_word.py '$WORD' $RAND_INDEX" | ssh gpfs3 > /tmp/next_word 2>/dev/null
    fi
  fi
  NEXT_WORD=`cat /tmp/next_word`
  echo $NEXT_WORD
  WORD=$NEXT_WORD
done

exit 0
