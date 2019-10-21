import pickle as p

class filemanager:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "wb") as f:
            p.dump(data, f)

    def load(self):
        try:
            with open(self.filename, "rb") as f:
                data = p.load(f)
        except FileNotFoundError as fileErr:
            raise fileErr

        return data
