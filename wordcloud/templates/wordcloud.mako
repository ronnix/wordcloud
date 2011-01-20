<ul class="wordcloud">
% for word, freq_class in c.sorted_words:
    <li class="${freq_class}">${word}</li>
% endfor
</ul>
