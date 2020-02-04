import requests

# make 200 requests to the server
output = open("output.txt", "a+")
old_code_response = "Hello World. <br/>This is Kofi's Udacity Devops-nanodegree capstone project"
new_code_response = "This is Kofi's Udacity Devops-nanodegree capstone project"
response_texts = []
for i in range(600):
    response = requests.get("http://a36edb92e478d11eab27f065643d7386-1589614578.eu-west-2.elb.amazonaws.com")
    if response.text == old_code_response:
        response_texts.append("OUTDATED pod response: " + response.text)
    if response.text == new_code_response:
        response_texts.append("UPDATED pod response: " + response.text)
    response_texts.append("\n\n")
output.writelines(response_texts)
output.close()
