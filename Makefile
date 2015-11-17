.PHONY: test

clean:
	rm pygit/*.pyc
	rm test/*.pyc

test:
	cd test
	@echo '/----------------------'
	nosetests
	@echo '----------------------/'
	cd ../
