import gdown

url = 'https://drive.google.com/file/d/1dPjH-QAHACJ747QCDOLf3iawNKyHCN1E/view?usp=sharing'
id_ = url.split('/')[5]
url = 'https://drive.google.com/uc?id=' + id_
gdown.download(url, quiet=False)
