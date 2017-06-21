import urllib, os
from tqdm import tqdm

class TqdmUpTo(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`.
    https://pypi.python.org/pypi/tqdm
    """
    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize

def download_file(url, filename):
    """ file downloader with progress bar """
    with TqdmUpTo(unit='B', unit_scale=True, miniters=1, desc=filename) as t: 
        urllib.urlretrieve(url, filename=filename, reporthook=t.update_to, data=None)
