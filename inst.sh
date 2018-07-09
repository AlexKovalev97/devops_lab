#!/bin/bash
yum install git gcc gcc-c++ make patch zlib libffi-devel openssl-devel -y
yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel mysql-devel -y 
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo -e 'export PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"' >> ~/.bashrc 
source ~/.bashrc 
pyenv install 3.5.5
pyenv install 2.7.8
pip install -U pip
pyenv virtualenv 2.7.8 python2 
pyenv virtualenv 3.5.5 python3