<div style="border: 0px solid red;">
  <img style="vertical-align:middle;border: 0px solid red;" src="/images/subatomic-logo-colour.png" width="100px">
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

<a href="https://www.openshift.com" target="_blank"><img src="/images//openshift-logo-long.png" width="150px"></a> <br/>Red Hat® OpenShift is a container application platform that brings docker and Kubernetes to the enterprise". Openshift is used to provision environments for new projects and as a home for the associated CI/CD pipelines created through Subatomic.

<a href="https://slack.com"  target="_blank"><img src="/images//slack-logo.png" width=130px"></a> <br/>Slack is a cloud-based set of proprietary team collaboration tools and services. Slack is the primary means for interaction with the Subatomic system through the ChatOps style Quantum Mechanic interface. It is important to note that Quantum Mechanic is built using the <a href="https://atomist.com/" target="_blank">Atomist</a> framework.

<a href="https://www.atomist.com/"  target="_blank"><img src="/images//atomist-horiz-logo.png" width=175px"></a> <br/>Atomist is the automation platform for modern software delivery. Atomist provides the API for software, and a cloud service to run it, so that every company can automate delivery and give all their developers the self-service they crave. With Atomist, toil disappears, replaced by a helpful assistant that automatically fixes your common mistakes, checks your code for quality and security, and takes care of all the tedious tasks you don't want to do. Stop doing things by hand and deliver in code.

<a href="https://jenkins.io/"  target="_blank"><img src="/images//jenkins-logo-long.png" width=145px"></a> <br/>Jenkins is an open source automation server written in Java. Jenkins helps to automate the non-human part of the software development process, with continuous integration and facilitating technical aspects of continuous delivery. 