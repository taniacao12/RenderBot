# CodeCheck

## Exporting RPLAN Data

1. Locate and add RPLAN dataset to `data/RPLAN`

2. Run main.py
```
python main.py
```

3. Select file: input specific file name without extension or `all ` to batch run all files in directory

4. Watch the program produce files in `output/JSON` directory

## Verify Code Compliance

1. Verify JSON files in `output/JSON` directory

2. Run test
```
npm test
```

3. Select file: input specific file name without extension

4. Watch the program verify each requirement in console

## References

Wu, Wenming, Xiao-Ming Fu, Rui Tang, Yuhan Wang, Yu-Hao Qi, and Ligang Liu. 2019. “Data-driven Interior Plan Generation for Residential Buildings.” ACM Transactions on Graphics 38 (6): 1–12. https://doi.org/10.1145/3355089.3356556.