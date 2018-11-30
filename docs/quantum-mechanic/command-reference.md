# **Quantum Mechanic**
Below are the commands and their explanations that you'll encounter while using subatomic:

### **add config server**
Adds a config server to the selected OpenShift project.

### **add team member**
Adds a member to an existing team.

### **add team owner**
Adds a member to an existing team with owner privilege.

### **add slack**
Adds Slack details to an existing team member.

### **associate team**
Links a team to an existing project.

### **configure project bitbucket access**
Configures user and system access to Bitbucket for an existing project.

### **apply bitbucket practices**
Applies recommended practices to the Bitbucket project.

### **configure application jenkins prod**
Adds a prod deployment job to Jenkins for an application.

### **configure package**
Configures an existing application/library using a predefined template.

### **configure custom package**
Configure an existing application/library using custom templates.

### **request application prod**
Creates an application in prod.

### **request generic prod**
Moves OpenShift resources to prod.

### **create openshift pvc**
Creates a new OpenShift Persistent Volume Claim.

### **create project**
You will need to input two values `project name` and `project description`. This will create a project within
Subatomic.

### **request project prod**
Creates the OpenShift prod environments for a project.

### **create team**
You will need to input two values `team name` and `team description`. This will create a team with
the respective values in Subatomic.

### **help**
Creates an interactive help menu.

### **apply to team**
This will send a request to the channel that you type in. Once accepted you will be within said channel.

### **create jenkins bitbucket credentials**
Recreates the Jenkins Bitbucket credentials.

### **jenkins build**
Starts a jenkins build with the selected project.

### **link application**
Links an application contained within a BitBucket project to the project.

### **link library**
Links a library contained within a BitBucket project to the project.

### **link team channel**
If you already have an existing slack channel use this command. Subatomic will add the atomist bot
to this channel, however if the channel is private you will need to manually invite the bot.

### **link bitbucket project**
You will need to input your `bitbucket project key` and Subatomic will find the existing project within Bitbucket.

### **list team members**
Displays members and owners of the team.

### **list projects**
Lists all projects associated with the select team.

### **request devops environment**
This will create a  new OpenShift DevOps environment for your team or use an existing one.

### **request project environments**
Creates new OpenShift environments for a project. This will create a DEV, SIT and UAT environments.

### **create team channel**
This will create a public slack channel, if you want a private channel you will need to create
it manually then proceed to [sub link team channel](./command-reference.md#link-team-channel).

### **onboard me**
The most important command, without onboarding yourself you will not be able to run any subatomic commands.

You will need to input your `first name`, `last name`, `email address` and `domain username`.
Once submitted you will be able to execute subatomic commands granted you have the permission to execute them.

For a detailed walk through click [here](../user-guide/onboarding.md)

### **patch package s2i image**
Patches the s2i image used to build a package.

### **remove team member**
Removes a member (not owner) from a team.

### **tag all images**
Tags all latest Subatomic images to a devops environment.

### **tag image**
Tags an individual Subatomic image to a devops environment.