# CMA Development

## Back-end

To get the JSON file we need for the app, you first need to clone this repository. You must, understandably, also have Python installed on your computer. When this is done, make your way to the project directory via your terminal and run `backend.py`. This will create the desired JSON file in the same directory.

## Front-end

For the front end, I used Flask. Please follow the the installation directions outlined here to install Flask _from within the current directory_: https://flask.palletsprojects.com/en/2.1.x/installation/ (Obviously, we already have a project directory, so we don't need to create a new one as it says to under **Create an environment**).

To run the app locally, please set `FLASK_APP` to `main` (this is `export FLASK_APP=main` on Mac and Linux, `set FLASK_APP=main` on Windows). Then type in `flask run` (if this does not work, type in `python -m flask run`).

Now that that is running, open your browser and go to http://127.0.0.1:5000/. You should see the app!

## Resources
- As already indicated, I used the Flask web framework: https://flask.palletsprojects.com/en/2.1.x/
- I used Atom as my IDE: https://atom.io/
- I didn't have experience with .db files, so I needed to familiarize myself with those: https://www.tutorialspoint.com/sqlite/sqlite_python.htm, https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
- I also needed to figure out how to put all my work into JSON representation: https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
- My experience with front-end development is not as fleshed out as my back-end, so I furthermore referenced a tutorial to understand how to use Flask in conjunction with HTML and CSS: https://www.youtube.com/watch?v=MwZwr5Tvyxo

## Reflection
To set everything up (downloading Python, downloading Atom, etc.) and to familiarize myself with Windows Terminal commands (I'm used to Unix) took me anywhere from about 30 minutes-1 hour. Not including the set up time, I think coding the back-end took me right around 4 hours. I had to first take the time to figure out what SQLite was and how .db files worked and how to extract data from them. Once I did that, the bulk of my time was spent collecting and organizing that data (Once I thought I got it, I realized there could be several artists on a piece of art, and after I thought I got it again I noticed the issue of the same artist being listed many times over).

The more difficult part was the front-end. I must have spent a couple of hours just reading documentation/watching tutorials. The actual HTML (and to a lesser extent the CSS) coding took me around 4 hours as well. Though the code is not very long, I was not yet well adjusted and it took some time to fix the (many!) syntactical issues to get my code working.

Coding wise, this test took me about 8 hours to complete. Factoring set up and research, around 11-12.
