#!/usr/bin/env python3


from sys import argv
from os import system
deps = {
        'pdftotext':'poppler-utils',
    'espeak':'espeak'
}
missingdeps = []

def show_usage():
    print('arguments manquant  !')
    print(f"utilisation:\n{argv[0]} fichier_source fichier_dest ")

def check_args():
    if not len(argv) < 3:
        return True
    show_usage()
    return False
    


def check_dep(name):
    """Check whether `name` is on PATH."""
    from distutils.spawn import find_executable
    match = find_executable(name) is not None
    #print(f'found {name} executable')
    return match

def install_dep(name):
    if check_dep('apt'):
        system(f'sudo apt install {name}')
        return True
    print(f'cant\'t install dependency :{name}\n\'apt\' is missing')
    return False

def check_deps(deps):
    results = {}
    for dep in deps:
        results[dep] = check_dep(dep)
    return results

def pdf2text(source):
    tempname = 'temp123.txt'
    system(f'pdftotext {source} {tempname}')
    return tempname

def texttosound(source,destination):
    system(f'espeak -a 80 -v fr+f2 -f {source} -w {destination}')

def pdf2sound(source,destination):
    tempfile = pdf2text(source)
    texttosound(tempfile,destination)
    system(f'rm {tempfile}')
    return True

#print('checking dependencies')
deps_infos = check_deps(deps)
mdeps = []

for dep in deps_infos:
    if deps_infos[dep] == False:
        missingdeps[dep] = deps[dep]

for dep in missingdeps:
    if install_dep(deps[dep]) == False:
        mdeps.append(dep)

missingdeps = mdeps

if len(missingdeps):
    print('program can\'t start, you have missing dependencies')
    [print(f"missing:{name}") for name in missingdeps]
else:
    #print('startup check  [ - OK  ] ')
    if(check_args()):
        source = argv[1]
        destination = argv[2]
        if pdf2sound(source,destination):
            print('success')
        else:
            print('failed')
    else:
        print('failed for unknown reasons yet')
