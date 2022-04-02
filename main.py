import window
import os

if __name__ == "__main__":
    if not os.path.exists("./data"):
        os.mkdir("./data")
        os.mkdir("./data/picture")
        open("./data/data.dat", "wt")
    window.Create()
