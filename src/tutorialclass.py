import numpy as np

class Tutorialclass:
    """This is a little toy class to show documentation...
    
        Use: 
        1. instantiate this Class.
        2. Save numbers internally with the method `add_number(x)`:
        3. Saved internally in `self._data`
        4. Produce output with `get_sum()`
    """

    def __init__(self, limit=10):
        """_summary_

        Args:
            limit (int, optional): Some toy variables. Doesn't do anything. Defaults to 10.
        """
        self._data = []  # Array to store all the numbers

    def status(self):
        """_summary_
        """
        print(self._data)

    def add_number(self, x):
        """_summary_

        Args:
            x (np.float): Any number that should be stored on the internal list
        """
        self._data.append(x)

    def return_sum(self) -> dict: # Use function annotations, particularly when returning specific things
        """_summary_

        Returns:
            _type_: _description_
        """
        cc = dict()
        cc['sum'] = np.sum(self._data)
        return cc
