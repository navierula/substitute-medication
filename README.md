### Substitute Medication
##### Code written by Navie Narula

This program outputs a file specifying appropriate medical substitutions that can be made for each perscription listed. To retrieve the file, simply type this command into your terminal once in the source directory: `python run.py`

---

Comments: I wrote a fairly simple function to complete the problem, and as instructed, spent a little less than an hour doing so. In actuality, a database structure might be necessary to avoid over-iteration so results can be returned via a simply query. In this case, looping over the apis to obtain the results were necessary because comparisons had to be made at each step to check that the appropriate substitution was being made. In the end, these results are stored in a hashmap structure so accessing elements does occur in constant time once results are returned from the function.


