---
1. In the models file there is a classification Variable, that the column name of the leads.db, but i accidently write that name as calsification, i missed one s, and when i call that in the app file, there i use correct spelling, so i got an type error, and then i correct the misspelled in the models file, but my leads.db already created and the name of the column is clasification, so again i got an error, OperationalError(table leads has no column named classification), Then i again delete the leads.db and rerun the app file then automaticaly the leads.db create agin. Now teh column name is correctly written.

2. When i start building the n8n workflow, that time in the httprequest node i select teh post method and write the url, but it is not working and i get error everytime, because i used the n8n localy using docker, so i caahnged the url to http://host.docker.internal:8002/lead, then it work on my n8n and get the output.

3. I faced memory full issue, means out of memory, that's why i am not getting proper answer from ollama.

4. After some classification i got one more issue that, it unable to call the model from ollama, it directly go to the else part. So that time i identify the error and then i update teh system prompt, and also add a small change in the code , in the payload sectioon i add a format section to JSON. It will tell the system to give a answer in JOSN format.
---
