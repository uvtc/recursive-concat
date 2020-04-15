# recursive-concat

Recursively concatenate .txt or .md files in the current directory and below.

To install, copy recursive-concat.py to your ~/bin and make it executable:

    chmod +x ./recursive-concat.py

Usage: run the script in a directory containing .txt or .md files. Output
goes to stdout, so you'll usually pipe it to an output file located outside
the current directory:

    recursive-concat.py > ../all-one-page.txt


## Rationale

This is handy to use when you have a directory full of markdown-formatted
files which you'd like to process into one big output file. For example, to
create a pdf you might use [Pandoc](https://pandoc.org/), like so:

    pandoc all-one-page.txt -s -f markdown+smart \
        -o all-one-page.pdf -V geometry:"margin=0.6in" -V fontsize=12pt


## License

MIT. 2020, John Gabriele. See the accompanying LICENSE file.
