"""Common data archiving and compression formats are
directly supported by modules including: zlib,
gzip, bz2, lzma, zipfile and tarfile."""
"""Module zlib 
The functions in this module allow compression and 
decompression using the zlib library, 
which is based on GNU zip."""
import zlib

s = b'witch which has which witches wrist watch'
print("len(s)", len(s))
print("s", s)

"""zlib. compress ( data, level=-1 )
Compresses the bytes in data, returning a bytes object 
containing compressed data."""
t = zlib.compress(s)
print("len(t)", len(t))
print("t", t)
"""Decompresses the bytes in data, returning a bytes object 
containing the uncompressed data."""
d = zlib.decompress(t)
print("d", d)
"""Computes a CRC (Cyclic Redundancy Check) checksum of data. 
The result is an unsigned 32-bit integer. If value is present, 
it is used as the starting value of the checksum; otherwise, a default value 
of 0 is used. Passing in value allows computing a running checksum 
over the concatenation of several inputs."""
c = zlib.crc32(s)
print('c', c)
