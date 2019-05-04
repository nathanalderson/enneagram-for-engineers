The Enneagram For Engineers
===========================

This project contains slide for my conference talk on the Enneagram for Engineers.

The presentation is built with impress.js_. The main presentation is in `templates/index.html`_.

To run the presentation, you'll need python and flask_. The easiest way is to install python and then
create a virtual environment::

    virtualenv venv
    source venv/bin/activate
    pip install flask

Then start the presentation with::

    FLASK_APP=app.py flask run

Now open a browser to http://localhost:5000/.

.. _impress.js: https://github.com/impress/impress.js
.. _templates/index.html: templates/index.html
.. _flask: http://flask.pocoo.org/

Resources
=========

If you're just interested in the resources mentioned in the talk, those are replicated here for
easier reference:

* Ian Cron and Suzanne Stabile
    - *The Liturgists Podcast* `episode 37`_
    - *The Road Back To You* (website_) (podcast_) (book_)
    - `Typology Podcast`_
* enneagraminstitute.com_
* Sarajane Case
    - `Enneagram and Coffee Podcast`_
    - `Club Enneagram`_
* Enneagram Tests
    - `Eclectic Energies`_ (free)
    - `Enneagram Institute`_ ($12)
    - `Ian Cron`_ ($60/$120)

.. _episode 37: http://www.theliturgists.com/podcast/2016/8/23/the-enneagram-episode-37
.. _website: https://www.theroadbacktoyou.com/
.. _podcast: https://www.theroadbacktoyou.com/podcast
.. _book: https://www.goodreads.com/book/show/28268515-the-road-back-to-you
.. _Typology Podcast: https://www.typologypodcast.com/
.. _ennagraminstitued.com: https://www.enneagraminstitute.com/
.. _Enneagram and Coffee Podcast: https://enneagramandcoffee.libsyn.com/
.. _Club Enneagram: https://sarajane-case.mykajabi.com/club-enneagram
.. _Eclectic Energies: https://www.eclecticenergies.com/enneagram/test
.. _Eneagram Institute: https://tests.enneagraminstitute.com/
.. _Ian Cron: https://ianmorgancron.com/assessment#row--58717
