"""download mscelebrities dataset"""
import os

import requests
from tqdm import tqdm


def download_imdb(face_only=True, data_dir="./data"):
    """  https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/ """
    full_urls = ["https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_0.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_1.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_2.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_3.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_4.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_5.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_6.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_7.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_8.tar",
                 "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_9.tar",
                 ]
    full_meta = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar"
    face_url = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar"
    imdb_face = os.path.join(data_dir, "imdb_face.tar")
    if face_only:
        if os.path.isfile(imdb_face):
            raise Exception("file %s exists" % imdb_face) 
        response = requests.get(face_url, stream=True)
        total_size = int(response.headers.get('content-length', 0));
        with open(imdb_face, "wb") as handler:
            for data in tqdm(response.iter_content(), total=total_size, unit='B', unit_scale=True):
                handler.write(data)
    else:
        # TODO download all imdb data
        pass
        

def download_wiki(data_dir="./data"):
    """  https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/ """
    face_url = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki_crop.tar" 
    face_meta_url = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/wiki.tar.gz"

    wiki_face = os.path.join(data_dir, "wiki_face.tar.gz")
    wiki_meta = os.path.join(data_dir, "wiki_meta.tar.gz")

    # download faces
    if os.path.isfile(wiki_face):
        raise Exception("file %s exists" % wiki_face) 
    else:
        response = requests.get(face_url, stream=True)
        total_size = int(response.headers.get('content-length', 0));
        with open(wiki_face, "wb") as handler:
            for data in tqdm(response.iter_content(), total=total_size, unit='B', unit_scale=True):
                handler.write(data)

    if os.path.isfile(wiki_meta):
        raise Exception("file %s exists" % wiki_meta) 
    else:
        response = requests.get(face_meta_url, stream=True)
        total_size = int(response.headers.get('content-length', 0));
        with open(wiki_meta, "wb") as handler:
            for data in tqdm(response.iter_content(), total=total_size, unit='B', unit_scale=True):
                handler.write(data)

        
def main():
    download_imdb() 
    download_wiki() 

if __name__ == "__main__":
    main()
