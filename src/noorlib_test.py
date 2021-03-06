#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Test noorlib.py module."""


import unittest

from src import dummy_requests
from src import noorlib
from src.noorlib import noorlib_sfn_cit_ref


class NoorlibTest(unittest.TestCase):

    def test_nl1(self):
        i = 'http://www.noorlib.ir/View/fa/Book/BookView/Image/6120'
        o = noorlib_sfn_cit_ref(i)
        e = (
            '* {{cite book '
            '| last=رشید یاسمی '
            '| first=غلامرضا '
            '| last2=کریستن سن '
            '| first2=آرتور امانویل '
            '| title=ایران در زمان ساسانیان: تاریخ ایران ساسانی تا'
            ' حمله عرب و وضع دولت و ملت در زمان ساسانیان '
            '| publisher=دنیای کتاب '
            '| publication-place=تهران - ایران '
            '| series=ایران در زمان ساسانیان: تاریخ ایران ساسانی تا'
            ' حمله عرب و وضع دولت و ملت در زمان ساسانیان '
            '| volume=1 '
            '| year=1368 '
            '| url=http://www.noorlib.ir/View/fa/Book/BookView/Image/6120 '
            '| language=فارسی '
            '| ref=harv '
            '| access-date='
        )
        self.assertIn(e, o[1])

    def test_nl2(self):
        """The year parameter is not present."""
        i = 'http://www.noorlib.ir/View/fa/Book/BookView/Image/18454'
        o = noorlib_sfn_cit_ref(i)
        self.assertIn('{{sfn | کورانی | p=}}', o[0])
        self.assertIn(
            '* {{cite book '
            '| last=کورانی '
            '| first=علی '
            '| title=المعجم الموضوعی لاحادیث '
            'الامام المهدی عجل الله تعالی فرجه الشریف '
            '| publisher=دار المرتضی '
            '| publication-place=بيروت '
            '| series=المعجم الموضوعي لإحادیث'
            ' الإمام المهدي (عجل الله فرجه الشریف) '
            '| volume=1 '
            '| url=http://www.noorlib.ir/View/fa/Book/BookView/Image/18454 '
            '| language=عربی '
            '| ref=harv '
            '| access-date=',
            o[1],
        )


noorlib.requests_get = dummy_requests.DummyRequests().get
if __name__ == '__main__':
    unittest.main()
