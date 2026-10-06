Installation:
pip install pytest-xdist

Commands :
Parallel execution - 
pytest -n 2 # It picks all the tests and starts the execution with 2 threads
pytest tests -m sanity -n 2 # It starts 2 threads, picks all the test methods available in tests with sanity tag
pytest tests -m sanity -n auto # It starts the threads based on the cpu cores

Sequential execution-
runs only the markers
pytest -m smoke

run the test has both sanity and smoke
pytest -m "sanity and regression"

run the tests are having sanity or regression
pytest -m "sanity or regression"

run the tests which are not having the regression
pytest -m "not regression"

combine multiple conditions
pytest -m "(smoke or sanity) and not regression"

Generate HTML report
pytest --html=report.html

Shows fixtures
pytest --fixtures

Run matching tests
pytest -k keyword

