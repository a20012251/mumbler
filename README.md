# mumbler
A mumbler using gpfs

There are three boxes: gpfs1, gpfs2 and gpfs3. gpfs1 is the master.

The same code should be in all the machines under /root/mumbler. The only difference is that in the server.py file, line 7 should be the name of machine, e.g. gpfs2.

###server.py

It contain the common code for the rest of the scripts. Mainly file and naming handling.

###precompute_files.py

It scans all the zip files and calculates the frequency of each word in each file and produces some files with this information.
It also creates a shorter version for every zip file. It collapses all the pairs that appear in
different years in a single row and removes the columns that are not used. It reduces each zip file to a text file of around 50 MB.
It was run using a detached screen because it takes 7 hours in each box in total.

###count_word.py

```
count_word.py WORD
```

It returns the number of times a WORD appears from the list of frequencies. It uses the precomputations to speed up the count. It does not read the zip files.

###get_word.py

```
get_word.py WORD INDEX
```

It returns the pair of the word WORD that, from the frequencies, would be in index INDEX. It uses *count_word.py* to speed up the counts and read only one shortened file.

###mumbler.sh

```
mumbler.sh WORD LENGTH
```

It produces a random mumbler list starting with the word WORD and with length LENGTH. It uses ssh to call the other servers to leverage locality.
Each next word is found it at most 30 seconds, which happens when the WORD is at the end of its file.

###File Structure

The zip files are located in /gpfs/gpfsfpo/gpfsX/ where X is 1, 2 or 3. Similarly, the precomputations are located in /gpfs/gpfsfpo/gpfsX_counts/.
Each file was generated from its corresponding machine to improve network access.
