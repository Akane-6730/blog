## ASCII
- In Python, the `chr()` function can be used to convert an ASCII ordinal number to a character (the `ord()` function does the opposite).

??? note "Example"
    ```python
    a = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    for i in range (0, len(a)):
        print(chr(a[i]),end='')
        # Output: crypto{ASCII_pr1nt4bl3}
    ```
## Hex
- In Python, the `bytes.fromhex()` function can be used to convert hex to bytes. The `.hex()` instance method can be called on byte strings to get the hex representation.
??? note "Example"
    ```python
    a=bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
    print(a)
    # Output: b'crypto{You_will_be_working_with_hex_strings_a_lot}'
    ```
## Base64
> - Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.
- Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

-  In Python, after importing the base64 module with `import base64`, you can use the `base64.b64encode()` function. 
??? note "Example"
    ```python
    import base64
    a=bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
    b=base64.b64encode(a)
    print(b)
    # Output: b'crypto/Base+64+Encoding+is+Web+Safe/'
    ```
## Bytes and Big Integers
> - Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?
- The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.
> ??? Abstract "To Illustrate"
      ```python
      message: HELLO
      ascii bytes: [72, 69, 76, 76, 79]
      hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
      base-16: 0x48454c4c4f
      base-10: 310400273487
      ```

- Python's PyCryptodome library implements this with the methods `bytes_to_long()` and `long_to_bytes()`. You will first have to install PyCryptodome and import it with `from Crypto.Util.number import *`.

??? note "Example"
    ```python
    from Crypto.Util.number import *
    message=11515195063862318899931685488813747395775516287289682636499965282714637259206269
    flag=long_to_bytes(message)
    print(flag)
    # Output: b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
    ```
## XOR
- The Python pwntools library has a convenient `xor()` function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.
??? note "Example1"
    ```python
    def xor_string_with_13(label):
        result = ""
        for char in label:
            xor_result = ord(char) ^ 13
            result += chr(xor_result)
        return result
    print(xor_string_with_13("label"))
    # Output: "aloha"
    ```
!!! abstract "four main properties"
    Commutative: A ⊕ B = B ⊕ A

    Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C

    Identity: A ⊕ 0 = A

    Self-Inverse: A ⊕ A = 0

    - Commutative means that the order of the XOR operations is not important.
    - Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). 
    - The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

??? note "Example2 sulution1"
    ```python
    from pwn import xor
    k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
    k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
    flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
    print(xor(k1,k2_3,flag))
    ```
??? note "Example2 sulution1"
    ```python
    FLAG = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ^ 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
    print(bytes.fromhex(hex(FLAG)[2:]))
    ```