# txt difference finder
This script compares two text files and finds the words in one file that are not present in the other file. It outputs these words to a new file.

## Usage
```bash
git clone https://github.com/mvanwinden/txt-difference-finder
cd txt-difference-finder
python txt-difference-finder.py 'path_to_sourcefile' 'path_to_comparisonfile' 'output_file'
```

where:

* **path_to_sourcefile** is the path to the text file you want to compare against the other file.
* **path_to_comparisonfile** is the path to the text file you want to compare with the source file.
* **output_file** is the path to the new file that will be created, containing the words that are in the source file but not in the comparison file.
