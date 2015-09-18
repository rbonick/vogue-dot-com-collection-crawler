Vogue.com Collection Crawler
=======
This crawler will browse vogue.com collection slideshows and pull the urls of all the images within the slideshow.

To Use
------
* Make sure the following are installed:
    * [Python 3.4+](https://www.python.org/downloads/)
    * [Requests](http://docs.python-requests.org/en/latest/) (`pip install requests`)
    * [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) (`pip install beautifulsoup4`)
    * [ImgurPython](https://github.com/Imgur/imgurpython) (`pip install imgurpython`)
* Visit [https://api.imgur.com/oauth2/addclient](https://api.imgur.com/oauth2/addclient) and add an application.
    * Note: callback url doesn't matter.
* Update `secrets.py` with the correct values. 
* Navigate to the folder containing crawler.py via command line / terminal (**NOT python terminal**) 
* Execute `python crawler.py <url> <album name (optional)>`.
    * Note: Make sure the url is a slideshow for the collections (sample url: http://www.vogue.com/fashion-shows/spring-2016-ready-to-wear/derek-lam/slideshow/collection)

Pull requests
-------
I'm not sure that there's much work to be done on this, but if someone wants to add something I'm happy to incorporate pull requests.
