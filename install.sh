apt-get update
apt-get install -y make
apt-get install -y g++
apt-get install -y tesseract-ocr
apt-get install -y libtesseract-dev
# http://stackoverflow.com/questions/4011705/python-the-imagingft-c-module-is-not-installed
apt-get install -y libfreetype6-dev
apt-get install -y python-pip
apt-get install -y python-dev

pip install pillow nose Sphinx