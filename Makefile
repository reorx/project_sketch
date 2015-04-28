.PHONY: clean test

clean:
	rm -rf build *.egg-info

build:
	python setup.py build

test:
	PYTHONPATH=. nosetests -w test/ -v
