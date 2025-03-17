import hello
def test_hello():
  assert hello.hello () == "hello world"
 
if __name__ == "__main__":
     import pytest
     pytest.main()