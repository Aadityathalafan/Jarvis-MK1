import webbrowser
import difflib

def open_website_name(website_name):
    website = {
    "google" : "https://www.google.com",
    "youtube" : "https://www.youtube.com",
    "instagram" : "https://www.instagram.com",
    "facebook" : "https://www.facebook.com",
    "twitter" : "https://www.twitter.com",
    "linkedin" : "https://www.linkedin.com",
    "wikipedia" : "https://www.wikipedia.org",
    "reddit" : "https://www.reddit.com",
    "amazon" : "https://www.amazon.com",
    "ebay" : "https://www.ebay.com",
    "netflix" : "https://www.netflix.com",
    "apple" : "https://www.apple.com",
    "microsoft" : "https://www.microsoft.com",
    "quora" : "https://www.quora.com",
    "yahoo" : "https://www.yahoo.com",
    "bing" : "https://www.bing.com",
    "github" : "https://www.github.com",
    "stackoverflow" : "https://www.stackoverflow.com",
    "pinterest" : "https://www.pinterest.com",
    "dropbox" : "https://www.dropbox.com",
    "spotify" : "https://www.spotify.com",
    "soundcloud" : "https://www.soundcloud.com",
    "vimeo" : "https://www.vimeo.com",
    "tumblr" : "https://www.tumblr.com",
    "tiktok" : "https://www.tiktok.com",
    "whatsapp" : "https://www.whatsapp.com",
    "snapchat" : "https://www.snapchat.com",
    "telegram" : "https://www.telegram.org",
    "zoom" : "https://www.zoom.us",
    "skype" : "https://www.skype.com",
    "paypal" : "https://www.paypal.com",
    "airbnb" : "https://www.airbnb.com",
    "uber" : "https://www.uber.com",
    "lyft" : "https://www.lyft.com",
    "booking" : "https://www.booking.com",
    "expedia" : "https://www.expedia.com",
    "tripadvisor" : "https://www.tripadvisor.com",
    "nytimes" : "https://www.nytimes.com",
    "bbc" : "https://www.bbc.com",
    "cnn" : "https://www.cnn.com",
    "guardian" : "https://www.theguardian.com",
    "forbes" : "https://www.forbes.com",
    "businessinsider" : "https://www.businessinsider.com",
    "techcrunch" : "https://www.techcrunch.com",
    "wired" : "https://www.wired.com",
    "hackernews" : "https://news.ycombinator.com",
    "bbcnews" : "https://www.bbc.co.uk/news",
    "medium" : "https://www.medium.com",
    "blogger" : "https://www.blogger.com",
    "wordpress" : "https://www.wordpress.com",
    "flickr" : "https://www.flickr.com",
    "deviantart" : "https://www.deviantart.com",
    "etsy" : "https://www.etsy.com",
    "imgur" : "https://www.imgur.com",
    "duckduckgo" : "https://www.duckduckgo.com",
    "archive" : "https://www.archive.org",
    "shutterstock" : "https://www.shutterstock.com",
    "canva" : "https://www.canva.com",
    "adobe" : "https://www.adobe.com",
    "behance" : "https://www.behance.net",
    "dribbble" : "https://www.dribbble.com",
    "kickstarter" : "https://www.kickstarter.com",
    "patreon" : "https://www.patreon.com",
    "unsplash" : "https://www.unsplash.com",
    "pixabay" : "https://www.pixabay.com",
    "flipkart" : "https://www.flipkart.com",
    "aliexpress" : "https://www.aliexpress.com",
    "bestbuy" : "https://www.bestbuy.com",
    "walmart" : "https://www.walmart.com",
    "target" : "https://www.target.com",
    "costco" : "https://www.costco.com",
    "ikea" : "https://www.ikea.com",
    "homedepot" : "https://www.homedepot.com",
    "lowes" : "https://www.lowes.com",
    "wayfair" : "https://www.wayfair.com",
    "kohls" : "https://www.kohls.com",
    "overstock" : "https://www.overstock.com",
    "zillow" : "https://www.zillow.com",
    "realtor" : "https://www.realtor.com",
    "indeed" : "https://www.indeed.com",
    "glassdoor" : "https://www.glassdoor.com",
    "monster" : "https://www.monster.com",
    "craigslist" : "https://www.craigslist.org",
    "freelancer" : "https://www.freelancer.com",
    "upwork" : "https://www.upwork.com",
    "fiverr" : "https://www.fiverr.com",
    "udemy" : "https://www.udemy.com",
    "coursera" : "https://www.coursera.org",
    "khanacademy" : "https://www.khanacademy.org",
    "edx" : "https://www.edx.org",
    "skillshare" : "https://www.skillshare.com",
    "pluralsight" : "https://www.pluralsight.com",
    "zoominfo" : "https://www.zoominfo.com",
    "salesforce" : "https://www.salesforce.com",
    "sap" : "https://www.sap.com",
    "oracle" : "https://www.oracle.com",
    "ibm" : "https://www.ibm.com",
    "hp" : "https://www.hp.com",
    "dell" : "https://www.dell.com",
    "lenovo" : "https://www.lenovo.com",
    "asus" : "https://www.asus.com",
    "acer" : "https://www.acer.com"
    }

    website_name_lower = website_name.lower()


    if website_name_lower in website:
        url = website[website_name_lower]
        webbrowser.open(url)
        print(f"opening : {website_name}...")

    else:
        matches = difflib.get_close_matches(website_name_lower, website.keys(), n=1, cutoff=0.6)
        if matches:
            closest_match = matches[0]
            url = website[closest_match]
            webbrowser.open(url)

            print(f"opening the closest match {closest_match} at {url}")

        else:
            print(f"Sorry, I don't have information about the website : {website_name}")

while True:
    user_input = input("please write the name of website : ")
    open_website_name(user_input)