from pathlib import Path
import os
import sys


class Settings(object):
    """Object that handle the settings for this tool."""

    default_shebang = "#!/usr/bin/env python3"

    def __init__(self):
        """No initial pararameters nedeed at the moment"""
        pass

    def work_place_exists(self, work_place_path: str) -> bool:
        """Gets file argument in file_arg variable, and locates it on file system,
        then return the full path where is located.

        :param file_arg: Relative file path argument to locate
        :type file_arg: str
        :returns: str with the full path of the located file
        :rtype: str
        """

        path = Path(work_place_path)
        if path.exists() and path.is_dir():
            return True
        else:
            return False


    def set_work_place(self, work_place_path: str):
        """Writes work place on a config file for later read.

        :param work_place: Path to the existing work place
        :type work_place: str
        :returns: No return
        :rtype: None
        """

        if not self.work_place_exists(work_place_path):
            os.makedirs(work_place_path)
        with open("~/pylunarvim/config.txt", "w") as config:
            config.write(work_place_path)


    def get_work_place_settings(self) -> str:
        """Gets working space set by the user, the returns it

        :param: No arguments
        :type:
        :returns: str with the path for the working space set by user on config.txt
        :rtype: str
        """

        with open("~/pylunarvim/config.txt", "r") as config:
            work_place = config.readline()

        return work_place


    def check_work_place(self, work_place_path: str) -> bool:
        """Check if work place on work_place_path exists, if so, then returns True.
        If not, then returns False

        :params work_place_path: Work place path to check
        :type: str
        :returns: bool signaling that the work place is present or not
        :rtype: bool
        """

        try:
            if self.work_place_exists(work_place_path):
                return True
            else:
                raise Exception

        except Exception:
            print("ERROR: Path to Work Place Not Found")
            return False


    def display_work_place(self, getworkplace: bool) -> None:
        """Reads work place settings from file.

        :params getworkplace: False or True for displaying or not the settings
        :type: bool
        :returns: No return
        :rtype: None
        """

        if getworkplace:
            work_place_settings = self.get_work_place_settings()
            print(work_place_settings)
            sys.exit(0)



    def add_work_place_to_path(self, work_place: str) -> None:
        """Adds work_place to the PATH variable

        :params work_place: str with the path to work_place
        :type: str
        :returns: No return
        :rtype: None
        """

        home = Path.home()
        with open(str(home) + ".zshrc", "a") as zshrc_file:
            zshrc_file.write("")
            zshrc_file.write(f'export PATH={work_place}:$PATH')
