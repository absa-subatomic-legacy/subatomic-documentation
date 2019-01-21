# **Link an Application**
At this point in the guide you should have been presented with a prompt to link an existing application to your project. You should have arrived at this point through the conversational prompts presented after creating a project. Note that you can also link an existing application using the command below in your team channel

`@atomist sub link application`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#link-application)

Below is an example of linking the existing application to your project

![Add Application](/images/user-guide/add-an-application/add-application.png)

The flow for adding an existing application is different to all the commands encounterd so far. First the prompts for an application name and description are shown. Enter these and submit them when you are satisfied with your values. Subatomic will then pull a list of all the repositories in your Bitbucket project and you can select which one holds the source for the application you wish to use. Once you have made your selection you will be informed that your application is being created.

## **Configure Component**
You will be presented with button to configure your component. Upon selection you will have the option to choose which package definition to use for your project. E.g. for a springboot-1 project you would choose `maven-springboot-1-deployable`. Theses contain predefined definitions, if you would like to specify which components to use rather use the [sub configure custom package](../quantum-mechanic/command-reference.md#configure-custom-package) instead.

`@atomist sub configure package`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#configure-package)

![Configure Component](/images/user-guide/add-an-application/configure-component.png)

Upon completion of the configuration you will see the following type of message:

![Configuring Application](/images/user-guide/add-an-application/ConfiguringPackage.png)

## **Jenkins Build**
The application should now be provisioned and you are presented with an option to kick off a build. Note that if your application did not have a Jenkins build file, Subatomic will generate one for you and add it to your application repository. The message should look as below

![Start Build](/images/user-guide/add-an-application/start-jenkins-build.png)

Start the build by choosing the presented option. The jenkins build can also be started by using the command below in your channel

`@atomist sub jenkins build`

> For details on the use of this command please see [here](../quantum-mechanic/command-reference.md#jenkins-build)

You should be notified that your application is now being built. The build is started using your Jenkins master instance in your DevOps environment. The link to your jenkins instance can be found in the DevOps environment and logging into the instance will then allow you to track/promote and deploy your builds.

![Jenkins Build Complete](/images/user-guide/add-an-application/JenkinsBuild.png)