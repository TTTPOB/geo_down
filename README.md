# GEO Dataset Downloader

This Python script is used to generate an aria2c input file for downloading supplementary files from a given GEO (Gene Expression Omnibus) Series (GSE) accession number.

## Usage

The script accepts a single argument, which is the GSE accession number. To use the script, run it from the command line with the GSE number as an argument:

```bash
geo-down GSE190442
```

This will print the aria2c input file content to the console. You can redirect this output to a file if you wish:

```bash
geo-down GSE190442 > GSE190442_aria2_input.txt
```

Then, you can use the generated file as input for aria2c to download the supplementary files:

```bash
aria2c -i GSE190442_aria2_input.txt
```
