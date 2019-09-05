"""
Lambdata - collection of helper funtions for Lambda School Data Science
"""

from . import add_list_to_dataframe
from . import class_example
from . import complex
from . import train_validate_test_split

import pandas as pd
import numpy as np

ZEROS = pd.DataFrame(np.zeros(50))
ONES = pd.DataFrame(np.ones(10))
