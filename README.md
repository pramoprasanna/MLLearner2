### Boston Housing Price Prediction

### Software and Tools Required

1. [GitHub Accounts](https://github.xom)
2. [GitCLI](https://git-scm.com/docs/gitcli)
3. [PyCharm IDE](https://www.jetbrains.com/pycharm/download/?section=windows)
	• IDE used - Pycharm Community version
	• Python version - 3.12
4. [HerokuAccount]
5. [VirtualEnvironment Setup]
		○ https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
		○ https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3

# MLLearner2

Following as per for Learning and Practise

https://www.youtube.com/watch?v=MJ1vWb1rGwM&t=1394s

### Create a New Environment

			§ Venv setup:
				§ python3 -m pip install --upgrade pip
				§ pip3 install virtualenv < pkg installation>
				§ Create virtual environment : pip3 install virtualenv
				§ Cd to Directory => .\Activate.ps1
				§  pip list =>  To list all packages installed
				§ https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements
			§ python '.\Sample Model1.py'

## FLASK Service creation as described in video 

https://www.youtube.com/watch?v=MJ1vWb1rGwM&t=1394s

## DEPLOY in GCP Using below once it works locally using above

GCP Deploy steps: [ Reference : https://www.youtube.com/watch?v=xcODUk0o6tU&t=2s ]
	1. 2 main things necessary in project code - File called main.py which is the entry point for GCP and file called app.yaml with the runtime version of Python in format - runtime:python312
	2. Open URL https://console.cloud.google.com/ , Go to IAM and Admin on Left Tab , Open Manage Resources , Add New Project 
	3. Install SDK from URL https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe locally. This is to deploy the code from local into Google Cloud.
	4. Open the Command prompt in folder path where the project is present in local
	5. Run the below commands:
		a. gcloud init ,  Choose the google account that can be used to perform this operation , select the project . This sets the project in GCP as required.
		b.  gcloud app deploy app.yaml --project <<Projectname>>  chosen in above step. Files gets uploaded. Select the region . This step creates an app engine. Target URL available in the logs is the URL on which this model service becomes available
Disable Application at the end to avoid overusing the Limit - https://console.cloud.google.com/appengine?serviceId=default&project=bostonhousing-423115