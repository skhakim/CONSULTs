DBNAME="DB_"
QUERY_FOLDER="query_set"
mkdir search_result
for f in tol_genomes/*32_mer_counts_dumps.fa; do
    ./main_search -i "${DBNAME}_/$f" -c 0 -t 24 -q "$QUERY_FOLDER"
    echo "$f done."
done

