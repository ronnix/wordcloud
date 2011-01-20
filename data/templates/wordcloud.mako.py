# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1295541593.364965
_template_filename='/Users/ronan/dev/agileopen/wordcloud/wordcloud/wordcloud/templates/wordcloud.mako'
_template_uri='/wordcloud.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<ul class="wordcloud">\n')
        # SOURCE LINE 2
        for word, freq_class in c.sorted_words:
            # SOURCE LINE 3
            __M_writer(u'    <li class="')
            __M_writer(escape(freq_class))
            __M_writer(u'">')
            __M_writer(escape(word))
            __M_writer(u'</li>\n')
            pass
        # SOURCE LINE 5
        __M_writer(u'</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


