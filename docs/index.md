# **Welcome to Subatomic!**

Subatomic is toolset designed to automate the provisioning and use of your developement environment from infrastructure through to CI/CD pipelines and associated monitoring. The goals of the project are to remove the hassle and cost of repeating the processes required to get new projects up an running from scratch to being to deployed into multiple environments. The project home can be found [here](https://github.com/absa-subatomic).

## **Getting Started**
There are many moving pieces in the Subatomic environment but a users main interaction with the system will occur through the Quantum Mechanic slack client. In future a web ui will be added for a more powerful user experience. Below are some links to help a user getting started with the system.

* [User Guide](user-guide/overview.md) - A tutorial for getting started as an end user of subatomic.
* [Quantum Mechanic Command Reference](quantum-mechanic/command-reference.md) - A reference guide for using the slack commands in Quantum Mechanic.
* [New to Subatomic](new-to-subatomic.md) - A useful set of links and
reference materials if you're new to Subatomic.

## **The Subatomic Stack**
Subatomic is built with a specific core stack in mind. The below list details the environment requirements for running Subatomic.

* [Openshift](https://www.openshift.com/) - "Red Hat® OpenShift is a container application platform that brings docker and Kubernetes to the enterprise". Openshift is used to provision environments for new projects and as a home for the associated CI/CD pipelines created through subatomic.
* [Bitbucket Server](https://www.atlassian.com/software/bitbucket/server) - Subatomic's primary market is large development teams and naturally this tends towards large organizational environments. The Atlassian stack is common place in such environments and as such Bitbucket Server is currently the only supported source control system supported in Subatomic.
* [Slack](https://slack.com/) - Slack is the primary means for interaction with the Subatomic system through the ChatOps style Quantum Mechanic interface. It is important to note that Quantum Mechanic is built using the [Atomist](https://atomist.com/) framework.
