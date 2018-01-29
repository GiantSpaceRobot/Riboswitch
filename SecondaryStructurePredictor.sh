#!/bin/sh
# Usage: ./SecondaryStructurePredictor.sh
# Author: Paul Donovan 
# Email: pauldonovandonegal@gmail.com
# 29-Jan-2018

for file in /Directory/of/Genomes/*;
do
	echo Running secondary structure prediction on $file
	File=$(basename $file)
	name=${File%.fna}
	cmsearch -A /Directory/for/cmsearch-output/"$name.msa" /Directory/with/Covariance-Models/RF00059.cm "$file"
	sed '/^$/d' /Directory/for/cmsearch-output/"$name.msa" > /Directory/for/Edited-cmsearch-output/"$name.msa"
	sed -i 's/ \+ /\t/g' /Directory/for/Edited-cmsearch-output/"$name.msa"
	sed -n '/ RF/q;p' /Directory/for/Edited-cmsearch-output/"$name.msa" > /Directory/for/Edited-cmsearch-output/"$name.edit"
	python2.7 Riboswitch-to-FASTA.py /Directory/for/Edited-cmsearch-output/"$name.edit" /Directory/for/RNA-FASTA/"$name.rna"
	echo "Running RNAfold on RNA sequences for $File"
	for fil in /Directory/for/RNA-FASTA/*;
	do
		Fil=$(basename $fil)
		nam=${Fil%.rna}
		RNAfold -p -d2 --noLP < "$fil"  > /Directory/for/Predicted-RNA-Structures/RawOutput/"$nam.out"
		mv rna.ps /Directory/for/Predicted-RNA-Structures/PostScript/"$nam.out"
	done
done

for file in /Directory/for/Predicted-RNA-Structures/PostScript/*;
do
	echo Converting PostScript $file to PDF
	File=$(basename $file)
	name=${File%.ps}
	gs -sDEVICE=pdfwrite -sOutputFile=/Directory/for/Predicted-RNA-Structures/PDF/$name.pdf -dBATCH -dNOPAUSE $file
done