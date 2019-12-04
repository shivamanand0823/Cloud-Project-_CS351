# Cloud-Project-_CS351
Cloud service level agreement (SLA) based resource monitoring: Simulate transactions in a given set of machines on the cloud. Monitor the resources (CPU, memory usage, hard disks, network usage etc.) and report. In case the resource utilization goes beyond a certain threshold (e.g. 98%), then mark it as SLA failure, and allocate fresh resources in a fresh machine. Trigger process failover (a simple print statement saying “triggered” is sufficient).


Server.py:It acts like a mediator between client and Virtual machine .It connects user to Virtual machine and if Virtual machine overloads it switches whole data from one virtual machine to another such that no data loss takes place and our goal is also been fulfilled of SLA failure.It also contains the information regarding authentication and authorization ,where it takes place as the client verify its credeantials.It uses parallel programing to get the information of health of Virtual machines such as (CPU, memory usage, hard disks, network usage etc.If it crosses a certain limit it switches from one Virtual Machine to another.We have used threading to get information about Virtual machines.  



Client.py:It acts helper for authentication and authorization It is the user end where user authenticate itself by server .Client uses virtual machines to gets it's computation done and print the statement "Trigger process failover triggered" if SLA failover takes place and it switches itself from one Virtual machine to another.Username=Shivam/Varun/Rushikesh,Password=Cloud



Virtual_Machine.py:It is the place where the computations of the users are occuring,in case of its failover it transfers
its data to another Virtual machines.



Steps to be followed while simulating the project :

Step1:Open the command prompt .

Step2:execute python Virtual_machine_1.py on command prompt.

Step3:execute python Virtual_machine_2.py

Step4:execute Server.py

Step5:execute Client.py   Username=Shivam/Varun/Rushikesh,Password=Cloud

Working:While user input their data in Client.py it stores the data in Virtual_machine_1.py through server.py if Virtual_machine_1.py overloads the server transfers the whole data of Virtal_machine_1.py to Virtal_machine_2.py.

Conclusion:Simulate transactions in a given set of machines on the cloud. Monitor the resources (CPU, memory usage, hard disks,etc.) and report. In case the resource utilization goes beyond a certain threshold (e.g. 98%), then mark it as SLA failure, and allocate fresh resources in a fresh machine. Trigger process failover.During this whole process we are not losing any information even though the SLA failover takes place.

