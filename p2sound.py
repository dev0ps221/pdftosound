#!/usr/bin/env python3
#THIS IS FOR LINUX USERS
#
#
#DEPENDENCIES
#poppler-utils
#espeak
#
#reference:
#" 
#  pdftotext ebook.pdf ebook.txt
#  espeak -f ebook.txt -w ebook_audio.wav
#"
#from reddit conversation:https://www.reddit.com/r/linux4noobs/comments/cmo2i4/whats_a_good_linux_pdf_app_that_can_read_pdfs/
#
#


deps = {
        'pdftotext':'',
    'espeak':'espeak'
}
missingdeps = []
def check_dep(name):
    """Check whether `name` is on PATH."""
    from distutils.spawn import find_executable
    return find_executable(name) is not None

def install_dep(name):

def check_deps(deps):
    results = {}
    for dep in deps:
        results[dep] = check_dep(dep)
    return results


