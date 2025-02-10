import os
import shutil
import time
from AppOpener import open, close
import keyboard
from Qxdm_operations.keyboard_functions import KeyboardAction
from Qxdm_operations.hdf_operation import HDFFileReader
from utils.logger import logger


class Qxdm_operations:
    def __init__(self):
        self.keyboard = KeyboardAction()
        self.hdf_reader = HDFFileReader()
        self.hdf_reader.read_hdf_files()


    def open_logs(self, file_name):

        try:
            open("Qcat")
            logger.info("******************* Opening QCat ****************************")
            time.sleep(5)
            keyboard.press_and_release('alt+space')
            keyboard.press_and_release('x')
            logger.info("**** Maximise the window ****")
            time.sleep(5)
            keyboard.press_and_release('alt+f')
            logger.info("**** Open QXDM log file ****")
            time.sleep(5)
            self.keyboard.press_enter_n_times(2)
            time.sleep(3)

            logger.info("******************** File Explorer *************************")
            # opens file explorer
            keyboard.write(file_name)
            logger.info("**** Enter File name ****")
            time.sleep(5)
            self.keyboard.press_enter_n_times(1)
            time.sleep(5)


            logger.info("********************** Handle Alerts and popups *********************")
            # handle alert popups
            self.keyboard.keyboard_events(popup_alert=True)
            time.sleep(3)


            logger.info("********************* Tools --> Convert to pcap files *********************")
            # click on tools and convert it to pcap file
            keyboard.press_and_release('alt+t')
            time.sleep(3)
            self.keyboard.press_enter_n_times(5)
            time.sleep(3)
            keyboard.press('enter')
            time.sleep(15)
            close("Qcat")
            logger.info("******************** Next Session ********************************")

        except Exception as e:
            logger.error(f"Qcat Application handling Error: {e}")


    def process_logs(self):

        try:
            qxdm_logs_folder = r"C:\Users\Downloads\QXDM_Logs\qxdm_file"
            destination_folder = r"C:\Users\Downloads\QXDM_Logs\output_threadx"
            for root, _, files in os.walk(qxdm_logs_folder):
                for file in files:
                    if "TheadX_IP" in file and file.endswith(".pcap"):
                        source_file = os.path.join(root, file)
                        destination_path = os.path.join(destination_folder, file)
                        shutil.move(source_file, destination_path)

        except FileNotFoundError as e:
            logger.error(f"File error: {e}")


    def main(self):
        try:
            for file_name in self.hdf_reader.hdf_file_names:
                qxdm_operations.open_logs(file_name)

            logger.info("************************** Move TheadX_IP files to new separate folder *******************************")
            qxdm_operations.process_logs()

        except Exception as e:
            logger.error(f"Exception in Locating file name: {e}")



if __name__ == '__main__':
    qxdm_operations = Qxdm_operations()
    qxdm_operations.main()
