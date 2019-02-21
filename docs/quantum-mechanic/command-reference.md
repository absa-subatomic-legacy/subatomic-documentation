# **Quantum Mechanic**
Below are the commands and their explanations that you'll encounter while using Subatomic:

## Category View
The below sections have the commands grouped by functionality to help you browse them. You can use the links for the commands to navigate to the full description of what each command does.

###  **Bitbucket Commands**
Bitbucket commands that control Bitbucket project configuration and access controls

1. [`sub apply bitbucket practices`](#sub-apply-bitbucket-practices) - Apply recommended practices to Bitbucket project

###  **Jenkins Commands**
Jenkins commands that allow the user to control builds and jenkins configuration

1. [`sub configure application jenkins prod`](#sub-configure-application-jenkins-prod) - Add a prod deployment job to jenkins for an application
2. [`sub create jenkins bitbucket credentials`](#sub-create-jenkins-bitbucket-credentials) - Recreate the Jenkins Bitbucket Credentials
3. [`sub jenkins build`](#sub-jenkins-build) - Kick off a Jenkins build
4. [`sub project request jenkins job`](#sub-project-request-jenkins-job) - Creates a jenkins build folder for a given project

###  **Member Commands**
Member commands allow you to manage Subatomic members. These include editing Slack details, on-boarding, editing user roles and adding members to teams.

1. [`sub add team member`](#sub-add-team-member) - Add a member to a team
2. [`sub add team owner`](#sub-add-team-owner) - Add a member as an owner to a team
3. [`sub onboard me`](#sub-onboard-me) - The most important command, without on-boarding yourself you will not be able to run any subatomic commands. You will need to input your `first name`, `last name`, `email address` and `domain username`. Once submitted you will be able to execute subatomic commands granted you have the permission to execute them. For a detailed walk through click [here](../user-guide/onboarding.md).


###  **Package Commands**
Package commands are related to managing applications and libraries. These include deployment, build, prod promotion and image management.

1. [`sub configure application jenkins prod`](#sub-configure-application-jenkins-prod) - Add a prod deployment job to jenkins for an application
2. [`sub configure package`](#sub-configure-package) - Configure an existing application/library using a predefined template
3. [`sub configure custom package`](#sub-configure-custom-package) - Configure an existing application/library manually specifying all build/deplyoment details.
4. [`sub request application prod`](#sub-request-application-prod) - Create application in prod
5. [`sub link application`](#sub-link-application) - Link an existing application
6. [`sub patch package s2i image`](#sub-patch-package-s2i-image) - Patch the s2i image used to build a package

###  **Project Commands**
Project commands provide management capabilities around individual Projects and their associated resources. This includes environment management, application and library creation, jenkins and Bitbucket configuration.

1. [`sub associate team`](#sub-associate-team) - Add additional team/s to a project
2. [`sub configure project bitbucket access`](#sub-configure–project-bitbucket–access) - Reconfigure user and system access to Bitbucket for an existing project
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
13. `sub project request jenkins job` - Creates a jenkins build folder for a given project

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
11. `sub create team channel` - This will create a public slack channel, if you want a private channel you will need to create it manually then run  `sub link team channel` command above (7).
12. `sub remove team member` - Removes a member (not owner) from a team.
13. `sub tag all images` - Tag all latest subatomic images to a devops environment
14. `sub tag image` - Tag an individual subatomic image to a devops environment

###  **Other Commands**
All other general/miscellaneous commands

1. `sub create openshift pvc` - Create a new OpenShift Persistent Volume Claim
2. `sub team migrate cloud` - Move all Openshift resources belonging to a team to a different cloud
3. `sub help` - Displays an interactive help menu

## Detailed View
This section is dedicated to explaining in detail what each command does. The subatomic environment is designed to speed up developer workflow, but it should never prevent users from using the underlying stack directly if needed or desired.
The information here is put in place to help users understand exactly what is going on under the hood so that clarity is provided and manual execution of each command could be performed if desired.

---
#### `sub add config server`
This command is used to create a [Spring Cloud Config](https://spring.io/projects/spring-cloud-config) server for a team. The config server is configured to point to a single repository where application configuration is pulled from. The command itself performs the following steps

1. The Secret `subatomic-config-server` is created in the teams DevOps environment. This Secret contains the ssh key configuration required by the config server to access your Bitbucket config repository.
2. The ConfigMap `subatomic-config-server` is created in the teams DevOps environment. This contains the default `application.yml` configuration used by the config server.
3. The `subatomic-config-server` ImageStream is tagged into the teams DevOps environment.
4. The `default` service account is granted view rights since this is required to run the config server.
5. The `subatomic-config-server-template` Template is the then processed to created the necessary DeploymentConfig and Service in OpenShift.

---
#### `sub add team owner`
This is used to directly add a user to a Team you are the owner of with owner permissions. The user will need to have been onboarded before you can add them to the Team. Adding user as an owner performs the following operations:

1. Associate the user to the Team in the Subatomic database as an owner.
2. Add the user to all OpenShift namespaces associated to the Team and grant them Admin permissions.
3. Add the user to the Bitbucket projects for each Subatomic Project associated to the team. They are granted Admin rights on the Bitbucket projects.
4. Invite the new user to the Team's slack channel.


---
#### `sub add team member`
This is used to directly add a user to a Team you are the owner of with member permissions. The user will need to have been onboarded before you can add them to the Team. Adding user as a member performs the following operations:

1. Associate the user to the Team in the Subatomic database as a member.
2. Add the user to all OpenShift namespaces associated to the Team and grant them Write permissions.
3. Add the user to the Bitbucket projects for each Subatomic Project associated to the team.
4. Invite the new user to the Team's slack channel.

---
#### `sub apply bitbucket practices`
This will apply an opinionated set of recommended configuration settings to a Project's associated Bitbucket Project. The following is a list of the configuration that will be applied:

1. Restrict master branch merges to only allow `fast-forward` merges.
2. Restrict master branch to only allow changes through pull requests.
3. Mark master branch as not deletable.
4. Enables the Verify Committer hook.
5. Enables the Required Build before merging hook.
6. Enables the No Incomplete Tasks before merging hook.
7. Add all owners and members of the team to the default reviewers list.

---
#### `sub associate team`
This allows users to associate additional Teams to a Subatomic Project. Users of these associated Teams are granted permissions to all the Project source code and deployment environments. Additionally any Project notifications will be shown in the newly associated Team's Slack channel.

---
#### `sub configure application jenkins prod`
When running a Generic Prod request, all OpenShift resources in the highest non-prod environment are indiscriminately moved over to the production environments. This is just a straight copy of the resources, and does not configure any Jenkins jobs for Application production deployments.
This command is used to create just the Jenkins jobs for deploying an application into production environments following such a resource copying operation. The following steps are performed in order to do this:

1. Generate a Jenkinsfile that will be used to deploy the application into prod. The Jenkinsfile is the added to your Application repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile.[${pipelineTag}.]${environmentPostfix}` where `[${pipelineTag}.]` is not present if the deployment's owning pipeline has no tag.
2. Create a Jenkins build job that uses the generated Jenkinsfile to deploy your Application. The build job is also added to the Jenkins Job View which holds all the Jenkins jobs related the Application being deployed.

---
#### `sub configure custom package`
When a Package(either an Application or Library) is created in Subatomic, there are no details captured about how it should be built or deployed. It is just a piece of metadata describing the details of a Package's name, whether it is deployable, where it's source code lives etc. The user needs to then tell Subatomic how they wish to build/deploy this Package. Running this command will prompt the user to enter the minimal details required to build or deploy the Package. This includes the following:

- The S2I ImageStream to use to build an Application.
- The OpenShift template to process in order to create the Application's OpenShift resources in each deployment environment.
- The default Jenkinsfile to add to the Package repository (This is the only configuration entry used for a Library).

Once all of these details are specified the following actions are performed:

**For Applications:**

1. Configure the OpenShift portions of the Application:
    1. Create the OpenShift ImageStream in the owning Team's DevOps environment. This is where the OpenShift build pushes the built Application images to.
    2. Create the OpenShift BuildConfig in the owning Team's DevOps environment. This performs the S2I build for the Application.
    3. Process the supplied OpenShift Template to create the required deployment resources. This typically will always include an ImageStream and DeploymentConfig.
2. Configure the Jenkins build and default deployments for the Application:
    1. Generate a Jenkinsfile that will build and deploy your application through your default pipeline. The Jenkinsfile is the added to your Application repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile`.
    2. Create a Jenkins build job that uses the generated Jenkinsfile to build your Application. The build job is also added to a Jenkins Job View which holds all the Jenkins jobs related the Application being deployed.
3. For each environment in each release pipeline in your project, configure the Jenkins deployment process:
    1. Generate a Jenkinsfile that will be used to deploy the application into the environment. The Jenkinsfile is the added to your Application repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile.[${pipelineTag}.]${environmentPostfix}` where `[${pipelineTag}.]` is not present if the evironment's owning pipeline has no tag.
    2. Create a Jenkins build job that uses the generated Jenkinsfile to promote your Application from the previous environment. The build job is also added to the Jenkins Job View which holds all the Jenkins jobs related the Application being deployed.

**For Libraries:**

1. Generate a Jenkinsfile that will build your Library. This Jenkinsfile should be modified by the user to push your artifacts somewhere they can be reused from. The Jenkinsfile is the added to your Library repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile`.
2. Create a Jenkins build job that uses the generated Jenkinsfile to build your Library.
---
#### `sub configure package`
When a Package(either an Application or Library) is created in Subatomic, there are no details captured about how it should be built or deployed. It is just a piece of metadata describing the details of a Package's name, whether it is deployable, where it's source code lives etc. The user needs to then tell Subatomic how they wish to build/deploy this Package. Running this command presents the user with a prompt to decide what Package Defintion to apply to the Package. A Package Definition is a preset configuration file which describes the following:

- The S2I ImageStream to use to build an Application.
- The environment variables to set during the S2I build.
- The OpenShift template to process in order to create the Application's OpenShift resources in each deployment environment.
- The environment variables to set in the Deployment Configs created in each OpenShift environment.
- The default Jenkinsfile to add to the Package repository (This is the only configuration entry used for a Library).

The system administrators should create custom Package Definitions for the most common types of Packages used in your orginization and these should appear in the dropdown for selection. After selecting a Package Definition to use all the information is passed through to the `sub configure custom package` command. To find out more about this command click [here](#sub-configure-custom-package).

---
#### `sub configure project bitbucket access`
TODO

---
#### `sub create jenkins bitbucket credentials`
This will recreate the Bitbucket credentials used by Jenkins to access Bitbucket and clone sources used in builds. This should only need to be run in the Service Account credentials have changed.

---
#### `sub jenkins build`
This will kick off a Jenkins dev pipeline build for a selected application. That is it will run the build associated to the standard Jenkinsfile for an Application, and not the additional deployment jobs associated to the Application.

---
#### `sub link application`
This will prompt a user for details about an Application they wish to allow Subatomic to manage. This will require an existing initialised repository in the Bitbucket project associated to the Application's intended owning Subatomic Project. This creates the metadata representation of the Applicaiton within the Subatomic database. Once the Application has been created the user needs to decide how Subatomic should treat the Application. See [sub configure package](#sub-configure-package) for more details.

---
#### `sub onboard me` 
This is the first command any user should run. Without on-boarding yourself you will not be able to run any subatomic commands. You will need to input your `first name`, `last name`, `email address` and `domain username`. Once submitted you will be able to execute subatomic commands granted you have the permission to execute them. For a detailed walk through click [here](../user-guide/onboarding.md).

---
#### `sub patch s2i image`
This looks up the latest versions of s2i ImageStream's available, tags a selected one to your Team DevOps environment, and changes a selected Application's BuildConfig to use updated ImageStream.

---
#### `sub project request jenkins job`
This requests a build folder for a specific project be created. This can either be useful if the build folder is deleted, or a user wants to create builds for a project without creating the OpenShift environments. The usecase for the latter being when a Project only contains libraries and no deployable applications. This performs the following operations:

1. Create the build folder for the Project. The build folder uses the Project's name to name to build folder.
2. Create the environment name credentials within the build folder/job domain. These credentials store the OpenShift namespaces for each environment in your pipeline. E.g. "DEV_PROJECT" - Dev Openshift Project, "TZA_UAT_PROJECT" - UAT OpenShift project for the TZA deployment pipeline.
3. Create the Bitbucket authorization credential. This is used by Jenkins to clone sources from the configured Bitbucket instance.

---
#### `sub request application prod` 
This command can be used to request moving an Application into production. The command when run initially scans the highest non prod environment if the selected pipeline for a DeploymentConfig used by this Application. By traversing the DeploymentConfig a tree of related OpenShift resources related to this Application can be found. The types of resources included in the search are DeploymentConfigs, Services, Routes, PersistentVolumeClaims, and ImageStreams. The user is presented with the list of identified resources, and confirms they are happy to move these into the production in environments. Upon confirmation the following actions are performed:

1. Move across all identified resources into each production environment.
2. Generate a Jenkinsfile that will be used to deploy the application into prod. The Jenkinsfile is the added to your Application repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile.[${pipelineTag}.]${environmentPostfix}` where `[${pipelineTag}.]` is not present if the deployment's owning pipeline has no tag.
3. Create a Jenkins build job that uses the generated Jenkinsfile to deploy your Application. The build job is also added to the Jenkins Job View which holds all the Jenkins jobs related the Application being deployed.

