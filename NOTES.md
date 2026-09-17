***What is MVT?***

- Models are the blueprint for database tables, they contain the characteristics of the data that is being stored in the database. Like the character count or whether a field is unique.
- View receives requests from the browser and processes the request according to what the logic is then sends back a response.
- Template defines the structure of how the webpage will be rendering information to the user viewing it.

***What is a migration, and why don't we edit the database by hand?***

A Migration consists of the changes that need to be made in a database that were defined in the models. Migrations are an easy way of making changes to the database structure. The reason migrations are used over editing the database by hand, is because it reduces the risk of data loss and it allows for all the changes to be tracked clearly in the code which is visible to anyone with access to it.

***What is the difference between a Django view and a template?***

A View layer manages application logic, it handles requests and processes what responses should be returned to the user. The Template just structures the way the information is going to be displayed to the user, that could be coming from data passed by the view or hardcoded elements in the template.

***What does “deploying” mean, and why did we use Git to do it?***

Deploying means getting code for a project that has been built and running it on a live server so it can be accessed from the internet by other users.
Git allows us to have the exact same commit history the code had when it was being built. So the server does not miss out on any file, if changes are made later on and pushed to github, the only thing needed is a 'git pull' from the server for the live code to be updated.