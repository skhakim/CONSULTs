DBNAME="DB_"
for f in tol_genomes/*32_mer_counts_dumps.fa; do
    ./main_map -i $f -o "${DBNAME}_/$f"
    echo "$f done."
done
