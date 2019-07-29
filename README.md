Welcome to Feed 2 Write.as!
======================================

This is a Glitch app that will allow you to turn any RSS feed into a list on a Write.as post that updates automatically! (_Source_: https://glitch.com/~feed-2-writeas)

To see an example of this app in action, click [here](https://imminent-antimatter.glitch.me/xml).

Getting Started
-------
- First remix this app!
- Then, in your Write.as blog, create a new post for your feed! Fill the body in with whatever. For example, make one titled 'What I am Reading'.
- Come back to the app. In stuff.py, add the following values where listed:
    1) feed: the RSS feed url (ex. https://getpocket.com/users/me/feed/all)
    
    2) alias: the collection alias for your Write.as blog (ex. for https://write.as/matt, the alias is 'matt')
    
    3) slug: the slug that identifies the post that will host the feed. So, if my post was https://blog.cjeller.site/what-i-am-reading, the slug is 'what-i-am-reading'.
    
    4) intro: the text that will be above the list - something that describes what the links are about (ex. 'Here is what I am currently reading on the web: ')

- Finally we need to add the Write.as authentication token. This way the post will update through your account. We will do this by logging in thru curl!
- So open up a terminal and copy the below in. Make sure to replace the username and password with your own:

```
curl "https://write.as/api/auth/login" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{"alias": "me", "pass": "12345"}'

```
- If successful, you should receive a 200 response and see a 'token' in there with a crazy long value. Copy that value and bring it into the app, pasting it in the .env file as the value for TOKEN. (Make sure to put it between quotations w/o spaces -> TOKEN="12345")


THE MOMENT OF TRUTH!!!
----------------------
- Open up the app in another window and go to the '/xml' route (ex. https://feed-2-writeas.glitch.me/xml). It should redirect you to the Write.as post, now with a list of links from your RSS feed!

THE (SECOND) MOMENT OF TRUTH!!!
----------------------
- Try to update your RSS feed, add something in Pocket or whatever, and them try the above route again. It should register the changes and update the post!

- Congrats! Now we want to place the app on our blog...

Putting the app on your Write.as Blog
----------------------
- First pin the Write.as post! That way it is in the header under your title.
- Go to Customize settings of your blog and go to 'Custom Javascript'.
- Put the following code there. Replace with your official blog url and app url:

```
var a = document.querySelector('a[href="https://blog.cjeller.site/what-i-am-reading"]');
if (a) {
  a.setAttribute('href', 'https://feed-2-writeas.glitch.me/xml');
}
```
- Save and check to see if it redirects to your feed post!

A Remix of [@dschep](https://glitch.com/@dschep) 's [Python3](https://glitch.com/~python3)
----------------------


