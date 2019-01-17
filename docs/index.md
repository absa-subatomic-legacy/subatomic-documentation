<div style="border: 0px solid red;">
  <img style="vertical-align:middle;border: 0px solid red;" src="/images//subatomic-logo-colour.png" width="100px">
  <span style="font-size:30px;;border: 0px solid red;">Welcome to Subatomic</span>
</div>

Subatomic is a toolset designed to automate the provisioning and management of your OpenShift environment from infrastructure through to CI/CD pipelines and associated monitoring. 

The goals of the project are:

1. To remove the hassle and cost of repeating the processes required to get new projects up and running from scratch to being deployed into multiple environments.
2. To ensure projects, team and environments are provisioned and managed consistently and according to the same standards and procedures.
2. To empower development teams to own and self manage their projects and infrastructure as completely as possible.

There are many different components in the Subatomic stack but users main interaction with the system will occur through the Quantum Mechanic Slack chat client.

The github project home can be found <a href="https://github.com/absa-subatomic"  target="_blank">here</a>.

## **Getting Started**
Below are some links to help a user getting started with the system.

* [User Guide](user-guide/overview.md) - A tutorial for getting started as an end user of Subatomic.
* [Quick Command Reference](quantum-mechanic/command-reference.md) - A reference guide for using the Quantum Mechanic Slack commands.

## **The Subatomic Stack**
Subatomic is built with a specific core service stack in mind. The below list details the 3rd party software required for running Subatomic.

<a href="https://www.openshift.com" target="_blank"><img src="/images//openshift-logo-long.png" width="150px"></a>" <br/>Red Hat® OpenShift is a container application platform that brings docker and Kubernetes to the enterprise". Openshift is used to provision environments for new projects and as a home for the associated CI/CD pipelines created through Subatomic.


<a href="https://www.atlassian.com/software/bitbucket/server" target="_blank"><img src="/images//bitbucket-logo.png" width="150px"></a> <br/> Bitbucket is a web-based version control repository hosting service owned by Atlassian, for source code and development projects that use either Mercurial or Git revision control systems.. Subatomic's primary market is large development teams and naturally this tends towards large organizational environments. The Atlassian stack is common place in such environments and as such Bitbucket Server is currently the only supported source control system supported in Subatomic.

<a href="https://slack.com"  target="_blank"><img src="/images//slack-logo.png" width=130px"></a> <br/>Slack is a cloud-based set of proprietary team collaboration tools and services. Slack is the primary means for interaction with the Subatomic system through the ChatOps style Quantum Mechanic interface. It is important to note that Quantum Mechanic is built using the <a href="https://atomist.com/" target="_blank">Atomist</a> framework.

<a href="https://www.atomist.com/"  target="_blank"><img src="/images//atomist-logo.png" width=145px"></a> <br/>Atomist lets you construct your delivery process in code – but not too much code. A service, a framework, and some libraries take care of the pieces that are common to every development organization. Atomist works atop your existing toolchain, adding functionality and smoothing your experience; then you’re free to improve it

<a href="https://jenkins.io/"  target="_blank"><img src="/images//jenkins-logo.png" width=145px"></a> <br/>Jenkins is an open source automation server written in Java. Jenkins helps to automate the non-human part of the software development process, with continuous integration and facilitating technical aspects of continuous delivery. 