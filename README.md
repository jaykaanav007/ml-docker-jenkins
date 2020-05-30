# ml-docker-jenkins# 
Task Description is as follows below :-
1. Create container image that’s has Python3 and Keras or numpy installed using dockerfile 

2. When we launch this image, it should automatically starts train the model in the container.

3. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4. Job1 : Pull the Github repo automatically when some developers push repo to Github.

5. Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

6. Job3 : Train your model and predict accuracy or metrics.

7. Job4 : if metrics accuracy is less than 80% , then tweak the machine learning model architecture.

8. Job5: Retrain the model or notify that the best model is being created

9. Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left.

Solution for the task is as follows below :-
![image](https://user-images.githubusercontent.com/61894395/83334624-667dd100-a2c5-11ea-929e-6614164958d1.png)
# Integrating Jenkins , Github and Docker
# Creating the Docker Image :-
we can create our own docker image by creating a Dockerfile based on our requirements and just mention OS name which you want to use it as the base OS in your dockerfile and install the respective packages and its dependency .
![image](https://user-images.githubusercontent.com/61894395/83334710-f1f76200-a2c5-11ea-9c1a-c5ae2a62cfc6.png)
In my case i have used centos latest version as my base os for my dockerfile and installed the python interpreter and and some dependency for the open cv and overcommited the memory due to extra space issue.

# About Jenkins :-
Being one of the powerful tool in the world of DevOps, Jenkins offers a simple way to set up a continuous integration or continuous delivery (CI/CD) environment for almost any combination of languages and source code repositories using pipelines, as well as automating other routine development tasks. While Jenkins doesn’t eliminate the need to create scripts for individual steps, it does give you a faster and more robust way to integrate your entire chain of build, test, and deployment tools than you can easily build yourself.The plugins of Jenkins makes it powerful.

For this task, we will need the Plugins which are as follows below:-
GitHub Plugin

Email Notification Plugin

Build Pipeline Plugin

Downstream-Ext Plugin

# Job1
In job1 as soon as the developer commits the code then the job1 is triggered .
![image](https://user-images.githubusercontent.com/61894395/83334887-24ee2580-a2c7-11ea-8cfd-02c22d600158.png)
![image](https://user-images.githubusercontent.com/61894395/83334895-35060500-a2c7-11ea-92bf-ac4812191750.png)
My GitHub Link

https://github.com/jaykaanav007/ml-docker-jenkins

the above mentioned is my github repository url where you can find the all the code that i have used in my task

In job 1 as soon as the developer commits his code then job1 will trigger the job1 ,it will download the the code from the git repository which we have mentioned in the the job1 and and save the code in its workspace and when we execute the command which we have mentioned in the build script in mycase it copys the code into the loccal system that is RedHat
![image](https://user-images.githubusercontent.com/61894395/83334917-5d8dff00-a2c7-11ea-93e0-142db80af6e1.png)
# Job 2
Job 2 is build only if the job1 is sucessful
![image](https://user-images.githubusercontent.com/61894395/83334996-a80f7b80-a2c7-11ea-8514-0fece8a35990.png)
In job2 it will check for the mnistds.py file commited by the developer if it exists then it will launch the docker container and is and is mounted to the host OS as the updations and files created by the docker are stored permanently by giving privilege to the container so that we can overcommit memory .we can use any name to identify the container as container id's are difficult to remember I have appended the $BUILD_NUMBER to the docker container name so that it will always be unique and we wont encounter any trouble while running the container as this is the common issue we encounter and we run our python file which loads data and creates predictor and predicted files using docker exec command.
![image](https://user-images.githubusercontent.com/61894395/83335033-c5dce080-a2c7-11ea-854c-1e7d25c3e758.png)
when we launch the the container to execute mnistds.py program file it will execute the program file and start traing the model and the build no is stored into a buildno file which is pushed directly into the github so that we can use this buildno to acess the output file of the current build in the downstream job as the accuracy is shown here.
![image](https://user-images.githubusercontent.com/61894395/83335070-e442dc00-a2c7-11ea-834c-63b0eb874d28.png)
also provided the github credentials so that i can directly push my updated file to the github directly from the current job itself.
![image](https://user-images.githubusercontent.com/61894395/83335096-fb81c980-a2c7-11ea-8187-be46e41cc53e.png)
The output will be like this after all the epochs are successful you get your metrics value and at the last you can commit your buildno.
![image](https://user-images.githubusercontent.com/61894395/83335114-17856b00-a2c8-11ea-8fc0-904ced21f5f2.png)
![image](https://user-images.githubusercontent.com/61894395/83335125-2a983b00-a2c8-11ea-81ed-41f46d1cb18e.png)
# Job 3
In job 3 it will check for the accuracy of the model and it executes / performs the respective action
![image](https://user-images.githubusercontent.com/61894395/83335142-46034600-a2c8-11ea-9833-ee5713a9c1f9.png)
here the buildno which we have stored from the previous build is stored into a variable which will be replaced in the url of the job 2 from it we grep the accuracy value and we check whether the accuracy is greater than 80 or not if it is 80 the model will be ready for prediction or else we append a add.txt file which consists of the convolution layer along with activation function relu and 'pooling layer' which will be appended to the mnistds.py file and pushed back to the github if the developer want to add any other layers if he thinks it is required he can just add it to the add.txt fill and push it it will automatically appended to the training file and the job1 is triggered where it again copies the new modified file from github and starts the loading and training process without any human intervention and the process continues until the acuracy condition is met.

If your model achives the accuracy more than 80% accuracy you can predict the outputs in my task i have written the code for Classifying Handwritten Digits.
![image](https://user-images.githubusercontent.com/61894395/83335156-629f7e00-a2c8-11ea-9628-7ba092fe045b.png)
![image](https://user-images.githubusercontent.com/61894395/83335174-78ad3e80-a2c8-11ea-84d4-7a1304878e81.png)
# Job 4
Job 4 monitors job 2 whenever the job 2 fails that is if traing part fails it will automatically triggers the job again and sends an email email notification to the developer.
![image](https://user-images.githubusercontent.com/61894395/83335199-967aa380-a2c8-11ea-80aa-4b110ef34b22.png)
![image](https://user-images.githubusercontent.com/61894395/83335206-ae522780-a2c8-11ea-9fa6-fbfe5c840ee7.png)
for the email notification we need we need to configure it in the jenkins configure system settings
![image](https://user-images.githubusercontent.com/61894395/83335216-c5911500-a2c8-11ea-9474-4431aa0a2564.png)
![image](https://user-images.githubusercontent.com/61894395/83335224-dc376c00-a2c8-11ea-9a54-1810c6253a3e.png)
![image](https://user-images.githubusercontent.com/61894395/83335230-ece7e200-a2c8-11ea-8bd8-5160ac7196e1.png)
This is the Build Pipeline if all the jobs are successfully and also remember that the monitoring job will run only if the job2 ie training job fails.
![image](https://user-images.githubusercontent.com/61894395/83335239-08eb8380-a2c9-11ea-9805-250cbd84cb96.png)
our mentor vimal daga search him on google 
