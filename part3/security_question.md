# Security audit of the app's infrastructure

First of all, it is important to note that the OWASP is an open project that provides numerous tools and programs
for developing and mantaining safe and confiable applications and APIs. So, in this way, I will use  the  OWASP top 10 guide of 2021 for conducting this security audit. 

In this context, I will start by reviewing the security risks I consider are the most critical for the infrastucture of the solar panel installation app:

- **Risk # 1: Injection**. For avoiding SQL injection (As the main database is built in mySQL) it is important to review the Python code implemented in FastAPI. Software engineers should have done preventive actions such as using ORM libraries to prevent injection.

- **Risk # 2: Broken Access Control**. This is one of the most dangerous, particularly for web applications (taking into account that the app has also a web frontend) because customer and application data may be accessed without autorization. Thus what is necessary to be done is audit access controls and permissions (specially for accessing to customer data) and stablish proper access roles for developers, customers and customer service.

- **Risk #3: Sensitive Data Exposure**. To mitigate this risk, developers must ensure that data is transmitted using HTTPS. Also, it is important to regularly review that encription keys are managed securely.

- **Risk #4: Security Misconfiguration**. It is a common mistake that the configurations of Kubernetes cluster are not reviewed and updated regularly (they are usually overlooked). So developers should address this issue and also use good practices (such as AWS best practices and the principle of least privilege for granting access).

- **Risk #5: Failures in authentication and identification**. This is a classic one, as it involves the human factor making it a common avenue for security breaches. In one hand, it is important to assure that the customers and users have strong passwords. But in the other hand, it is necessary to implement MFA (Multi-factor Authentication) in all users accounts and also ensure that sessions have a timeout defined, in order to be managed securely. This last point is specially important in the mobile application, because it may be overlooked and create a potential security risk. In my experience it is sometimes forgotten or ignored, so it is important that the developers realise of this aspect.

- **Risk #6: Deprecated and vulnerable components**. It is usual that in web and mobile development 'external components' are used to have special functionalities or certain services that are essential for the correct lifecycle of the application. However, good practices like updating components and libraries and implement vulnerability management processes may avoid this risk to convert into severe security problems (like zero days exploits).


Finally, the most significant concern for me is **Failures in logging and monitoring**. Even though the team involved in the application is not very large, they hold significant responsabilities for customer data and privacy. Therefore, regular activities such as code reviews, penetration testing and others security assesaments need to be done regularly in order to keep the integrity of the data and the application. In the same way, it is also crucial to define a clear security strategy, particularly for managing security incidents and suspicious activities. The human layer remains the most vulnerable and, therefore, the most important.

