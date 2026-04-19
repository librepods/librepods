.PHONY: setup verify run scan test clean

setup:
	pip install -r requirements.txt

verify:
	python3 verify_setup.py

run:
	python3 librepods.py

scan:
	python3 librepods.py --scan

test:
	python3 -m pytest tests/ -v

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
