normal_activity_file="normal_activity.json"
falling_activity_file="falling.json"
normal_activities=("Sit&Up" "Lie&Up" "Walk" "Bend&Up" "Recovery")
falling_activities=("BackwardFalling" "ForwardFalling" "LeftSideFalling" "RightSideFalling")

for activity in "${normal_activities[@]}"
do
    count1=`grep -o "$activity" $normal_activity_file | wc -l`
    count2=`grep -o "$activity" $falling_activity_file | wc -l`
    echo $activity, "$(($count1+$count2))"
done

for activity in "${falling_activities[@]}"
do
    echo grep -o "$activity" $falling_activity_file;
    grep -o "$activity" $falling_activity_file | wc -l;
done
