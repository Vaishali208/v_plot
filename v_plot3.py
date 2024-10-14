import sys
import numpy as np
from collections import Counter

def midpoint(start, end):
    """Calculate the midpoint of a given start and end."""
    return (start + end) / 2
x_values = []
y_values =[]

xy_counts = Counter()

for line in sys.stdin:
    cols = line.strip().split()
    if len(cols) >= 12:
        
        start1, end1 = int(cols[2]), int(cols[3])
        start2, end2 = int(cols[8]), int(cols[9])
        fragment_length = int(cols[11])
        
        midpoint_1 = midpoint(start1, end1)
        midpoint_2 = midpoint(start2, end2)
        x_value = round(midpoint_1 - midpoint_2)
        
        x_values.append(x_value)
        y_values.append(fragment_length)

        xy_counts[(x_value, fragment_length)] += 1

with open('matrix_output3.txt', 'w') as f:
    for (x, y), count in xy_counts.items():
        f.write(f"{x} {y} {count}\n")

print("Matrix file 'matrix_output3.txt' generated successfully.")

gnuplot_script = """
set terminal pngcairo size 800,600 enhanced font 'Arial,10'
set output 'plot.png'

set title "V PLOT"
set xlabel "Difference of Midpoints (x-axis)"
set ylabel "Fragment Length (y-axis)"
set cblabel "Frequency(Z axis)" 

set cbrange[0:400]
set xrange [-500:500]
set yrange [0:*]


set xtics font "Arial,14"
set ytics font "Arial, 14"
set cbtics font "Arial,14"

set grid lw 0.5 lc rgb "gray"
set border lw 1.5
set palette defined (0 "white", 1 "blue", 2 "black", 3 "yellow", 4 "red")
set colorbox

plot 'matrix_output3.txt' using 1:2:3 with points palette pointsize 0.1 pointtype 7 notitle
"""

with open('v_plot.gnu', 'w') as gnuplot_file:
    gnuplot_file.write(gnuplot_script)
print("gnuplot v_plot.gnu")

