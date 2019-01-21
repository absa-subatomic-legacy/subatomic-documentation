# **Quantum Mechanic**
Below are the commands and their explanations that you'll encounter while using Subatomic:

###  **Bitbucket Commands**
Bitbucket commands that control Bitbucket project configuration and access controls

1. `````sub apply bitbucket practices````` - Apply recommended practices to Bitbucket project

###  **Jenkins Commands**
Jenkins commands that allow the user to control builds and jenkins configuration

1. ```sub configure application jenkins prod``` - Add a prod deployment job to jenkins for an application
2. ```sub create jenkins bitbucket credentials``` - Recreate the Jenkins Bitbucket Credentials
3. ```sub jenkins build``` - Kick off a Jenkins build

###  **Member Commands**
Member commands allow you to manage Subatomic members. These include editing Slack details, on-boarding, editing user roles and adding members to teams.

1. ```sub add team member``` - Add a member to a team
2. ```sub add team owner``` - Add a member as an owner to a team
3. ```sub add slack``` - Add Slack details to an existing team member
4. ```sub onboard me``` - The most important command, without on-boarding yourself you will not be able to run any subatomic commands. You will need to input your `first name`, `last name`, `email address` and `domain username`. Once submitted you will be able to execute subatomic commands granted you have the permission to execute them. For a detailed walk through click [here](../user-guide/onboarding.md)


###  **Package Commands**
Package commands are related to managing applications and libraries. These include deployment, build, prod promotion and image management.

1. ```sub configure application jenkins prod``` - Add a prod deployment job to jenkins for an application
2. ```sub configure package``` - Configure an existing application/library using a predefined template
3. ```sub configure custom package``` - Configure an existing application/library
4. ```sub request application prod``` - Create application in prod
5. ```sub link application``` - Link an existing application
6. ```sub patch package s2i image``` - Patch the s2i image used to build a package

###  **Project Commands**
Project commands provide management capabilities around individual Projects and their associated resources. This includes environment management, application and library creation, jenkins and Bitbucket configuration.

1. `sub associate team` - Add additional team/s to a project
2. `sub configure project bitbucket access` - Reconfigure user and system access to Bitbucket for an existing project
3. `sub apply bitbucket practices` - Apply recommended practices to Bitbucket project
4. `sub request generic prod` - Move OpenShift resources to prod *
5. `sub create OpenShift pvc` - Create a new OpenShift Persistent Volume Claim
6. `sub create project` - Create a new project. You will need to input two values `project name` and `project description`.
7. `sub request project prod` - Create the OpenShift production environments for a project
8. `sub link application` - Link an existing application
9. `sub link library` - Link an existing library
10. `sub link bitbucket project` - You will need to input your `bitbucket project key` and Subatomic will find the existing project within Bitbucket.
11. `sub list projects` - List projects belonging to a team
12. `sub request project environments` - Create new OpenShift environments for a project

###  **Team Commands**
Team commands allow you to manage your Subatomic team. These include team membership, team projects and DevOps environment configuration.

1. `sub add config server` - Add a new Subatomic Config Server
2. `sub add team member` - Add a member to a team
3. `sub add team owner` - Add a member as an owner to a team
4. `sub associate team` - Add additional team/s to a project
5. `sub create team` - You will need to input two values `team name` and `team description`. This will create a team with the respective values in Subatomic.
6. `sub apply to team` - Apply to join an existing team
7. `sub link team channel` - If you already have an existing slack channel use this command. Subatomic will add the atomist bot to this channel, however if the channel is private you will need to manually invite the bot.
8. `sub list team members` - Displays members and owners of the team.
9. `sub team migrate cloud` - Move all Openshift resources belonging to a team to a different cloud
10. `sub request devops environment` - Check whether to create a new OpenShift DevOps environment or use an existing one
11. `sub create team channel` - This will create a public slack channel, if you want a private channel you will need to create it manually then proceed to [sub link team channel](./command-reference.md#link-team-channel).
12. `sub remove team member` - Removes a member (not owner) from a team.
13. `sub tag all images` - Tag all latest subatomic images to a devops environment
14. `sub tag image` - Tag an individual subatomic image to a devops environment

###  **Other Commands**
All other general/miscellaneous commands

1. `sub create openshift pvc` - Create a new OpenShift Persistent Volume Claim
2. `sub team migrate cloud` - Move all Openshift resources belonging to a team to a different cloud
3. `sub help` - Displays an interactive help menu
