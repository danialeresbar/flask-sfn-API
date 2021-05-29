# Science Fiction Novel API

This section will show you how to build a prototype API using Python and 
the Flask web framework. Our example API will take the form of a distant 
reading archive—a book catalog that goes beyond standard bibliographic 
information to include data of interest to those working on digital projects. 
In this case, besides title and date of publication, our API will also serve 
the first sentence of each book. This should be enough data to allow us 
to envision some potential research questions without overwhelming us as we focus 
on the design of our API.

We’ll begin by using Flask to create a home page for our site. In this step, 
we’ll learn the basics of how Flask works and make sure our software is configured 
correctly. Once we have a small Flask application working in the form of a home page, 
we’ll iterate on this site, turning it into a functioning API.

## Flask

Flask is a lightweight WSGI web application framework. It is designed to make 
getting started quick and easy, with the ability to scale up to complex applications. 
It began as a simple wrapper around Werkzeug and Jinja and has become one of the most 
popular Python web application frameworks.

Flask offers suggestions, but doesn’t enforce any dependencies or project layout. 
It is up to the developer to choose the tools and libraries they want to use. 
There are many extensions provided by the community that make adding new 
functionality easy.

![logo](https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png)
