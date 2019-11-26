# Cloud-Project-_CS351
Cloud service level agreement (SLA) based resource monitoring: Simulate transactions in a given set of machines on the cloud. Monitor the resources (CPU, memory usage, hard disks, network usage etc.) and report. In case the resource utilization goes beyond a certain threshold (e.g. 98%), then mark it as SLA failure, and allocate fresh resources in a fresh machine. Trigger process failover (a simple print statement saying “triggered” is sufficient).


Server.py:It acts like a mediator between client and Virtual machine .It connects user to Virtual machine and if Virtual machine overloads it switches whole data from one virtual machine to another such that no data loss takes place and our goal is also been fulfilled of SLA failure.It also contains the information regarding autentication and autorization ,where it takes place as the client verify its crediantials.It uses parallel programing to get the information of health of Virtual machine such as (CPU, memory usage, hard disks, network usage etc.If it crosses a certain limit it switches from one Virtual Machine to another.We have used threading for getting information about Virtual machines.  



Client.py:It acts helper for autentication and autorization It is the user end where user authenticate itself by server .Client uses virtual machines to gets it's computation done and print the statement "Trigger process failover triggered" if SLA failover takes place and it switches itself from one Virtual machine to another.



Virtual_Machine.py:It is the place where the computations of the users are occuring,in case of its failover it transfers
its data to another Virtual machines.



Steps to be followed while simulating the project :

Step1:Open the command promt .

Step2:exceute python virtual_machine_1.py on command promt.

Step3:exceute python virtual_machine_2.py

Step4:execute server.py

Step5:execute client.py

Working:While user input their data in client.py it stores the data in virtual_machine_1.py through server.py if virtual_machine_1.py overloads the server transfers the whole data of virtal_machine_1.py to virtal_machine_2.py.

Conclusion:Simulate transactions in a given set of machines on the cloud. Monitor the resources (CPU, memory usage, hard disks,etc.) and report. In case the resource utilization goes beyond a certain threshold (e.g. 98%), then mark it as SLA failure, and allocate fresh resources in a fresh machine. Trigger process failover.During this whole process we are not losing any information even though the SLA failover takes place.

