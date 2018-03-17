TIME=$(shell date "+%FT%T")
OUTFILE=results/result-$(TIME).json
LOGFILE=logs/logs-$(TIME).json

run:
	python -m driver > $(OUTFILE) 2> $(LOGFILE)

jupyter:
	cd analysis; jupyter notebook
