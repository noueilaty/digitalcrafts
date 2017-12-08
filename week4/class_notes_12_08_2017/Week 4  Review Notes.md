**Topics:**

* Github README.md file (markdown language)  
* Amazon AWS  
* Heroku Account: Install heroku CLI  
* Git Branches  
* Review  
* **Quiz!**

### **Git Branches:**

**Working with one branch:**

-*Master branch*: created by default. Any code changes made will write to the master branch.

 Git init: initalizes the respository and creates the master branch.

-Branch: is where the code is currently living.

\*Problem: if you are commiting to one branch, you’re creating a liability that you could hold others back from a completed product.

**Working with multiple branches:**

Each user has their own branch, and can work independently of eachother on their own portions of the codebase. Once a user completes their code branch, they can push their code to the master branch.

If one of the develoeprs is not ready to merge to the master branch

\*Merge conflicts: overwriting code

### **Amazon AWS:**

To deploy a static website:

1. Launch the AWS Console
2. Host a static website
3. Select the ‘Your website’ option
4. Compress (Zip) the host folder on your computer, then drag and drop the zip file.
5. You’re done!

\*Anytime you make a change, zip it up and upload to AWS again.

Amazon generates a dynamic URL for you to reference. You have the option to purchase or setup with your own domain.

To delete the website, search for ‘bucket’ from the AWS Console. Then delete the files associated with your website.

### **Heroku: ***(5 free apps on included)*

Built on Ruby on Rails

Refer to URL for detailed instructions:

<http://blog.teamtreehouse.com/deploy-static-site-heroku>

1. Ensure you’ve downloaded Heroku CLI (Can use brew to do so).
2. Initialize the files using git (via terminal)
3. Commit the files locally.
4. Push master branch to Heroku

```js
heroku apps:/create my-website
```

### **Git README.md:**

**
**

Create a **README.md** file (markdown). Markdown is it’s own language.

Markdown Cheatsheet:

<https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>

Mac Screenshots:

<https://support.apple.com/en-us/HT201361>

Include:

* Title
* Description
* Screenshots
* Link to YouTube demonstration
