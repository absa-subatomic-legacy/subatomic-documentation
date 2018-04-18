# **Create a Project**
At this point in the guide you should have been presented with a prompt to create a new project. You should have arrived at this point through the conversational prompts presented after creating your team and associated a slack channel to it. Note that project creation can also be invoked through the command run in your team channel as below

`@atomist sub create project`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#create-project)

When talking to the Atomist bot in a channel, conversational prompts will occur in a thread. Follow the prompts and enter the necessary values for you project. An example of this is seen below

![Project Creation](/images/user-guide/create-a-project/create-a-project.png)

Re-assign the values if necessary and submit when ready.

## **Linking a Bitbucket Project**
You should now be presented with options to link or create a Bitbucket project to associate to the Subatomic project, and an option to create the necessary OpenShift environments. 

![Post Project Creation](/images/user-guide/create-a-project/post-project-creation.png)

Choose the option to link an existing Bitbucket project. This can also be invoked using the command below in the channel

`@atomist sub link bitbucket project`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#link-bitbucket-project)

> For details on creating a new Bitbucket project see the [documentation](../quantum-mechanic/command-reference.md#create-bitbucket-project)

Follow the prompts to link the bitbucket project. An example is shown below

![Link Bitbucket](/images/user-guide/create-a-project/link-bitbucket-project.png)

Note that the Bitbucket project key is pulled from the URL of the project. The URL shown when browsing the Test project above is as follows with the project key highlighted

![Bitbucket URL](/images/user-guide/create-a-project/bitbucket-url.png)

Submit the command and you should be informed once the Bitbucket project has been configured. The configuration involves giving access to all members in your team access, and setting default merge checks and default reviewers for the project. 

## **Create OpenShift Environments**

You should now be prompted to create the associated Openshift evnironments for the project

![Post Link Bitbucket](/images/user-guide/create-a-project/post-link-bitbucket.png)

Click the "Create OpenShift environments" button. This command can also be invoked using the command below in the team channel

`@atomist sub request project environments`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#request-project-environments)

You will be notified that your Openshift environments are being provisioned and once they are complete they should be visible in your Openshift instance.

![Openshift Environments](/images/user-guide/create-a-project/openshift-environments.png)

Currently the DEV, SIT, and UAT environments are the default and only option. These will host all the applications within the project you have created. The environments have user permissions and quota's automatically configured for your team.

## **Add an Application**

Once the project environments were provisioned you should have been prompted to create a new application in the project.

![Create Application](/images/user-guide/create-a-project/create-an-application.png)

Choose to link an existing application and proceed to [Add an Application](./add-an-application).

> For details on linking an existing library see the [documentation](../quantum-mechanic/command-reference.md#link-library)