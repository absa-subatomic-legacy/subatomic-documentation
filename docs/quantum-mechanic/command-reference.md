# **Quantum Mechanic**
Quantum Mechanic is the interactive Slack interface of Subatomic. Below are the commands and their explanations that you'll encounter while interacting with this interface.

## Quick Reference
The below sections have the commands grouped by functionality and with very brief explanations to help you browse them. You can use the links for the commands to navigate to the full description of what each command does.

###  **Bitbucket Commands**
Bitbucket commands that control Bitbucket project configuration and access controls

1. [`sub apply bitbucket practices`](#sub-apply-bitbucket-practices) - Apply recommended practices to Bitbucket project

###  **Jenkins Commands**
Jenkins commands that allow the user to control builds and Jenkins configuration

1. [`sub configure application jenkins prod`](#sub-configure-application-jenkins-prod) - Add a prod deployment job to Jenkins for an application
2. [`sub create jenkins default credentials`](#sub-create-jenkins-default-credentials) - Recreate the Jenkins default credentials
3. [`sub jenkins build`](#sub-jenkins-build) - Kick off a Jenkins build
4. [`sub project request jenkins job`](#sub-project-request-jenkins-job) - Creates a Jenkins build folder for a given project

###  **Member Commands**
Member commands allow you to manage Subatomic members. These include editing Slack details, on-boarding, editing user roles and adding members to teams.

1. [`sub add team member`](#sub-add-team-member) - Add a member to a team
2. [`sub add team owner`](#sub-add-team-owner) - Add a member as an owner to a team
3. [`sub onboard me`](#sub-onboard-me) - The most important command, without on-boarding yourself you will not be able to run any subatomic commands. You will need to input your `first name`, `last name`, `email address` and `domain username`. Once submitted you will be able to execute subatomic commands granted you have the permission to execute them. For a detailed walk through click [here](../user-guide/onboarding.md).


###  **Package Commands**
Package commands are related to managing applications and libraries. These include deployment, build, prod promotion and image management.

1. [`sub configure application jenkins prod`](#sub-configure-application-jenkins-prod) - Add a prod deployment job to Jenkins for an application
2. [`sub configure package`](#sub-configure-package) - Configure an existing application/library using a predefined template
3. [`sub configure custom package`](#sub-configure-custom-package) - Configure an existing application/library manually specifying all build/deployment details.
4. [`sub request application prod`](#sub-request-application-prod) - Create application in prod
5. [`sub link application`](#sub-link-application) - Link an existing application
6. [`sub link library`](#sub-link-library) - Link an existing library
7. [`sub patch package s2i image`](#sub-patch-package-s2i-image) - Patch the s2i image used to build a package

###  **Project Commands**
Project commands provide management capabilities around individual Projects and their associated resources. This includes environment management, application and library creation, Jenkins and Bitbucket configuration.

1. [`sub associate team`](#sub-associate-team) - Add additional team/s to a project
2. [`sub configure project bitbucket access`](#sub-configure–project-bitbucket–access) - Reconfigure user and system access to Bitbucket for an existing project
3. [`sub apply bitbucket practices`](#sub-apply-bitbucket-practices) - Apply recommended practices to Bitbucket project
4. [`sub request generic prod`](#sub-request-generic-prod) - Move OpenShift resources to prod
5. [`sub create openshift pvc`](#sub-create-openshift-pvc) - Create a new OpenShift Persistent Volume Claim
6. [`sub create project`](#sub-create-project) - Create a new project. You will need to input two values `project name` and `project description`.
7. [`sub request project prod`](#sub-request-project-prod) - Create the OpenShift production environments for a project and a particular pipeline.
8. [`sub link application`](#sub-link-application) - Link an existing application
9. [`sub link library`](#sub-link-library) - Link an existing library
10. [`sub link bitbucket project`](#sub-link-bitbucket-project) - You will need to input your `bitbucket project key` and Subatomic will find the existing project within Bitbucket.
11. [`sub list projects`](#sub-list-projects) - List projects belonging to a team
12. [`sub request project environments`](#sub-request-project-environments) - Create new OpenShift environments for a project
13. [`sub project request jenkins job`](#sub-project-request-jenkins-job) - Creates a Jenkins build folder for a given project

###  **Team Commands**
Team commands allow you to manage your Subatomic team. These include team membership, team projects and DevOps environment configuration.

1. [`sub add config server`](#sub-add-config-server) - Add a new Subatomic Spring Cloud Config Server
2. [`sub add team member`](#sub-add-team-member) - Add a member to a team
3. [`sub add team owner`](#sub-add-team-owner) - Add a member as an owner to a team
4. [`sub associate team`](#sub-associate-team) - Add additional team/s to a project
5. [`sub create team`](#sub-create-team) - You will need to input two values `team name` and `team description`. This will create a team with the respective values in Subatomic.
6. [`sub apply to team`](#sub-apply-to-team) - Apply to join an existing team
7. [`sub link team channel`](#sub-link-team-channel) - If you already have an existing slack channel use this command. Subatomic will add the atomist bot to this channel, however if the channel is private you will need to manually invite the bot.
8. [`sub list team members`](#sub-list-team-members) - Displays members and owners of the team.
9. [`sub team migrate cloud`](#sub-team-migrate-cloud) - Move all OpenShift resources belonging to a team to a different cloud
10. [`sub request devops environment`](#sub-request-devops-environment) - Create a DevOps environment for a selected Team.
11. [`sub create team channel`](#sub-create-team-channel) - This will create a public slack channel, if you want a private channel you will need to create it manually then run [`sub link team channel`](#sub-link-team-channel) command.
12. [`sub remove team member`](#sub-remove-team-member) - Removes a member from a team.

###  **Other Commands**
All other general/miscellaneous commands

1. [`sub create openshift pvc`](#sub-create-openshift-pvc) - Create a new OpenShift Persistent Volume Claim
2. [`sub team migrate cloud`](#sub-team-migrate-cloud) - Move all OpenShift resources belonging to a team to a different cloud
3. [`sub help`](#sub-help) - Displays a help menu as a Slack browsable form of the Quick Reference section of this page.

## Detailed Reference
This section is dedicated to explaining in detail what each command does. The subatomic environment is designed to speed up developer workflow, but it should never prevent users from using the underlying stack directly if needed or desired.
The information here is put in place to help users understand exactly what is going on under the hood so that clarity is provided and manual execution of each command could be performed if desired.

---
#### `sub add config server`
This command is used to create a [Spring Cloud Config](https://spring.io/projects/spring-cloud-config) server for a team. The config server is configured to point to a single repository where application configuration is pulled from. The command itself performs the following steps:

1. The Secret `subatomic-config-server` is created in the teams DevOps environment. This Secret contains the ssh key configuration required by the config server to access your Bitbucket config repository.
2. The ConfigMap `subatomic-config-server` is created in the teams DevOps environment. This contains the default `application.yml` configuration used by the config server.
3. The `subatomic-config-server` ImageStream is tagged into the teams DevOps environment.
4. The `default` service account is granted view rights since this is required to run the config server.
5. The `subatomic-config-server-template` Template is then processed to created the necessary DeploymentConfig and Service in OpenShift.

---
#### `sub add team owner`
This is used to directly add a user to a Team you are the owner of with owner permissions. The user will need to have been on-boarded before you can add them to the Team. Adding user as an owner performs the following operations:

1. Associate the user to the Team in the Subatomic database as an owner.
2. Add the user to all OpenShift namespaces associated to the Team and grant them Admin permissions.
3. Add the user to the Bitbucket projects for each Subatomic Project associated to the team. They are granted Admin rights on the Bitbucket projects.
4. Invite the new user to the Team's slack channel.


---
#### `sub add team member`
This is used to directly add a user to a Team you are the owner of with member permissions. The user will need to have been on-boarded before you can add them to the Team. Adding user as a member performs the following operations:

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
#### `sub apply to team`
This command allows users to send a request to a Team asking to be added as a member of that team. When executing this command, a membership request is created to the Team and Slack notification with Approve and Reject options is sent to the Team. An owner of the team needs to approve or reject this request. If the membership request is approved, the following actions are performed:

1. Associate the user to the Team in the Subatomic database as a member.
2. Add the user to all OpenShift namespaces associated to the Team and grant them Write permissions.
3. Add the user to the Bitbucket projects for each Subatomic Project associated to the team.
4. Invite the new user to the Team's slack channel.

---
#### `sub associate team`
This allows users to associate additional Teams to a Subatomic Project. Users of these associated Teams are granted permissions to all the Project source code and deployment environments. Additionally any Project notifications will be shown in the newly associated Team's Slack channel.

---
#### `sub configure application jenkins prod`
When running a Generic Prod request, all OpenShift resources in the highest non-prod environment are indiscriminately moved over to the production environments. This is just a straight copy of the resources, and **does not** configure any Jenkins jobs for Application production deployments.
This command is used to create just the Jenkins jobs for deploying an application into production environments following such a resource copying operation. The following steps are performed in order to do this:

1. Generate a Jenkinsfile that will be used to deploy the application into prod. The Jenkinsfile is the added to your Application repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile.[${pipelineTag}.]${environmentPostfix}` where `[${pipelineTag}.]` is not present if the deployment's owning pipeline has no tag.
2. Create a Jenkins build job that uses the generated Jenkinsfile to deploy your Application. The build job is also added to the Jenkins Job View which holds all the Jenkins jobs related to the Application being deployed.

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
    1. Generate a Jenkinsfile that will be used to deploy the application into the environment. The Jenkinsfile is then added to your Application repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile.[${pipelineTag}.]${environmentPostfix}` where `[${pipelineTag}.]` is not present if the environment's owning pipeline has no tag.
    2. Create a Jenkins build job that uses the generated Jenkinsfile to promote your Application from the previous environment. The build job is also added to the Jenkins Job View which holds all the Jenkins jobs related to the Application being deployed.

**For Libraries:**

1. Generate a Jenkinsfile that will build your Library. This Jenkinsfile should be modified by the user to push your artifacts somewhere they can be reused from. The Jenkinsfile is then added to your Library repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile`.
2. Create a Jenkins build job that uses the generated Jenkinsfile to build your Library.

---
#### `sub configure package`
When a Package(either an Application or Library) is created in Subatomic, there are no details captured about how it should be built or deployed. It is just a piece of metadata describing the details of a Package's name, whether it is deployable, where it's source code lives etc. The user needs to then tell Subatomic how they wish to build/deploy this Package. Running this command presents the user with a prompt to decide what Package Definition to apply to the Package. A Package Definition is a preset configuration file which describes the following:

- The S2I ImageStream to use to build an Application.
- The environment variables to set during the S2I build.
- The OpenShift template to process in order to create the Application's OpenShift resources in each deployment environment.
- The environment variables to set in the Deployment Configs created in each OpenShift environment.
- The default Jenkinsfile to add to the Package repository (This is the only configuration entry used for a Library).

The system administrators should create custom Package Definitions for the most common types of Packages used in your orginisation and these should appear in the dropdown for selection. After selecting a Package Definition to use all the information is passed through to the `sub configure custom package` command. To find out more about this command click [here](#sub-configure-custom-package).

---
#### `sub configure project bitbucket access`
This command is used to assign the necessary permissions to a Project's associated Bitbucket Project. This is useful if either the Subatomic service account has lost permissions, users permissions were changed, or your repositories have been migrated to a new Bitbucket instance. In particular the following permissions are set up:

1. Give the Subatomic service account admin permissions.
2. Give Team owners admin permissions.
3. Give Team members write permissions.

---
#### `sub create jenkins default credentials`
This will recreate the default credentials used by Jenkins. This can be run if the Bitbucket Service Account credentials have changed or if the Jenkins credentials are generally out of date. In particular this creates the following credentials:

1. Bitbucket Credentials - Used to access Bitbucket.
2. Nexus - Stores the URL of the Nexus instance to use for builds.
3. Docker - Stores the Docker registry url used to specify locations of images that Jenkins uses (e.g. Jenkins agent images)
4. Shared Resources Namespace - Stores the name of the Subatomic shared resource OpenShift namespace. This is used to know which namespace to look for centralised images in.
5. Maven - This is the default Maven settings used in Maven builds.

---
#### `sub create openshift pvc` 
This command can be used to either add a PersistentVolumeClaim to a particular environment, or to every environment in a Project pipeline based on user selection.

---
#### `sub create project` 
This command can be used to create a new Subatomic Project associated to a particular Team. This just creates the metadata representation of the project within the Subatomic database. After creating a Project, you will need to associate it to a Bitbucket Project which you should be prompted for. More information about associating a Subatomic Project to a Bitbucket project can be found [here](#sub-link-bitbucket-project). Once the Project has been fully defined, this captured metadata can then be used as the input into 'templates' that create things such as [new OpenShift environments](#sub-request-project-environments), or [Jenkins build jobs](#sub-project-request-jenkins-job).

---
#### `sub create team` 
This command can be used to create a new Subatomic Team. This only creates the metadata model of the Team in the Subatomic database. This can then be used as the base to create a DevOps environment and create new Project's under. **Note:** When creating a new team, the user that executes the command will be made the owner of this Team.

---
#### `sub create team channel` 
This command will create a Slack channel with the supplied name and assign it as the Team's associated Subatomic Slack channel. The following actions are performed when running this command:

1. Create a Slack channel with the chosen name.
2. Assign the Slack channel to the Team's associated Subatomic slack channel in the Subatomic database.
3. Invite the Atomist bot to the newly created Slack channel.
4. Invite all Team owners and members to the newly created Slack channel.

**Note:** When following the message prompts after creating a Team, the Slack channel will automatically be created using the Team's name in kebab case format.

---
#### `sub help`
Displays a help menu as a Slack browsable form of the Quick Reference section of this page.

---
#### `sub jenkins build`
This will kick off a Jenkins dev pipeline build for a selected application. That is it will run the build associated to the standard Jenkinsfile for an Application, and not the additional deployment jobs associated to the Application.

---
#### `sub link application`
This will prompt a user for details about an Application they wish to allow Subatomic to manage. This will require an existing initialised repository in the Bitbucket project associated to the Application's intended owning Subatomic Project. This creates the metadata representation of the Application within the Subatomic database. Once the Application has been created the user needs to decide how Subatomic should treat the Application. See [sub configure package](#sub-configure-package) for more details.

---
#### `sub link bitbucket project`
When creating a Project in Subatomic, the Subatomic Project needs to be associated to a Bitbucket project. This command is used to do this linking. In order to link the Bitbucket project to the Subatomic Project the user needs to provide the Bitbucket project key. Instructions on finding this Bitbucket project key can be found in the [FAQ](../FAQ.md#sub-link-bitbucket-project).

---
#### `sub link library`
This will prompt a user for details about a Library they wish to allow Subatomic to manage. This will require an existing initialised repository in the Bitbucket project associated to the Application's intended owning Subatomic Project. This creates the metadata representation of the Library within the Subatomic database. Once the Library has been created the user needs to decide how Subatomic should treat the Library. See [sub configure package](#sub-configure-package) for more details.

---
#### `sub link team channel`
This command allows a user to link their Team to a new Slack channel for notification purposes. The Slack channel needs to exist for this command to work correctly. This is particularly useful if the currently associated Team channel was renamed, if you want to use a private slack channel(\*) for the team notifications, or if you have an existing channel you wish to use for the notifications and Subatomic control flow interaction. When linking a Team to a new Slack channel the following actions are performed:
1. Invite the Members of the Team to the Slack channel.
2. Invite the Atomist Bot to the Team Channel.

The Atomist Bot should present a generic message about creating a DevOps environment whenever it joins a new channel that is associated to a Team.

**\*Note:** If you want to use a private Slack channel, the Atomist bot cannot be invited automatically. You will need to manually invite the bot the to channel using `\invite @Atomist` once you have linked the Team to the Slack channel.

---
#### `sub list projects`
This command is used to provide users a way to view the details around what Projects are linked to a particular team. These details include the Project names and associated Bitbucket projects, along with options to drill down into each Project's associated Package details.

---
#### `sub list team members`
This will present a list of the Team owners and users. This is useful to know who can perform actions that require ownership permission.

---
#### `sub onboard me` 
This is the first command any user should run. Without on-boarding yourself you will not be able to run any subatomic commands. You will need to input your `first name`, `last name`, `email address` and `domain username`. Once submitted you will be able to execute subatomic commands granted you have the permission to execute them. For a detailed walk through click [here](../user-guide/onboarding.md).

---
#### `sub patch package s2i image`
This looks up the latest versions of s2i ImageStream's available in the centralised resources namespace, and changes a selected Application's BuildConfig to use the updated ImageStream.

---
#### `sub project request jenkins job`
This requests a build folder for a specific project be created. This can either be useful if the build folder is deleted, or a user wants to create builds for a project without creating the OpenShift environments. The use case for the latter being when a Project only contains libraries and no deployable applications. This performs the following operations:

1. Create the build folder for the Project. The build folder uses the Project's name to name the build folder.
2. Create the environment name credentials within the build folder/job domain. These credentials store the OpenShift namespaces for each environment in your pipeline. E.g. "DEV_PROJECT" - Dev OpenShift Project, "TZA_UAT_PROJECT" - UAT OpenShift project for the TZA deployment pipeline.
3. Create the Bitbucket authorization credential. This is used by Jenkins to clone sources from the configured Bitbucket instance.

---
#### `sub remove team member` 
This command is used to remove a member from a Team. This action can only be performed by a Team owner. When removing a member from a team, the following actions are performed:

1. Remove the Subatomic association between the user and the Team.
2. Remove the user's permissions from all OpenShift namespaces associated to the Team.
3. Remove the user's permissions from the Bitbucket project's associated to the Team.
4. Kick the user from the Team's Slack channel.

**Note:** Team owners can also be removed (including self removal), provided that there is currently more than 1 Team owner.

---
#### `sub request application prod` 
This command can be used to request moving an Application into production. The command when run initially scans the highest non prod environment if the selected pipeline for a DeploymentConfig used by this Application. By traversing the DeploymentConfig a tree of related OpenShift resources related to this Application can be found. The types of resources included in the search are DeploymentConfigs, Services, Routes, PersistentVolumeClaims, and ImageStreams. The user is presented with the list of identified resources, and confirms they are happy to move these into the production in environments. Upon confirmation the following actions are performed:

1. Move across all identified resources into each production environment.
2. Generate a Jenkinsfile that will be used to deploy the application into prod. The Jenkinsfile is the added to your Application repository if it does not exist. The name of the Jenkinsfile is `Jenkinsfile.[${pipelineTag}.]${environmentPostfix}` where `[${pipelineTag}.]` is not present if the deployment's owning pipeline has no tag.
3. Create a Jenkins build job that uses the generated Jenkinsfile to deploy your Application. The build job is also added to the Jenkins Job View which holds all the Jenkins jobs related the Application being deployed.

---
#### `sub request devops environment` 
A DevOps environment is an OpenShift namespace which acts as a shared environment for common infrastructure across all of a Team's Projects. This by default includes a Jenkins instance used to build all Applications and Libraries in a Team's associated Projects and includes all the BuildConfigs used to run the S2I builds for the Team. Additional infrastructure such as a Spring Cloud Config server or Key Cloak server would be added to the DevOps environment and shared across all Project environments. When running this command, the following actions will be performed: 

1. Create the OpenShift namespace for the Team. This will be named `${teamName}-${devops}` using kebab casing.
2. Apply the system admin set default OpenShift Limits and Quota's to the new namespace.
3. Give all Team members write permissions to the DevOps namespace.
4. Give all Team owners admin permissions to the DevOps namespace.
5. Create a secret `bitbucket-ssh` which contains the credentials required by the shared DevOps applications to access Bitbucket.
6. Deploy an instance of Jenkins.
7. Load in all the credentials required by Jenkins. More information on these credentials can be found [here](#sub-create-jenkins-default-credentials)

---
#### `sub request generic prod` 
This command can be used to request moving all OpenShift resources in a non prod environment to the production environments. This is useful for if you have created resources that are not directly associated to a Subatomic Application (like a custom deployment or build) and you are taking the Project to production for the first time. This command when run initially scans the highest non prod environment looking for all DeploymentConfigs, Services, Routes, PersistentVolumeClaims, and ImageStreams. The user is presented with the list of identified resources, and confirms they are happy to move these into the production in environments. Upon confirmation all identified resources are copied in each production environment. **Note:** If your project is purely Subatomic created, then the recommended process is to just use the [`sub request application prod`](#sub-request-application-prod) command to move each application to production individually.

---
#### `sub request project environments` 
After creating a Subatomic Project, a user can request that the Project have OpenShift environments provisioned for its use. When requesting these environments, if the Project has not had its build/dev and release pipelines defined, the Project will be assigned a default pipeline structure. The following actions are then performed:

1. Configure the Project OpenShift resources:
    1. Create an OpenShift namespace created for each environment of each deployment and release pipeline associated to a Project.
    2. Assign default OpenShift Quota and Limits and apply a standard OpenShift Project namespace template to these namespaces. The default template, Quota's, and Limits, will be customised by your System Admin to meet the requirement of the organisation's space.
    3. Create a Pod Network between each OpenShift Project Namespace and the Team's DevOps namespace. This allows the Applications in the Project namespaces to access Application's in the DevOps space via service URI's (e.g. accessing the DevOps Config Server).
2. Configure the Project in Jenkins:
    1. Create the build folder for the Project. The build folder uses the Project's name to name the build folder.
    2. Create the environment name credentials within the build folder/job domain. These credentials store the OpenShift namespaces for each environment in your pipeline. E.g. "DEV_PROJECT" - Dev OpenShift Project, "TZA_UAT_PROJECT" - UAT OpenShift project for the TZA deployment pipeline.
    3. Create the Bitbucket authorization credential. This is used by Jenkins to clone sources from the configured Bitbucket instance.

---
#### `sub request project prod` 
In order to promote Applications to production, you need to have production environments available to deploy the Application's into. This command will allow users to provision these production environments for a selected Project and deployment pipeline. The process follows the following approach:

1. Request that the Team members put their names down in a sign off process to approve that the Project is ready for production:
    1. If a user rejects the approval request, the entire Prod Request is cancelled.
    2. You need at least 3 approvals to have the Prod Request approved. If you have less that 3 team members, then instead all Team members need to approve this request.
2. Once the request is approved the following actions are then performed
    1. A Team DevOps OpenShift namespace is created on each production cluster if it does not exists already.
    2. A Project Pipeline OpenShift namespace is created on each production cluster.
    3. A pod network is setup so that the Applications in the production Project environments can communicate with the DevOps environment services.

Once a Project pipeline has been moved to production then the Applications within the Project can be setup to move into production. For more information on this look at [`sub request generic prod`](#sub-request-generic-prod) and [`sub request application prod`](#sub-request-application-prod).

---
#### `sub team migrate cloud` 
When a Team in Subatomic is created, it is associated to a particular "cloud". A cloud represents a group of OpenShift clusters that are grouped into a non prod cluster, and multiple production clusters. Provided that the Subatomic deployment has been configured to use multiple "clouds", this command can be used to migrate a Team and all associated Projects from one cloud to another cloud. The steps in this operation are as follows:

1. Create a new DevOps environment on the new cloud's non prod cluster.
2. Recreate all OpenShift namespaces from all Projects associated to the Team being migrated.
3. Copy all OpenShift resources from the original environments to the newly created OpenShift environments. This includes DeploymentConfig, Service, Route, PersistentVolumeClaim, and ImageStream resources.
4. Recreate the Jenkins build jobs for each Application associated to the Project.
