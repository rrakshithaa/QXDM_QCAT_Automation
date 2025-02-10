import os


class HDFFileReader:
    def __init__(self):
        self.hdf_file_names = []

    def read_hdf_files(self):
        hdf_file_path = r"C:\UsersDownloads\QXDM_Logs\qxdm_file"
        for root, _, files in os.walk(hdf_file_path):
            for file in files:
                if file.endswith('.hdf'):
                    self.hdf_file_names.append(file)
