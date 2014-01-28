from nose import main
import foo

def test_adder():
    assert foo.adder(5,5) == 10

if __name__ == '__main__':
    main()
