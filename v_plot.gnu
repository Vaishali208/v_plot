
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
