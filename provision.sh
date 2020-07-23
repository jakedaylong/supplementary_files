#!/bin/bash
curl https://pyenv.run | bash
echo export PATH="/home/vagrant/.pyenv/bin:/home/vagrant/.pyenv/versions/3.8.5/bin:$PATH" >> /home/vagrant/.bashrc
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bashrc
export PATH="/home/vagrant/.pyenv/bin:/home/vagrant/.pyenv/versions/3.8.5/bin:$PATH"
/home/vagrant/.pyenv/bin/pyenv install 3.8.5
/home/vagrant/.pyenv/bin/pyenv global 3.8.5
python -m pip install --upgrade pip
python -m pip install --upgrade keyrings.alt
python -m pip install pyscaffold

# su - vagrant -c 'python -m pip install dephell[full] --user'
# su - vagrant -c 'python -m pip install --upgrade keyrings.alt --user '
# su - vagrant -c 'dephell self autocomplete'
git config --global user.email "me@andykmiles.com"
git config --global user.name "Andy Miles"

if [ ! -e "/home/vagrant/project/setup.cfg" ]; then
       cd /home/vagrant/project && putup --tox --no-skeleton --travis project
       cd /home/vagrant/project/project && mv * .. && cd .. && rm -r project
       cd /home/vagrant/project && pyenv local 3.8.5
fi

echo $'pytest\npytest-cov\npytest-mock\npytest-bdd\npysnooper\ntox\nmypy\npylint\n' > /home/vagrant/project/requirements.txt.dev
echo $'loguru\n' > /home/vagrant/project/requirements.txt
cd /home/vagrant/project && python setup.py develop
cd /home/vagrant/project && python -m pip install -r requirements.txt.dev
cd /home/vagrant/project && python -m pip install -r requirements.txt
