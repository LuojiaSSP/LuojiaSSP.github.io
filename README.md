# SSP website 


SSP website.

The website is use [pelican](https://docs.getpelican.com/en/latest/index.html) to generate. More information about pelican can be found [here](https://docs.getpelican.com/en/latest/index.html).


## How to Use

    1. Clone the repository
    2. Make changes locally
    3. Setup pelican and use it generate the website
    4. Check the website works fine locally
    5. Push the changes to Github
    6. Visit the website at [LuojiaSSP.github.io](luojiassp.github.io)

### Clone the repository

    ```bash
    git clone https://github.com/LuojiaSSP/LuojiaSSP.github.io.git
    ```
### Make changes locally, generate the website and push the changes to Github

    ```bash
    cd LuojiaSSP.github.io
    ```
    1. Edit the the files in the `content` folder
    2. Run `pelican -s pelicanconf.py -o ./docs` to generate the website
    3. Run `pelican --listen -o ./docs` to start the web server locally to preview the website
    4. Run `git add *` to add all the changes
    5. Run `git commit -m "your comment"` to commit the changes
    6. Run `git push origin master` to push the changes to Github

### Visit the website

Visit the website at [LuojiaSSP.github.io](luojiassp.github.io)
    
