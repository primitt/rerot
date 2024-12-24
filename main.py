from flask import Flask, request, jsonify, render_template
from together import Together
import json
from dotenv import load_dotenv
import os

load_dotenv()

read_brainrot = open("brainrot.json", "r").read()
together = Together(api_key=os.getenv("together_key"))
prompt = """
TOday you are acting like a brainrot translator. I am giving you a sentence in English, and you have to tranlate it to brainrot terms.

I will also provide you a large dictionary in JSON format of a ton of brianrot terms and their definitions for your convinience. Now I will provide you the sentence to translate.
ONLY respond with the translated sentence. Do not provide any other justification. Do not write "The translated sentence is" or anything like that. Just the translated sentence, thats IT. Additionally, do not put quotes around the sentences.
Additionally, add some text slang in there too like "u" instead of "you" or "lol" for laugh out loud.
Remeber, if a question is given, do not translate it, just respond with the question, but in brainrot terms, and remember to keep the punchuation.
"""

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/api/rerot", methods=["GET"])
def rerot():
    text = request.args.get("text")
    if not text:
        return jsonify({"error": "No text provided."})
    else:
        print(read_brainrot)
        resp = together.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages = [
            {"role":"assistant", "content":prompt},
            {"role":"assistant", "content":read_brainrot},
            {"role":"user", "content":"Translate this into brainrot, the user wrote: " + text}
        ]
        )
        final_resp = resp.choices[0].message.content
        return jsonify({"data": final_resp})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010)
