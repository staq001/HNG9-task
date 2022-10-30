from django.shortcuts import render
from django.http.response import HttpResponse
import json

class Bio:
    def __init__(self, slackusername, bio, age):
        self.slackusername = slackusername
        self.bio = bio
        self.age = age
        self.backend = True

    def __str__(self):
        return f"slackUsername: {self.slackusername}, backend: {self.backend}, age: {self.age}, bio: { self.bio}"

    def jsonify(self):
        x = {'slackUsername': self.slackusername, "backend": self.backend, "age": int(self.age), "bio": self.bio}
        return json.dumps(x)


test = Bio('Staq_', "I'm a calm and intelligent person, i wish to enjoy my time here.", 23)
# print(test.jsonify())

def app(request):
    string = test.jsonify()
    return HttpResponse(string)
