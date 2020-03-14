from shutil import which

class GetPackman():

    def __init__(self):
        self.candidates = [
            # packman of the future
            'dnf',
            'snap',

            # legacy packman
            'yum',
            'apt'
        ]

    def __call__(self):
        _packman_ = self.find_packman()
        return _packman_

    def find_packman(self):
        for candidate in self.candidates:
            if(which(candidate)):
                return candidate
        return ''

get_packman = GetPackman()
