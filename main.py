from flask import Flask, render_template, request, redirect
from google.cloud import datastore

import logging

app = Flask(__name__)


@app.route("/")
def home():
     return render_template("home.html",author = " ")


@app.route("/discuss",methods=['GET'])
def discuss():
     return render_template("discuss.html")

@app.route("/submit")
def submit():
     name = request.args.get("name")
     email = request.args.get("email")
     topic = request.args.get("topic")
     message = request.args.get("message")
     if ( len(name) == 0 and len(email) == 0  and len(topic) == 0 ):
            app.logger.info("message is epty")

     else:     
           datastore_client = datastore.Client([PROJECT-ID-GOESHERE])
           key = datastore_client.key('Topic')
           q_entity = datastore.Entity(key=key)
           q_entity["name"]=name
           q_entity["email"]=email
           q_entity["topic"]=topic
           q_entity["topicDescription"]=message
           datastore_client.put(q_entity)
           app.logger.info("name: " + name+" email: " + email + " topic: " + topic)
     return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)
