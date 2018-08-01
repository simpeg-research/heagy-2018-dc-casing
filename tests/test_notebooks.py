import os
import testipynb
import unittest
import numpy as np

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['notebooks']
)
IGNORE = [
    "1_DC_Flawed_Steel_Cased_Wells",
    "3_DC_Flawed_Steel_Cased_Wells_layer",
    "9_DC_Approximating_Steel_Cased_Wells_Cartesian"
]

n_ignore = 3  # so we don't run over-time on travis, randomly ignore 2 notebooks
Test = testipynb.TestNotebooks(directory=NBDIR, timeout=2800)
ignore_inds = np.random.choice(len(Test._nbnames) - len(IGNORE), n_ignore)
test_nbnames = [t for t in Test._nbnames if t not in IGNORE]
Test.ignore = IGNORE + [test_nbnames[i] for i in ignore_inds]
TestNotebooks = Test.get_tests()

if __name__ == "__main__":
    unittest.main()
