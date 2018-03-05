# AA_freq_to_codon_design
A tool for converting your AA frequencies into codon design.

## INSTRUCTIONS FOR USE:
1. Modify main.py with your favorite text editor (gedit, notebook, etc.) and at the end of the script change the paths:
	- First path refers to codon map, file.
	- Second path refers to aminoacid frequencies. The file should be in the same format as the 'AAFREQ.txt' provided.
	- Third path refers to the output file that will be created for the solution 'Solution.csv'. The format here refers columns to position in codon design and rows to nucleotides.
2. Install python 3.6 and Pandas package. You can do it by following the instructions at: https://www.anaconda.com/download/
	- For installing pandas you can do in your terminal: 
	> Conda install pandas
or
	> pip install pandas
3. Run the script just by typing in your terminal:
	> python main.py
