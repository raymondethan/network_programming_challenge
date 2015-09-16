# Bowery Interview Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"

  config.vm.define "server1" do |server1|
    server1.vm.hostname = "server1"
    server1.vm.network "private_network", ip: "10.0.0.10"
  end

  config.vm.define "server2" do |server2|
    server2.vm.hostname = "server2"
    server2.vm.network "private_network", ip: "10.0.0.11"
  end

  config.vm.define "server3" do |server3|
    server3.vm.hostname = "server3"
    server3.vm.network "private_network", ip: "10.0.0.12"
  end
end
