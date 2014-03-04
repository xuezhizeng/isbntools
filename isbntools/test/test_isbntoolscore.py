#!/usr/bin/env python
# -*- coding: utf-8 -*-


from nose.tools import assert_equals, assert_raises
from ..isbntoolscore import _check_digit10, _check_digit13, _check_structure10, _check_structure13, is_isbn10, is_isbn13, to_isbn10, to_isbn13, canonical, clean, notisbn, get_isbnlike, get_canonical_isbn, mask
from ..data.data4tests import ISBNs


# nose tests

# def test__check_digit10(firstninedigits):
#     pass


# def test__check_digit13(firsttwelvedigits):
#     return


# def test__check_structure10(isbn10like):
#     return


# def test__check_structure13(isbn13like):
#     return


def test_is_isbn10():
    assert_equals(is_isbn10('0826497527'), True)
    assert_equals(is_isbn10('0826497520'), False)


def test_is_isbn13():
    assert_equals(is_isbn13('9780826497529'), True)
    assert_equals(is_isbn13('9791090636071'), True)
    assert_equals(is_isbn13('9780826497520'), False)


def test_to_isbn10():
    assert_equals(to_isbn10('9780826497529'), '0826497527')
    assert_equals(to_isbn10('9780826497520'), '0826497527')  # ISBN13 not valid


def test_to_isbn13():
    assert_equals(to_isbn13('0826497527'), '9780826497529')
    assert_equals(to_isbn13('0826497520'), '9780826497529')  # ISBN10 not valid


def test_clean():
    assert_equals(clean(' 978.0826.497529'), '9780826497529')
    assert_equals(clean('ISBN: 9791090636071'), 'ISBN 9791090636071')
    assert_equals(clean('978,0826497520'), '9780826497520')


def test_notisbn():
    assert_equals(notisbn('0826497527'), False)
    assert_equals(notisbn('0826497520'), True)
    assert_equals(notisbn('9780826497529', level='strict'), False)
    assert_equals(notisbn('978082649752', level='strict'), True)
    assert_equals(notisbn('978082649752', level='loose'), True)
    assert_equals(notisbn('9780826400001', level='loose'), False)
    assert_equals(notisbn('9780826400001', level='strict'), True)
    assert_equals(notisbn('978 9426497529'), True)
    assert_equals(notisbn('9789426497529'), True)
    assert_equals(notisbn('979 10 9063607 1'), False)
    assert_equals(notisbn('9780826497520'), True)


def test_get_isbnlike():
    assert_equals(len(get_isbnlike(ISBNs)), 79)
    assert_equals(len(get_isbnlike(ISBNs, 'normal')), 79)
    assert_equals(len(get_isbnlike(ISBNs, 'strict')), 69)
    assert_equals(len(get_isbnlike(ISBNs, 'loose')), 81)
    assert_equals(get_isbnlike(ISBNs, 'e'), None)
    # assert_raises(TypeError, len(get_isbnlike(ISBNs, 'e')))


# def test_isbn_stdin_validate():
#     pass


def test_get_canonical_isbn():
    assert_equals(get_canonical_isbn('0826497527', output='bouth'),
                  '0826497527')
    assert_equals(get_canonical_isbn('0826497527'), '0826497527')
    assert_equals(get_canonical_isbn('0826497527', output='isbn-10'),
                  '0826497527')
    assert_equals(get_canonical_isbn('0826497527', output='isbn-13'),
                  '9780826497529')
    assert_equals(get_canonical_isbn('ISBN 0826497527', output='isbn-13'),
                  '9780826497529')
    assert_equals(get_canonical_isbn('0826497520'), None)
    assert_equals(get_canonical_isbn('9780826497529'), '9780826497529')
    assert_equals(get_canonical_isbn('9780826497520'), None)


def test_canonical():
    assert_equals(canonical('ISBN 9789720404427'), '9789720404427')
    assert_equals(canonical('ISBN-9780826497529'), '9780826497529')
    assert_equals(canonical('ISBN9780826497529'), '9780826497529')
    assert_equals(canonical('isbn9780826497529'), '9780826497529')
    assert_equals(canonical('isbn 0826497527'), '0826497527')


def test_mask():
    assert_equals(mask('5852700010'), '5-85270-001-0')
    assert_equals(mask('0330284983'), '0-330-28498-3')
    assert_equals(mask('3796519008'), '3-7965-1900-8')
    assert_equals(mask('4198301271'), '4-19-830127-1')
    assert_equals(mask('2226052577'), '2-226-05257-7')
    assert_equals(mask('6053840572'), '605-384-057-2')
    assert_equals(mask('7301102992'), '7-301-10299-2')
    assert_equals(mask('8085983443'), '80-85983-44-3')
    assert_equals(mask('9056911872'), '90-5691-187-2')
    assert_equals(mask('9500404427'), '950-04-0442-7')
    assert_equals(mask('9800101942'), '980-01-0194-2')
    assert_equals(mask('9813018399'), '981-3018-39-9')
    assert_equals(mask('9786001191251'), '978-600-119-125-1')
    assert_equals(mask('9780321534965'), '978-0-321-53496-5')
    assert_equals(mask('9781590593561'), '978-1-59059-356-1')
    assert_equals(mask('9789993075899'), '978-99930-75-89-9')
    assert_equals(mask('0-330284983'), '0-330-28498-3')
    assert_equals(mask('9791090636071'), '979-10-90636-07-1')
    assert_equals(mask(''), None)
