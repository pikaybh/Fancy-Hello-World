from copy import deepcopy
from time import sleep


class FancyPrint:
    _candidates = [
        ' ', 
        '0', 
        ':', 
        'A', 
        '[', 
        'a', 
        '{'
    ]

    def __init__(self, duration : float = 0.05):
        self.duration = duration
        self._L = []

    def _check_condition(self, start_char, end_char, target_char):
        return ord(start_char) <= ord(target_char) and ord(target_char) < ord(end_char)

    def _check_scope(self, _c : str) -> tuple:
        """
        :param _c: A character to check it's ASCII code scope.
        :type _c: str(char)
        :return: start number of scope, end number of scope
        :rtype: tuple
        """
        for i in range(len(self._candidates)):
            if i + 1 >= len(self._candidates): return ord(self._candidates[i]), 127
            if self._check_condition(self._candidates[i], self._candidates[i+1], _c): return ord(self._candidates[i]), ord(self._candidates[i+1])

    def _print(self, c : str) -> None:
        start_ascii, end_ascii = self._check_scope(c)
        i = deepcopy(start_ascii)
        while i in range(start_ascii, ord(c)):
            print(''.join(self._L) + chr(i))
            i += 1
            sleep(self.duration)
        self._L.append(chr(i))

    def __call__(self, sentence : str):
        for c in sentence:
            self._print(c)
        print(''.join(self._L))
        self._L = []