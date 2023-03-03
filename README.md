# SSP website



The [website](https://luojiassp.github.io/) is use [pelican](https://docs.getpelican.com/en/latest/index.html) to generate. More information about pelican can be found [here](https://docs.getpelican.com/en/latest/index.html).


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

### Install requirements

packages in requirements.txt, expecially those as follow

```bash
pip install pelican # for generate the website
pip install pelican-sitemap # for sitemap
pip install pelican-seo # for seo
pip install invoke
pip install markdown
```


### Make changes locally, generate the website and push the changes to Github

```bash
cd LuojiaSSP.github.io
```
 1. Edit the the files in the `content` folder. The menu of the website is located in the `pages` folder. The folder `researches` contains the research projects. The folder `publications` contains the publications. The folder `people` contains the people. 
 2. Run ` pelican content -s pelicanconf.py -t ./themes/notmyidea/ -o ./docs --autoreload` to generate the website
 3. Run `pelican --listen -o ./docs -r` to start the web server locally to preview the website
 4. 2 and 3 can be run in one command `pelican content -s pelicanconf.py -t ./themes/notmyidea/ -o ./docs --autoreload --listen`, which is a better choice
 5. Run `git add *` to add all the changes
 6. Run `git commit -m "your comment"` to commit the changes
 7. Run `git push origin master` to push the changes to Github

if you want to add sharing button to your past add the following code to your posts,

```html
<!-- Add following div tag where you want show soopr share buttons -->
<div class='soopr-btn'></div>
<!-- Just before body tag add this line -->
<script async defer data-soopr-token='pt_f8843b680c3f1f259cbdc907a190d4f6' src='https://sdk.soopr.co/soopr.js'></script>
```

❗️if you want to create your website using my template please use your own [soopr account](https://www.soopr.co/) to generate the code above. Or use any social media sharing services such as AddThis, ShareThis, or AddToAny. Choose one that you prefer and create an account on their website.

### Visit the website

Visit the website at [LuojiaSSP.github.io](luojiassp.github.io)
    
## To do list

- [x] Add research projects
- [x] add research publications
- [x] add researcher profiles
- [x] add seo
- [x] add sitemap
- [x] add google analysis


## References

1. [SSP](https://ultra.fandom.com/wiki/SSP_(Something_Search_People))
2. [Themes &mdash; Pelican 4.7.2 documentation](https://docs.getpelican.com/en/latest/themes.html)
    
<!-- 2. [Pelican＋Github博客搭建详细教程 - Heriam - 博客园](https://www.cnblogs.com/cciejh/p/blog_building.html) -->