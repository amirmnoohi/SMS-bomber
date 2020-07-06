from .snappfood import Snappfood
from .snapptrip import Snapptrip
from .snapp import Snapp
from .tapsi import Tapsi
from .alibaba import Alibaba
from .divar import Divar
from .torob import Torob
from .zarinpal import Zarinpal
from .namava import Namava

Status = False

All = [
    ('snapp', Snapp(), Status | False),
    ('snappfood', Snappfood(), Status | False),
    ('snapptrip', Snapptrip(), Status | False),
    ('tapsi', Tapsi(), Status | False),
    ('alibaba', Alibaba(), Status | False),
    ('divar', Divar(), Status | False),
    ('torob', Torob(), Status | False),
    ('zarinpal', Zarinpal(), Status | False),
    ('namava', Namava(), Status | True),
]
