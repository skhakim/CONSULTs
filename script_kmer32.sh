for f in tol_genomes/*.fna; do
    jellyfish count -m 35 -s 100M -t 10 -C $f;
    cat mer_counts.jf> "${f%%.*}_mer_counts.jf";
    jellyfish dump "mer_counts.jf"  > "${f%%.*}_mer_counts_dumps.fa";
    ./main_minimization -i "${f%%.*}_mer_counts_dumps.fa" -o "${f%%.*}_32_mer_counts_dumps.fa"
    rm -f mer_counts.jf "${f%%.*}_mer_counts_dumps.fa" "${f%%.*}_mer_counts.jf"
done
