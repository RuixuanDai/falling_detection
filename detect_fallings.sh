# bash detect_fallings.sh 1.3 1 2.2 1 normal_activity.json
window_length=2
#thys=("2.0" "2.4" "2.6")
thys=("1.8")
thsmvs=("1.0" "1.1")
#th_y_recovery=$3
#th_smv_recovery=$4
normal_file="normal_activity.json"
falling_file="falling.json"
for th_y in "${thys[@]}"
do
    for th_smv in "${thsmvs[@]}"
    do
        output_file="${th_y}_${th_smv}.out"
        echo $output_file

        #for file in data/raw/testdata/normal*.csv
        for file in trim_new_device/*.csv
        do
            echo $file
            python algorithm_old.py --filename "$file" --window_length $window_length --th_y $th_y --th_smv $th_smv --testfile $normal_file | grep -v "only normal" >> $output_file
        done

        #for file in data/raw/testdata/falling*.csv
        #do
        #    python algorithm_old.py --filename "$file" --window_length $window_length --th_y $th_y --th_smv $th_smv --testfile $falling_file | grep -v "only normal">> $output_file
        #done
    done
done
