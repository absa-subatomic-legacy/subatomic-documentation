# **Frequently Asked Questions**
This page tries to list common questions and solutions to related to problems users may face when using Subatomic.

## **General**
These are questions that apply in general to Subatomic use.

### ***What is the difference between an application and a library?***
An application in Subatomic means a code base that is deployable and can be run by itself. An example would be a spring boot application, or an angular application. When linking or creating an application, all associated OpenShift resources required to deploy the application will be created along with the Jenkins build. This includes the necessary DeploymentConfig's and a BuildConfig for the application.

A library on the other hand is code that is meant to be used by other codebases. An example of such would be a library of math functions that are reused by various applications. When linking or creating a library, only the Jenkins build is created. The user is expected to push the artifact from their Jenkins build into a reusable location such as Nexus for use in other applications.

### ***Common Jenkins buid failures***

**Error:** `Jenkins fails to pull maven dependencies.`

This could possibly be happening due to a mvnw file in your repo. Currently mvn wrappers are not a supported in the default jenkins build pipeline provided by Subatomic.

**Error:** `Could not determine exact tip revision.`

This is bug in the current version of Jenkins used. The solution involves rescanning your multibranch pipeline in Jenkins, or performing a new code commit.

### ***No commands work or I get permission errors when running commands***

**Possibility 1:** Commands are not running because the automation client or the Gluon backend is not accessible. You will need to contact your Subatomic administrator.

**Possibility 2:** Commands in a particualr team channel are failing because you are either not actually a member of the team, or you dont have the permissions to run an owner specific command. To view the list of team members and owners for a team run `@atomist sub list team members`.


## **Commands**
Any questions related to running particular commands can be found in this section.

### **sub onboard me**
**Error:** `Failed to onboard since the member's details are already in use.`

When onboarding a user, it is important to have a unique username, email, and slack user. If any of these are already in use, the user needs to use different details to onboard. It is also likely that the user has already onboarded themselves and can try continue assuming that they are before trying different credentials.

### **sub link bitbucket project**
**Question:** How do I find my Bitbucket project key?

Your Bitbucket project key can be obtained from the URL to your Bitbucket project. The Bitbucket URL to your project should look similar to the following: `https://bitbucket.organisation.com/projects/PROJECT_KEY/repos/browse`. The characters in the location illustrated by `PROJECT_KEY` are the project key for the Bitbucket project.


