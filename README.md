
 
# 1	Introduction
The study examines cloud-based technology as a potential remedy for small and medium-sized organizations.\
The three primary cloud-based solution platforms are Microsoft Azure, Docker, and GitHub. On all of the above-mentioned platforms, we pushed the web application's code in the form of images which we developed for the Network Critical Solutions company, the recommendation and method are reflected in this document.


# 2	Enterprise background
Network Critical has dominated the computer networking sector since its founding in 1997. With offices now located in the Americas, Europe, and the Middle East, they continue to create and develop the best hardware (Network TAPs and Packet Brokers) and software (Drag-n-VuTM) while working with their reputable technology partners. All of their goods are designed, developed, and produced by our skilled engineering and technical teams. 
Since their products enable businesses of all sizes to securely link essential network monitoring, security, and performance tools, they have gained the respect of significant corporations worldwide for their ability to provide traffic visibility for business, carrier, and governmental networks.

# 3	Current IT Setup
The organization has a variety of IT systems, with its website playing a key role. The business also engages in digital marketing to advertise its goods and services. The organization may serve a wider group of customers with the aid of digital marketing strategies because Internet usage is growing rapidly. As the business interacts with more customers, the data is put to use. The information can be used for a variety of things, especially for the company's effective strategy. Companies may discover their strong and weak spots with the aid of data analysis, which is useful for locating target customers. The business is connected to Java script for the creation of the website's backend. 
The business can link the software with cutting-edge technology to enable a variety of possibilities in the form of API. The business is currently connected to numerous APIs. All functionalities can be carried out with a single piece of code with the integration of Django or Flask (GeeksforGeeks 2020). The performance and longevity of the website increase as the code length lowers.

# 4	Deployment Procedure
## Directory structure for the application:
The directory structure should be set up in accordance with the given image, which contains the source code and all necessary files as well as the Docker file to construct and containerize the image.
 ![image](https://github.com/thathired/netwporkCloud/assets/133872215/72baf20e-ac5b-486b-8ad5-120011ac7a41)

Docker image creation is required in order to containerize the application. The docker commands are displayed in the image below.
After the image has been created, we can examine the local images. 

In order to launch the web application using the Docker desktop, the image is also uploaded to Docker Hub.
![image](https://github.com/thathired/netwporkCloud/assets/133872215/583a7b61-b888-401d-944f-e5bf77576a46)

## Uploading a container to Azure:
This is how the picture is uploaded to Azure:\
• Utilize the resource group to create the Azure container registry.\
• Add a tag to the Azure Container Registry for the Docker image.\
• Open the Azure Container Registry and log in.\
• Upload the image to the registry for Azure containers.
 
The produced Docker image is now submitted to the GitHub registry using the following procedures:\
• Add a GitHub registry tag to the docker image.\
• As seen in the below image, push the Docker image to GitHub.\
• Use the GitHub portal to confirm the image that was pushed into GitHub.
![image](https://github.com/thathired/netwporkCloud/assets/133872215/1fa2c330-b56a-4c4f-bfb6-47db30db3ee9)

 
 
## Run/test the program:
Run the application on the server using a local or docker image, azure or GitHub-pulled image, etc.
![image](https://github.com/thathired/netwporkCloud/assets/133872215/e0e74388-9714-42f4-bce0-457b4ff1b5ff)
![image](https://github.com/thathired/netwporkCloud/assets/133872215/4fe8f600-799f-44e1-a42f-5ea3d9d1706c)


# 5	Recommendations
## 5.1	Cloud vs non-cloud solutions
It is advised that the business implement cloud solutions because:\
•	Cloud solutions helps in installing software on a remote server, hosting those apps there, or storing data in a remote database.\
•	 With the help of the cloud, we may scale up or down apps in accordance with our needs to save costs and maintain speed.\
•	 Anyone can access the remote server using the cloud, reducing their reliance on the on-premise infrastructure.\
•	Pay-as-you-go cloud computing solutions only charge us for the resources or services we actually use and for the time we utilize them. The cost of setting up the infrastructure is not billed to us.\
•	Using cloud services requires routinely patching and maintaining software updates for both underlying infrastructure and applications. This lessens the workload for IT teams.\
•	Cloud solutions keep up with infrastructure needs including hardware upgrades, security patches, and fault tolerance.\
•	Quick provisioning and application deployment provided by cloud solutions shorten enterprises' time-to-market.
## 5.2	Appropriate deployment types and service level
For deploying the cloud resources or services we needed.\
•	Docker instance\
•	Docker Container\
•	GitHub Container Registry\
•	Containerization of the application\
•	Updating the application.\
•	Multi-Container Apps
## Services/Resources used:
•	Azure Active registry\
•	GitHub Registry\
•	Docker Desktop\
•	Python/HTML/CSS/JS
## 5.3	Justification for Recommendation
The deployment and hosting of applications on the on-premise infrastructure are essentially what traditional on-premise infrastructure, also referred to as non-Cloud solutions, entails. We are unable to adjust our capacity in response to changes in demand. We are not given the freedom to view the servers remotely. Additionally, the startup costs for the infrastructure are very significant. Although somewhat automated, resource and service deployment take longer than usual.
Given all these factors, moving from an on-premises environment to a cloud environment is necessary for an organization that needs scalability, lower infrastructure costs, and remote access to resources. This involves moving the on-premise system to the cloud resources and using containerization to host the application on a remote server or by using a virtual machine on the cloud server.

# 6	Conclusion
The report covers the successful implementation of the Network critical Solutions Web application, which is useful for a variety of purposes such as enhanced data storage, data security, and efficient code processing. It also contains recommendations for both cloud and non-cloud solutions.


# 7	References
Network Critical Solutions. Available at: https://www.networkcritical.com [Accessed 12 Jul. 2023].
Docker. (2022). Docker: Accelerated, Containerized Application Development. [online] Available at: https://www.docker.com/ [Accessed 12 Jul. 2023].
GeeksforGeeks. (2020). Differences Between Django vs Flask. [online] Available at: https://www.geeksforgeeks.org/differences-between-django-vs-flask/ [Accessed 12 Jul. 2023].
Microsoft.com. (2023). Global Infrastructure. Microsoft Azure. [online] Available at: https://azure.microsoft.com/en-us/explore/global-infrastructure [Accessed 12 Jul. 2023].


