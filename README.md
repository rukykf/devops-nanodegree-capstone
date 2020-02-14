# devops-nanodegree-capstone
Capstone project for the udacity cloud devops nanodegree

## NOTES:
## USING AMAZON EKS and ANSIBLE
I opted to use Amazon's managed kubernetes as a service offering. 
I setup the cluster using ansible with amazon's eksctl tool for managing EKS clusters 

## SETTING UP THE JENKINS CI/CD SERVER
In the code repository I have included the ansible playbooks I used to setup my EKS cluster
but prior to running these playbooks, I did some setup on the Jenkins server itself.
These tasks, besides installing and configuring Jenkins include:
- configuring my AWS credentials with awscli
- installing docker
- installing ansible and its python dependencies
- adding my jenkins user to sudoers to make it easy to run the ansible playbooks without configuring a build agent (not the best idea, but it works :)

## ILLUSTRATING THE ROLLING UPDATE
While I have included screenshots of the site before the rolling update and after the rolling update,
I felt screenshots were inadequate to illustrate what was actually happening on the kubernetes pods during the update.

So I wrote a little script that made hundreds of requests
to the kubernetes cluster (through the dns of the LoadBalancer service I created)
This script and its output before and after the rolling update are part of this code repository
