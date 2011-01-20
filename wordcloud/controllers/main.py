# encoding: utf-8

import re
from urllib2 import urlopen
from collections import defaultdict

from pylons import request
from pylons import tmpl_context as c

from wordcloud.lib.base import BaseController
from wordcloud.lib.base import render


SPLIT_RE = re.compile(r'[\s\(\)\[\]\/\-\'‘’,\.]+')


CLASS_NAMES = [
    u"min",
    u"low",
    u"medium",
    u"high",
    u"max",
]


class MainController(BaseController):
    """ Main controller for word cloud contest
    """
    def process(self):
        """
        Web service
        """
        # Get input text
        url = request.GET.get('text', '').decode('utf8')
        text = urlopen(url).read()

        # Split words
        words = [w for w in SPLIT_RE.split(text) if len(w) >= 4]

        # Count frequencies
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1

        # Keep 
        most_freq = sorted([(v,k) for k,v in freq.iteritems()], reverse=True)[:9]
        freq = dict([(k,v) for v,k in most_freq])

        # How many classes
        c.classes = sorted(list(set(freq.values())))
        c.nb_classes = len(c.classes)
        class_names = {}
        for i, value in enumerate(c.classes):
            class_names[value] = CLASS_NAMES[i]

        # Sort elements by freq then alpha
        elem = sorted([(v, w) for w, v in freq.iteritems()])

        # Bin the values
        bins = [[], [], [], [], []]
        for i in xrange(9):
            if i % 2 == 0:
                bins[i / 2].append(elem[i])
            else:
                if (elem[i][0] - elem[i - 1][0]) < (elem[i+1][0] - elem[i][0]):
                    bins[(i-1) / 2].append(elem[i])
                else:
                    bins[(i+1) / 2].append(elem[i])

        # Sort alphabetically
        c.sorted_words = []
        for i, bin in enumerate(bins):
            for value, word in bin:
                c.sorted_words.append((word, CLASS_NAMES[i]))
        c.sorted_words.sort()

        # Render HTML template
        return render('/wordcloud.mako')
