import os
import sys

frontAssets = 'frontend/web/assets/'
frontTwig = 'frontend/runtime/Twig/cache/'
backAssets = 'backend/web/assets/'
backTwig = 'backend/runtime/Twig/cache/'
param = '*'

pathArray = [frontAssets, frontTwig, backAssets, backTwig]

for path in pathArray:
    if (os.path.isdir(path)):
        os.system("rm -rf " + path + param)
        sys.stdout.write("\033[0;32m")
        print("Success. Path " + path + " cleared successfully")
    else:
        sys.stdout.write("\033[1;31m")
        print("Error. Directory " + path + " doesn\'t exist")

sys.stdout.write("\033[0;0m")
