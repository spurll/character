Character Creator
=================

Rolls random characters for use in fiction.

Considerations and Caveats
==========================

There are obviously story reasons you might want a character to have some characteristics.
But for characters you're just throwing in, it's really easy to just "default" to whatever
your biases are. Instead, consider doing something different.

The starting point for these sliders represent some real-world demographics—but given how
poor representation is in fiction today, there's a good argument for overrepresenting some
previously underrepresented demographics.

This was made by a straight, white, cis dude. It's very likely that I've made some
mistakes or omissions. I'm happy to take critiques and suggestions. The code is also open
source and permissively licensed, so anyone is welcome to fork it and make it better!

Obviously there are all sorts of other vectors (what word am I looking for here?) that can
and should be represented in your world. This is just a starting place.

Implementation Plan
===================

Ethnicity, gender (incl nonbinary/trans), sexuality (including ace), ability/disability

Allow people to set their own sliders

Include some defaults for a few parts of the world (drop down).

Option to include character quirks (likes/hates/is scared of/fascinated by/uncomfortable
with... at different percentages then random noun)

Link to stats about X% of speaking roles going to men, X% to white people (source from
Geena Davis Institute on Gender in Media)

You’ll have to demographic fetch data from multiple sources. (Cache it, don’t do live searches.)
`http://api.census.gov/data/2010/sf1?key=15f9866ef28f579a44b17c1b4f0e46bbb177b382&get=P0010001,NAME&for=state:*`
`http://www.census.gov/developers/`
`http://www.opengeocode.org/tutorials/USCensusAPI.php`

Usage
=====

Installation
------------

TODO

Requirements
------------

TODO

* flask
* flask-wtf

Configuration
-------------

Edit `config.py`.

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To
make the server world-accessible or for other options, see `run.py -h`.

If you're having trouble configuring your sever, I wrote a
[blog post](http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html)
explaining how you can get Flask, uWSGI, and Nginx working together.

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

None

Thanks
======

This work was inspired by the Centring Women in Fiction panel from
[NerdCon: Stories 2016](http://nerdconstories.com). Special thanks to Eileen Cook, Liz
Hara, Rachel Kann, Alyssa Wong, Nalo Hopkinson, Mikki Kendall, Saladin Ahmed, and everyone
else who participated in interesting, thoughtful discussions at NerdCon.

Thanks also to [Aanand Prasad](https://twitter.com/aanand), whose
[Diversity Calculator](http://aanandprasad.com/diversity-calculator/) was also an
inspiration.

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under the [MIT "Expat" License](https://opensource.org/licenses/MIT).

Remember: [GitHub is not my CV](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/).
