"""This file compares each file in a directory to determine the most similar files"""

from file_processing import Directory

DIRECTORY_PATH = ''

if __name__ == '__main__':
    directory = Directory(DIRECTORY_PATH)

    # Compare each file against each other
    directory.identify_duplicates(
        report_file='compare_all_files.csv',
        filters={},  # filters to exclude/include files from directory
        threshold=0,  # set to zero to compare all files against each other
        use_abs_path=False
    )

    # Find most relevant matches
    directory.identify_duplicates(
        report_file='most_similar_files.csv',
        filters={},
        threshold=0.5,  # set to non-zero value to only report scores above the threshold
        top_n=2,  # the top n files to return, subject to satisfying the threshold score
        use_abs_path=False
    )
