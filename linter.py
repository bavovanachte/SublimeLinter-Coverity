from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class __class__(Linter):
    cmd = '__cmd__'
    regex = (
        r'^[^<>:;,?\"*|\s]+:+(?P<line>\d+):+\s*CID\s*\d*'
    )
    multiline = True
    defaults = {
        'selector': 'source.c, source.h',
    }
