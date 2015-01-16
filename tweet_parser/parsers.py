#coding=utf8

import re

class TweetParser(object):
    
    user_at_fmt = '@{u} '
    user_url_fmt = '/home/{u}/'

    em_at_fmt = '[{e}]'
    em_url_fmt = '/static/tweets/em/{e}.gif'
    em_limit = 4

    def __init__(self, name_list, em_list):
        self.word_dict = {}
        self._add_user(name_list)
        self._add_em(em_list)
        self._reset()

    def _add_user(self, name_list):
        user_word_dict = {self.user_at_fmt.format(u=u):self.node('a',content=self.user_at_fmt.format(u=u), href=self.user_url_fmt.format(u=u)) for u in name_list}
        self.word_dict.update(user_word_dict)

    def _add_em(self, em_list):
        if self.em_limit != 0:
            em_word_dict = {self.em_at_fmt.format(e=e):self.node('img',src=self.em_url_fmt.format(e=e)) for e in em_list}
            self.word_dict.update(em_word_dict)

    def pre_replace(self, src_word, dst_word):
        if src_word[0] == '[':
            if self.em_limit > 0:
                if self.em_count > self.em_limit:
                    return src_word
                self.em_count += 1
        elif src_word[0] == '@':
            self._user_set.add(src_word[1:-1])
    
    def parse(self, text):
        self._reset()
        return self._replace_word(text, self.word_dict) if text and self.word_dict else text

    @property
    def user_set(self):
        return self._user_set

    def _reset(self):
        self.em_count = 0
        self._user_set = set()

    def _replace_word(self, text,  word_dict):
        yo = re.compile('|'.join(map(re.escape, word_dict)))
        def translate(mat):
            src_word = mat.group(0)
            dst_word = word_dict[src_word]
            return self.pre_replace(src_word, dst_word) or dst_word
        return yo.sub(translate, text)

    def node(self, name, content=None, **kwargs):
        def _flat(value):
            if isinstance(value, dict):
                return ''.join(['{0}:{1};'.format(k,v) for k,v in value.items()])
            return ' '.join(value) if isinstance(value, (tuple, list, set)) else value
        attrs = ' '.join('{0}="{1}"'.format(k, _flat(v)) for k,v in kwargs.items() if _flat(v))
        return '<{0} {1}>{2}</{0}>'.format(name, attrs, content) if content else '<{0} {1}/>'.format(name, attrs)


def main():
    p = TweetParser(['admin', 'haha'],['em_1','em_2'])
    print p.node('a',content='admin', href='http://adddd', **{'class':['osc','github']})
    print p.node('img', src='/static/img/arclist/1.gif', alt='haha', style={'font-size':'12px','color':'#999999'}, **{'class':['osc','github']})
    text = '@admin this is a test [em_1][em_1][em_1][em_1][em_1][em_1]'
    print p.parse(text)
    print p.user_set

if __name__ == '__main__':
    main()