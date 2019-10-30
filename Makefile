.PHONY: test-money

test-money:
	python3 -m unittest -v money/tests/test_money.py


.PHONY: test-xunit

test-xunit:
	python3 xunit/xunit.py
