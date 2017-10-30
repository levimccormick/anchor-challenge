build:
	docker build -t anchor-test .

test:
		docker run --rm -it -v `pwd`/tests:/tests -v `pwd`/code:/code -w /code anchor-test
