if [ ! -d bin ]
then
    mkdir bin
fi

for source_file in sources/*.cpp; do
    filename="${source_file%%.*}"
    filename="${filename##*/}"
    
    for optimization_level in O0 O2 O3; do
        clang++ $source_file -o "bin/$filename"_$optimization_level -$optimization_level
    done
done