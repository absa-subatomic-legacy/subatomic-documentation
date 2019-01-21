## **Create a Team**
At this point in the guide you should have been presented with a prompt to create a new team. You should have arrived at this point through the conversational prompts presented after onboarding your user. Note that team creation can also be invoked through the command

`sub create team`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#team-commands)

After invoking the team creation command follow the prompts and enter the details for the team as required. Below is an example of creating a team

![Team Creation](/images/user-guide/create-a-team/team-creation.png)

The values entered can be modified or submitted as before. Submitting the values creates and stores a new team with nothing associated to it within the Subatomic environment. 

You will now be prompted to choose a cloud to create this team in. 
![Choose a cloud](/images/user-guide/create-a-team/choose a cloud.png)


After your cloud selection the command will process and you should receive a success message.

## **Associate/Create a Slack Channel**

You are now prompted to associate a slack channel to this team. Follow the prompts to link the slack channel, and choose to either create a new channel or link an existing channel to the team. Below is an example of creating a new slack channel to associate to the team.

![Slack Channel Creation](/images/user-guide/create-a-team/create-slack-channel.png)

> If linking an existing channel that is private you will need to manually invite the Atomist bot to the channel.


A slack channel can also be created using the command

`sub create team channel`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#team-commands)

Alternatively an existing channel can also be linked using the command

`sub link team channel`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#team-commands)

The slack channel is then automatically created and the Atomist bot is invited. 


## **Create a DevOps Environment**

Select the channel just created in the Slack Channel menu.

Below shows the welcome message sent by the Atomist bot when it joins your channel

![Atomist Joins](/images/user-guide/create-a-team/CreateDevOpsPrompt.png) You can now provision your DevOps environment by clicking on the "Create DevOps environment" button. This command can also be invoked using the command (note the `@atomist` prefix, which is required when sending commands in a channel instead of direct messages to the atomist bot)

`@atomist sub request devops environment`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#team-commands)

A message is shown when provisioning starts and a step by step status message is shown:

![Atomist status request DevOps](/images/user-guide/create-a-team/request-devops.png)

Once the DevOps provisioning is complete the team channel is updated with a message detailing possible next steps as seen below

![Post DevOps Steps](/images/user-guide/create-a-team/ProvisionDevOpsSuccess.png)

When the provisioning is complete your team will have a DevOps project created inside Openshift.
 
 This project hosts your jenkins master along with a possible config server that will be used by your team's applications. Permissions for all members of your team are automatically configured. Below shows an example of the Openshift DevOps project overview

![DevOps Environment](/images/user-guide/create-a-team/devops-env-created.png)

For this guide proceed by clicking the "Create project" button and proceed to [Create a Project](./create-a-project.md)

> For details on adding a config server see the [documentation](../quantum-mechanic/command-reference.md#team-commands)
