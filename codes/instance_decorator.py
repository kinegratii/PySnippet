# coding=utf8


class App(object):

    def __init__(self, app_id):
        self.app_id = app_id

    def inject(self, func):
        def _dec(*args, **kwargs):
            context = func(*args, **kwargs)
            context['app_id'] = self.app_id
            return context
        return _dec

    def inject_with_args(self, **kw):
        def _inject(func):
            def _dec(*args, **kwargs):
                context = func(*args, **kwargs)
                context.update(kw)
                return context
            return _dec
        return _inject

app = App(2)

# app.inject()()


@app.inject
def get_context():
    context = {'name': 'demo'}
    return context


@app.inject_with_args(app_id=6)
def get_context2():
    context = {'name': 'demo'}
    return context


def main():
    """
       >>> get_context()
       {'name': 'demo', 'app_id': 2}
       >>> get_context2()
       {'name': 'demo', 'app_id': 6s}
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
