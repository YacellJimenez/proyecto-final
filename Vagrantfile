Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"
    config.vm.hostname = "servidor-prueba"
    config.vm.network "private_network", ip: "192.168.56.10"

    config.vm.provider "virtualbox" do |vb|
      vb.memory = "256"
      vb.cpus = 1
    end
  end