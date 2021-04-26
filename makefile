.PHONY: thesis-20161105.pdf clean

thesis-20161105.pdf: thesis-20161105.tex
	pdflatex -shell-escape thesis-20161105.tex


clean:
	-rm *.aux *.lof *.log *.lot *.fls *.out *.toc *.fmt *.fot *.cb *.cb2 *.dvi *.xdv *-converted-to.* *.bbl *.bcf *.blg *-blx.aux *-blx.bib *.run.xml

