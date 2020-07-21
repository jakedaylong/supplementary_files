Vagrant.configure("2") do |config|
  config.vm.provider "docker"
  config.vm.box = "tknerr/baseimage-ubuntu-18.04"
  config.vm.box_version = "1.0.0"
  current_dir = File.basename(Dir.getwd)
  config.vm.hostname = current_dir.gsub("_", "-")
  config.vm.synced_folder ".", "/home/vagrant/project"

  $script = <<-'SCRIPT'
      echo vagrant ALL=NOPASSWD:ALL > /etc/sudoers.d/vagrant
      apt update
      DEBIAN_FRONTEND=noninteractive apt-get -yq install --no-install-recommends apt-utils
      DEBIAN_FRONTEND=noninteractive apt-get -yq install software-properties-common &&
      DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:deadsnakes/ppa
      DEBIAN_FRONTEND=noninteractive apt update
      DEBIAN_FRONTEND=noninteractive apt-get -yq install python3.8
      DEBIAN_FRONTEND=noninteractive apt-get -yq install python3-pip
      DEBIAN_FRONTEND=noninteractive apt-get -yq install python3.8-venv
      DEBIAN_FRONTEND=noninteractive apt-get -yq install python3.8-distutils
      DEBIAN_FRONTEND=noninteractive apt-get -yq install python3.8-tk
      DEBIAN_FRONTEND=noninteractive apt-get -yq install git
      echo alias python=python3.8 >> /home/vagrant/.bashrc
      echo export 'PATH=/usr/bin/python3.8:/home/vagrant/.poetry/bin/poetry:/home/vagrant/.local/bin:$PATH' >> /home/vagrant/.bashrc

      su - vagrant -c 'source /home/vagrant/.bashrc'
      su - vagrant -c 'python3.8 -m pip install --upgrade pip --user'
      # su - vagrant -c 'python3.8 -m pip install dephell[full] --user'
      su - vagrant -c 'python3.8 -m pip install --upgrade keyrings.alt --user '
      su - vagrant -c 'python3.8 -m pip install poetry --user'
      # su - vagrant -c 'dephell self autocomplete'


      if [ ! -e "/home/vagrant/project/pyproject.toml" ]; then
             su - vagrant -c 'cd /home/vagrant/project && poetry new --src project'
             su - vagrant -c 'cd /home/vagrant/project/project && mv * .. && cd .. && rm -r project'
      fi

      su - vagrant -c 'cd /home/vagrant/project && poetry add --dev pytest'
      su - vagrant -c 'cd /home/vagrant/project && poetry add --dev pytest-cov'
      su - vagrant -c 'cd /home/vagrant/project && poetry add --dev pytest-mock'
      su - vagrant -c 'cd /home/vagrant/project && poetry add --dev pytest-bdd'
      su - vagrant -c 'cd /home/vagrant/project && poetry add --dev pysnooper'

      su - vagrant -c 'cd /home/vagrant/project && poetry install'

  SCRIPT
  config.vm.provision "shell", inline: $script
end

