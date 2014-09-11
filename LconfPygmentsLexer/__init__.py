""" (c) 2014 `peter1000` https://github.com/peter1000
All Rights Reserved

LconfPygmentsLexer is distributed under the terms of the BSD 3-clause license.
Consult LICENSE.rst or http://opensource.org/licenses/BSD-3-Clause.
"""
# noinspection PyProtectedMember
from LconfPygmentsLexer._version import get_versions
__version__ = get_versions()['version']
del get_versions

SHORT_VERSION = __version__.rsplit('.', 1)[0]

TESTED_HOST_OS = 'Linux Ubuntu 13.10'

__project_name__ = 'LconfPygmentsLexer'
__title__ = "A simple pygments lexer for LCONF."
__author__ = '`peter1000` https://github.com/peter1000'
__copyright__ = '(c) 2014 ' + __author__
__license__ = 'BSD 3-clause license: Consult LICENSE.rst'
