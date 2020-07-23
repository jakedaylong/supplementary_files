Vagrant.configure("2") do |config|
  config.vm.provider "docker" do |d|
    d.build_dir = "."
    d.has_ssh = true
    current_dir = File.basename(Dir.getwd)
    config.vm.hostname = current_dir.gsub("_", "-")
    config.vm.synced_folder ".", "/home/vagrant/project"
   end
   config.vm.provision "shell", path: "provision.sh", privileged: false
end
