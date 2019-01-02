import os

# print(os.path.split(os.path.realpath(__file__))[0])
def testReports_path():
    return os.path.split(os.path.realpath(__file__))[0]