# **Quantum Mechanic**
Below are the commands and their explanations that you'll encounter while using Subatomic:

###  1. Bitbucket Commands (1)
Bitbucket commands that control Bitbucket project configuration and access controls

1. `````sub apply bitbucket practices````` - Apply recommended practices to Bitbucket project

###  2. Jenkins Commands (3)
Jenkins commands that allow the user to control builds and jenkins configuration

1. ```sub configure application jenkins prod``` - Add a prod deployment job to jenkins for an application
2. ```sub create jenkins bitbucket credentials``` - Recreate the Jenkins Bitbucket Credentials
3. ```sub jenkins build``` - Kick off a Jenkins build

###  3. Member Commands (4)
Member commands allow you to manage Subatomic members. These include editing Slack details, on-boarding, editing user roles and adding members to teams.

1. ```sub add team member``` - Add a member to a team
2. ```sub add team owner``` - Add a member as an owner to a team
3. ```sub add slack``` - Add Slack details to an existing team member
4. ```sub onboard me``` - On-board a new team member


###  4. Package Commands (6)
Package commands are related to managing applications and libraries. These include deployment, build, prod promotion and image management.

1. ```sub configure application jenkins prod``` - Add a prod deployment job to jenkins for an application
2. ```sub configure package``` - Configure an existing application/library using a predefined template
3. ```sub configure custom package``` - Configure an existing application/library
4. ```sub request application prod``` - Create application in prod
5. ```sub link application``` - Link an existing application
6. ```sub patch package s2i image``` - Patch the s2i image used to build a package

###  5. Project Commands (12)
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
10. `sub link bitbucket project` - Link an existing Bitbucket project
11. `sub list projects` - List projects belonging to a team
12. `sub request project environments` - Create new OpenShift environments for a project

###  6. Team Commands (14)
Team commands allow you to manage your Subatomic team. These include team membership, team projects and DevOps environment configuration.

1. `sub add config server` - Add a new Subatomic Config Server
2. `sub add team member` - Add a member to a team
3. `sub add team owner` - Add a member as an owner to a team
4. `sub associate team` - Add additional team/s to a project
5. `sub create team` - Create a new team
6. `sub apply to team` - Apply to join an existing team
7. `sub link team channel` - Link existing team channel
8. `sub list team members` - List members of a team ***
9. `sub team migrate cloud` - Move all Openshift resources belonging to a team to a different cloud
10. `sub request devops environment` - Check whether to create a new OpenShift DevOps environment or use an existing one
11. `sub create team channel` - Create team channel
12. `sub remove team member` - Remove a member from a team
13. `sub tag all images` - Tag all latest subatomic images to a devops environment
14. `sub tag image` - Tag an individual subatomic image to a devops environment

###  7. Other Commands (3)
All other general/miscellaneous commands

1. `sub create openshift pvc` - Create a new OpenShift Persistent Volume Claim
2. `sub team migrate cloud` - Move all Openshift resources belonging to a team to a different cloud
3. `sub help` - Displays an interactive help menu