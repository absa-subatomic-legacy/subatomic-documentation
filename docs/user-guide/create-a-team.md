# Create a Team
At this point in the guide you should have been presented with a prompt to create a new team. You should have arrived at this point through the conversational prompts presented after onboarding your user. Note that team creation can also be invoked through the command

`sub create team`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference-index.md#create-team)

After invoking the team creation command follow the prompts and enter the details for the team as required. Below is an example of creating a team

![Team Creation](/images/user-guide/create-a-team/team-creation.png)

The values entered can be modified or submitted as before. Submitting the values creates and stores a new team with nothing associated to it within the Subatomic environment. 

## Associate a Slack Channel

You are then prompted to associate a slack channel to this team. Follow the prompts to link the slack channel, and choose to either create a new channel or link an existing channel to the team. Below is an example of creating a new slack channel to associate to the team.

![Slack Channel Creation](/images/user-guide/create-a-team/create-slack-channel.png)

A slack channel can also be created using the command

`sub create team channel`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference-index.md#create-team-channel)

Aleternatively an existing channel can also be linked using the command

`sub link team channel`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference-index.md#link-team-channel)

The slack channel is then automatically created and the Atomist bot is invited. Below shows the welcome message sent by the Atomist bot when it joins your channel

![Atomist Joins](/images/user-guide/create-a-team/atomist-joins.png)

> If linking an existing channel that is private, there will be some manual steps involved to invite the atomist bot to your private channel.

## Create a DevOps Environment

You should now provision your DevOps environment by clicking on the "Create DevOps environment" button. This command can also be invoked using the command (note the `@atomist` prefix, which is required when sending commands in a channel instead of through direct messages to the atomist bot)

`@atomist sub request devops environment`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference-index.md#request-devops-environment)

A message is shown when provisioning starts and you are informed when the provisioning is complete. When the provisioning is complete your team will have a DevOps project created inside Openshift. This project hosts your jenkins master along and possibly a config server that will be used by your team's applications. Permissions for all members of your team are automatically configured. Below shows an example of the Openshift DevOps project overview

![DevOps Environment](/images/user-guide/create-a-team/devops-env-created.png)

The team channel is updated with a message detailing possible next steps as seen below

![Post DevOps Steps](/images/user-guide/create-a-team/devops-slack-message.png)

For this guide proceed by clicking the "Create project" button and proceed to [Create a Project](./create-a-project.md)

> For details on adding a config server see the [documentation](../quantum-mechanic/command-reference-index.md#add-config-server)