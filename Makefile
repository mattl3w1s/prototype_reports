GENERATED_FILES = finished/html_report.html finished/report.pdf

all: clean $(GENERATED_FILES)

finished/report.pdf: finished/html_report.html
	xhtml2pdf $< $@
	open $@

finished/html_report.html: templates/template.html
	cat $< | python3 processors/generate_html_report.py > $@
	open $@

clean:
	rm -rf finished/*
