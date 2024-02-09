"""This code extracts metadata from all files in a directory into a CSV report"""

from file_processing import Directory

DIRECTORY_PATH = ''

if __name__ == '__main__':
    directory = Directory(DIRECTORY_PATH)

    # Generate an analytics report (csv) on each file type and its number of files and total size
    directory.generate_analytics(
        report_file='analytics.csv',
        filters=None
    )

    # Generate a metadata report on all the files in a directory
    directory.generate_report(
        report_file='metadata.csv',
        split_metadata=True,
        filters={'exclude_str': ['.venv', '.pytest_cache', '.vscode', '__pycache__', '.git']},
        migrate_filters={'extensions': ['.csv', '.docx', '.pdf', '.pptx']},
        include_text=True,
        keywords=['Health', 'Canada', 'Classified', 'Protected']
    )
