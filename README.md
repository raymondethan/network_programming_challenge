### Programming Challenge

Consider a system consisting of n identical machines. On each machine resides some piece of software, A. A is currently at version 1 (denoted A1 in the figure below). Some user upgrades software A from version 1 to 2 (denoted A2 in the figure) on a single machine. Write an agent that will run on each machine and update all other machines when an update occurs.

![System](https://i.cloudup.com/UbCY3DEx2X-3000x3000.png)

To help get you started, a Vagrantfile has been included which will spin up three servers (server1, server2, server3) which will act as the test system. Your tool should scale for any number of servers. You can learn more about setting up Vagrant [here](http://docs.vagrantup.com/v2/getting-started/).

For simplicity, software A can be a text file containing the number 1 that gets updated to the number 2.