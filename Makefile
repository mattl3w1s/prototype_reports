finished/report.pdf: finished/html_report.html
	xhtml2pdf $< $@ 

finished/html_report.html: templates/template.html
	cat $< | python3 processors/generate_template.py > $@

clean:
	rm -rf finished/*
