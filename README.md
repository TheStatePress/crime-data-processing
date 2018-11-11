Extract monthly crime report PDFs into clean and usable CSV for analysis

# Usage  
Getting Started:  
1. Install pipenv
2. `pipenv install`
3. `pipenv shell`
4. `cd` into the `scripts` directory

The Workflow:  
1. download all of the relevant crime reports from ASUPD into `0-raw-data`
2. run `0-rename-files.py` if necessary to standardize the file names
3. run `1-batch-process-with-tabula.py` to get tabula's best guess at turning the PDFs into CSVs
    - The data is dirty! ASUPD has been mildly inconsistent with how they format things over the years and tabula isn't perfect
    - Luckily, at the very least they've stuck to a consistent order and selection of fields
4. run `2-separate-clean-from-dirty-data.py` to split each file into clean and dirty files
    - The 'clean' file contains only rows which have values in every field
    - The 'dirty' file contains header rows and rows which tabula messed up when attempting to parse
5. Manually fix the dirty file until only clean rows remain. You'll have to delete header rows and reconcile broken rows with the original PDF
6. run `3-combine-separated-files.py` to merge the newly-cleaned 'dirty' file into the original clean file. In other words, the output of this should be >100 completely clean data files (WIP)
7. run `4-merge-all-files.py` if you want all the data in one giant CSV. Pass --year (`python3 merge-all-files.py --year`) if you want output files by year instead of all together (not implemented yet)

### You'll need Java installed for this to work.  
check https://github.com/chezou/tabula-py if it doesn't work
