'''
    Title: Flow Tables Combine
    Purpose: Automate the joining of CSV files exported from FlowJo
    Author: Kyle Kroll
    Contact: kkroll1 (at) bidmc (dot) harvard (dot) edu
    Affiliation: Reeves Lab - Center for Virology and Vaccine Research
                 Beth Israel Deaconess Medical Center/Harvard Medical School
    https://github.com/KrollBio/FTC
'''
from os import listdir
from os.path import isfile
from os.path import join
import pandas as pd
import argparse

# Load CSV and remove the Mean and SD rows
# Split column names to remove the unneccessarily long gating paths


def load_csv(filepath):
    temp_df = pd.read_csv("{0}{1}".format(file_dir, filepath), delimiter=",")
    temp_df = temp_df.drop(temp_df[temp_df.iloc[:,0] == "Mean"].index)
    temp_df = temp_df.drop(temp_df[temp_df.iloc[:, 0] == "SD"].index)
    temp_df = temp_df.drop(labels="Unnamed: 32", axis=1)
    new_colnames = [modify_col_names(x) for x in temp_df.columns]
    new_colnames[0] = "Sample"
    temp_df.columns = new_colnames
    return(temp_df)

# Split column name and take last item in split


def modify_col_names(colnames):
    split_name = colnames.split("/")
    return(split_name[len(split_name)-1])


def main():
    csv_files = [f for f in listdir(file_dir) if isfile(join(file_dir, f))]
    list_dfs = [load_csv(x) for x in csv_files]
    concat_df = pd.concat(list_dfs, sort=False, ignore_index=True)
    concat_df.to_csv(output_file, sep=file_sep, index=False)

# Adding args to command line to specify input file directory, output file, and separator to use


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", help="Input Directory", type=str, required=True)
    parser.add_argument("--output", "-o", help="Output filename", type=str, required=True)
    parser.add_argument("--separator", "-s", help="Separator, options: [csv] [tab]", required=False, default=",", type=str)
    args = parser.parse_args()
    file_dir = args.input + "/"
    if args.separator == "csv":
        file_sep = ","
    elif args.separator == "tab":
        file_sep = "\t"
    else:
        print("Invalid file output separator supplied.")
    output_file = args.output

    main()