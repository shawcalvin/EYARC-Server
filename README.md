# EYARC BYU Learning Resource App
## Getting Started
In order to run the project, first clone the repository. Ensure that you have node.js installed on your machine, then install project dependencies by running the command
~~~
npm install
~~~
Finally, run the project through the command
~~~
npm run dev
~~~

## Endpoints
|Page|Description|HTTP Type|Passed in Request|Sent As|Returned in Request|Sent As|
|----|-----------|---------|-----------------|------|-------------------|------|
|login|Log in as existing user|POST|{username, password}|JSON|{authToken}|string|
|login|Get user's name after login|GET|{authToken}|string|{name}|string|
|login|Get role ID|GET|{authToken}|string|{roleID}|int8|
|[all pages]|Logout/end session|DELETE|{authToken}|string|200|status|
|course_list|Get list of course assignments|GET|{courseID}|string|{courseAssignments}|array of simple JSON objects|
|course_list|Get assignment data for page|GET|{assignmentID}|string|{assignment}|complicated JSON object|
