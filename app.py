
# coding: utf-8

# In[1]:


from flask import Flask


# In[23]:


app = Flask(__name__)


# In[24]:


from flask import request, render_template

@app.route("/",methods = ["Get","POST"])
def index():
    if request.method == "POST":
        NPTA = float(request.form.get("NPTA"))
        TLTA = float(request.form.get("TLTA"))
        WCTA = float(request.form.get("WCTA"))
        print(NPTA, TLTA, WCTA)
        from keras.models import load_model
        model = load_model("Lesson 5 BKRNN")
        pred = model.predict([[[NPTA, TLTA, WCTA]]])
        print(pred)
        s = "The predicted bankrupcy score is" + str(pred)
        return (render_template("index.html", result = s))
    else:
        return (render_template("index.html", result = "2"))


# In[25]:


if __name__ == "__main__":
    app.run()

