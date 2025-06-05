# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: to get the cound of lines in the dataset
# ========================================================================
# HEADERS
# ========================================================================

import pandas as pd

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	print("-" * 50)
	print(section_name)
	print("-" * 50)

# ========================================================================
# FUNCTIONS 
# ========================================================================





# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	df:pd.DataFrame = pd.read_csv("heartv1.csv", header=0)
	print(len(df))
	section("END")