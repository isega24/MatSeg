for i in 0 1 2 3 4 5;
do
    CUDA_VISIBLE_DEVICES=$1 python main.py uhcs-fold-$i train v1 --save &> uhcs-fold-$i.txt
done


