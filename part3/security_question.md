# Security audit of the app's infrastructure

In first place, it is important to notice that the OWASP is an open project that has many tools and programs
for developing and mantaining safe and confiable applications and APIs. So, in this way, I will use  the  OWASP top 10 guide of 2021 for developing this security audit. 

In this manner, I will start by reviewing the security risks I consider are the most important for the infrastucture of the solar panel installation app:

- **Risk # 1: Injection**. For avoiding SQL injection (As the main database is built in mySQL) it is important to review the Python code implemented in FastAPI. Software engineers should have done preventive actions such as using ORM libraries to prevent injection.

- **Risk # 2: Broken Access Control**. This is one of the most dangerous, specially for web applications (taking into account that the app has also a web frontend) because customer and application data may be accessed without autorization. Thus what is necessary to be done is audit access controls and permissions (specially for accessing to customer data) and stablish proper access roles for developers, customers and customer service.

- **Risk #3: Sensitive Data Exposure**. For avoiding this risk, developers have to ensure that during the transit of data HTTPS is used. Also, it is important to regularly review that encription keys are managed securely.

- **Risk #4: Security Misconfiguration**. It is a common mistake that the configurations of Kubernetes cluster are not reviewed and updated regularly, so developers should do this and also use good practices (such as AWS best practices and the principle of least privilege for granting access).

- **Risk #5: Failures in authentication and identification**. This is a classic one, because it has the human factor involved making it one of the most used for security breaches. In one hand, it is important to assure that the customers and users have strong passwords. But in the other, it is necessary to implement MFA (Multi-factor Authentication) in all users accounts and also ensure that sessions have a timeout defined, in order to be managed securely. This last point is specially important in the mobile application, because it may be ignored and create a potential security risk. In my experience it is sometimes forgotten or ignored, so it is important that the developers realise of this aspect.

- **Risk #6: Deprecated and vulnerable components**. It is usual that in web and mobile development 'external components' are used to have special functionalities or certain services that are essential for the correct lifecycle of the application. However, good practices like updating components and libraries and implement vulnerability management processes may avoid this risk to convert into serious security problems (like zero days exploits).




-**

