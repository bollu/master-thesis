.PHONY: thesis-20161105.pdf abstract.pdf clean


thesis-20161105.pdf: thesis-20161105.tex
	pdflatex -shell-escape thesis-20161105.tex
	bibtex thesis-20161105
	pdflatex -shell-escape thesis-20161105.tex
	pdflatex -shell-escape thesis-20161105.tex


spag: thesis-20161105.tex
	# allowed to fail since it throws error if we have grammar mistakes
	-textidote --check en_UK --output html thesis-20161105.tex > index.html
	python3 -m http.server

abstract.pdf:
	pdflatex -shell-escape abstract.tex


clean:
	-rm *.aux *.lof *.log *.lot *.fls *.out *.toc *.fmt *.fot *.cb *.cb2 *.dvi *.xdv *-converted-to.* *.bbl *.bcf *.blg *-blx.aux *-blx.bib *.run.xml

