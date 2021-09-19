import pytest


# conftest file is like a configuration file or like a setup and tear down file for an entire module
@pytest.fixture
def setUp():
    print("\n This method will run once before the pytest test case :")
    yield
    print("This method will run after every test method")


@pytest.fixture(scope='class')
def OnetimesetUP():
    print("Run this file once before every module run")

    # if browserType == 'firefox':
    #     print("Running test on FF")
    # else:
    #     print("Running test on chrome")

    yield

    print("Run this file once after every module run")


# def pytest_addoption(parser):
#     parser.addoption("--browser")

    ''' this parser will accept the argument from command line and 
    add option specify what argument the runner has to provide '''


# @pytest.fixture(scope="session")
# def browserType(request):
#     return request.config.setoption("--browser")
