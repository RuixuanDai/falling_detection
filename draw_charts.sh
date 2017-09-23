for file in data/*.tsv
do
    python draw_line_chart.py "$file"
done
