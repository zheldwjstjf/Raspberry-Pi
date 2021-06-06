import os
import shutil

mycmd = "pytest --alluredir ./allureReport ./simple_code.py" 
os.system(mycmd)

shutil.rmtree("./allureReport/history")
shutil.move("allure-report/history", "./allureReport")

mycmd = "allure generate --clean allureReport" 
os.system(mycmd)

mycmd = "allure open" 
os.system(mycmd)