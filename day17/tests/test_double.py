import pytest



def double(a):
    try:
        if a >= 0:
           return a * 2
    except  TypeError :
        print('TypeError')

@pytest.mark.int
def test_double_int():
    assert 2 == double(1)
@pytest.mark.int
def test_double1_minus():
    assert -2 == double(-1)
@pytest.mark.int
def test_double_float():
    assert 0.2 == double(0.1)
@pytest.mark.skip(reason='这是一个浮点数')
@pytest.mark.int
def test_double2_minus():
    assert -0.2 == double(-0.1)
@pytest.mark.zero
def test_double_0():
    print('方法中设置跳过用例')
    pytest.skip('跳过a为0')
    # 测试被跳过，断言不被执行
    assert 0 == double(0)

# @pytest.mark.xfail
@pytest.mark.bignum
def test_double_bignum():
    with pytest.raises(ValueError,match='TypeError'):
        raise ValueError('TypeError')


