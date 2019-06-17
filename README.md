# organize-latex-output-in-folder
This is a simple python script that I keep in my directory where my latex compiler outputs files.


grabs files in in home/Latex-Documents outputted by LaTex compiler. 
For example, if we have math.aux, math.pdf,math.tex, the script creates a new directory home/Latex-Documents/math and 
 it moves all three files math.aux, math.pdf,math.tex  inside that directory
 (although it will grab other files as well as long as they are of the form math.xxx.) 
 
I used this to organize my latex documents, so that there were no loose files flying around.
