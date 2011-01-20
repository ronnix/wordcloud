
import re
from urllib2 import urlopen
from collections import defaultdict

from pylons import request
from pylons import tmpl_context as c

from wordcloud.lib.base import BaseController
from wordcloud.lib.base import render

SPLIT_RE = re.compile(r'\s+')

CLASS_NAMES = [
    u"min",
    u"low",
    u"medium",
    u"high",
    u"max",
]


def norm(value, min_, max_):
    """
        >>> norm(1, 1, 5)
        1
        >>> norm(3, 1, 5)
        3
        >>> norm(5, 1, 5)
        5
        >>> norm(12, 12, 42)
        1
        >>> norm(42, 12, 42)
        5
    """
    return int((value - min_) / (max_ - min_ + 1.0) * 5.0) + 1


class MainController(BaseController):
    """ Main controller for word cloud contest
    """
    def process(self):
        """
        """
        # Get input text
        url = request.GET.get('text', '').decode('utf8')
        text = urlopen(url).read()

        # Split words
        words = [w for w in SPLIT_RE.split(text) if w != ""]

        # Count frequencies
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1

        most_frequent = sorted([(v,k) for k,v in freq.iteritems()], reverse=True)[:9]
        return most_frequent
        
        # Normalize values
        c.max_ = max(freq.values())
        c.min_ = min(freq.values())

        for word, value in freq.iteritems():
            freq[word] = CLASS_NAMES[norm(value, c.min_, c.max_) - 1]

        # Sort alphabetically
        c.sorted_words = sorted(freq.items())

        # return c.sorted_words
        return render('/wordcloud.mako')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
