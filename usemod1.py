from liberty.claims import libertylib

libertylib.make_claim()
libertylib.check_coverage()

print(libertylib.STATES)

import sys
for path in sys.path:
    print(path)

# sys.path =
# CURRENT FOLDER
# +
# folders in PYTHONPATH
# +
# <prefix>/lib
