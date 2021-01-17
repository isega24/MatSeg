for i in 0 1 2 3 4 5;
do
    CUDA_VISIBLE_DEVICES=$1 python main.py uhcs-fold-$i evaluate v1 --test-folder test  &> uhcs-fold-$i.evaluate.txt
done