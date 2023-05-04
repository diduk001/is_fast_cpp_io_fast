if [ ! -d outputs ]
then
    mkdir outputs
fi

for binary_file in bin/*; do
    filename="${binary_file##*/}"
    echo "Running $binary_file"
    $binary_file | tail -n 1 > outputs/$filename.out
    cat outputs/$filename.out
done