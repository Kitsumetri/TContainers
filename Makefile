TEST_CMD=python -m unittest tests/SinleLinkedList_Test.py

.PHONY: test
test:
	$(TEST_CMD)
