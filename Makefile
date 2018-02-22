GENERATED_FILES = finished/UHCL_pathway_comparison_report.html finished/report.pdf

all: clean $(GENERATED_FILES)

finished/report.pdf: finished/UHCL_pathway_comparison_report.html
	xhtml2pdf $< $@
	open $@

finished/UHCL_pathway_comparison_report.html: templates/template.html
	cat $< | python3 processors/generate_html_report.py > $@
	open $@

clean:
	rm -rf finished/*

finished/applicability_report.html: templates/rubric_template.html
	cat $< | python3 processors/generate_applic_report.py > $@