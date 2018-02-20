GENERATED_FILES = finished/html_report.html finished/report.pdf

all: clean $(GENERATED_FILES)

finished/report.pdf: finished/html_report.html
	xhtml2pdf $< $@
	open -n $@

finished/html_report.html: templates/template.html
	cat $< | python3 processors/generate_html_report.py > $@
	open -n $@

clean:
	rm -rf finished/*
