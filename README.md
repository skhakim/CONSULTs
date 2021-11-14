# CONSULT

### Minimization testing
```
./main_minimization -i k35C_bef_mininimization.fa -o k32C_af_mininimization.fa
```


### Library construction testing
```
./main_map -i k32C_af_mininimization.fa -o G000307305_nbr_map
```
This step takes about 7 min to complete. The constructed database uses ~60GB of disk space.

### Query search testing
```
./main_search -i G000307305_nbr_map -c 0 -t 1 -q query_set
```

### Family specification

```
python identify_family.py query_set/query_file
```
