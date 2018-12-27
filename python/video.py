import os
import re

BYTE_RANGE_RE = re.compile(r'bytes=(\d+)-(\d+)?$')


def parse_byte_range(byte_range):
    """Returns the two numbers in 'bytes=123-456' or throws ValueError.

    The last number or both numbers may be None.
    """
    if byte_range.strip() == '':
        return None, None

    m = BYTE_RANGE_RE.match(byte_range)
    if not m:
        raise ValueError('Invalid byte range: {}'.format(byte_range))

    first, last = [x and int(x) for x in m.groups()]
    # if last and last < first:
    #     raise ValueError('Invalid byte range: {}'.format(byte_range))

    return first, last


class RangeRequestHandler:
    """Adds support for HTTP 'Range' requests to SimpleHTTPRequestHandler

    The approach is to:
    - Override send_head to look for 'Range' and respond appropriately.
    - Override copyfile to only transmit a range when requested.
    """

    def get(self, path, verbose=False):
        """Serve a GET request
        """
        self.verbose = verbose
        if self.verbose:
            print(self.headers)

        self.path = path
        self.file_size = None
        self.headers = []

        data = None
        if os.path.isfile(path):
            fp = self.send_file_head(path)
            try:
                data = self.copy_chunks(fp, self.wfile)
            finally:
                fp.close()

        return data

    def send_file_head(self, path):
        # Handle ranges
        if 'Range' in self.headers:
            try:
                self.range = parse_byte_range(self.headers['Range'])
            except ValueError:
                self.send_error(400, 'Invalid byte range')
                return None
        else:
            self.range = 0, None

        # Extract requested byte range
        first, last = self.range

        fp = None
        try:
            fp = open(path, 'rb')
        except IOError:
            self.send_error(404, 'File not found')
            return None

        fs = os.fstat(fp.fileno())
        if not self.file_size:
            self.file_size = fs[6]

        if first is None:
            raise ValueError('errrr need to figure out this part: {}'.format(self.range))

        if first >= self.file_size:
            # https://tools.ietf.org/html/rfc7233
            self.send_error(416, 'Requested byte range not satisfiable')
            return None

        if last is None:
            # Range end is unspecified, so server gets to decide.
            last = first + self.file_size  #1024*1024

        if last >= self.file_size:
            # Don't go past end of file
            last = self.file_size - 1

        # Update internal range values
        self.range = first, last

        response_length = last - first + 1

        try:
            self.send_header('Content-type', 'video/mpeg4')
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Range', 'bytes {}-{}/{}'.format(first, last, self.file_size))
            self.send_header('Content-Length', str(response_length))
            self.send_header('Last-Modified', self.date_time_string(fs.st_mtime))

            # Cache stuff, but doesn't appear to work woith range requests :(
            # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
            # https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching
            self.send_header('Cache-Control', 'public, max-age=31536000')
            return fp
        except:
            fp.close()
            raise

    def send_header(self, key, value):
        self.headers[key] = value

    def copy_chunks(self, src, dst):
        """Copy data from source file to destination file in little chunks.
        """
        buffer_size = 256*1024

        first, last = self.range  # defined earlier in method send_head()

        if last is None or last >= self.file_size:
            # This issue should have been handled earlier.
            raise ValueError('Unexpected range: {}'.format(self.range))
            # last = self.file_size - 1
            # self.range = first, last

        # Keep reading/writing until nothing left tot copy.
        position = first
        src.seek(first)
        while last - position + 1 > 0:
            # Read it
            buffer_read = min(buffer_size, last-position+1)
            data = src.read(buffer_read)
            if len(data) == 0:
                break

            # Count it
            position += len(data)

            # Write it
            try:
                dst.write(data)
            except ConnectionResetError as e:
                # print(e)
                # print(first, position, last)
                break

        # Finish
        bytes_copied = position - first + 1
        return bytes_copied


if __name__ == '__main__':
    pass
