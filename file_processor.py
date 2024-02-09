"""This code extracts metadata from a single file"""

from file_processing import File

FILE_PATH = ''

if __name__ == '__main__':
    file = File(FILE_PATH)

    # Extract a single field of metadata
    print("Access time: ", file.access_time)

    # See a list of all the metadata collected for this particular file type
    print("All metadata: ", file.processor.__dict__)
