#!/usr/bin/env

import subprocess, os, random, copy

output_filename = "twelvetone_ex.ly"
output_file = open(output_filename, "w")

notes = ['c','cis','d','dis','e','f','fis','g','gis','a','ais','b']

temp_tt_array = []

def twelvetone_gen():
    notes_svd = copy.copy(notes)
    a = 11
    while len(temp_tt_array) < 12:
        r = random.randint(0,a)
        temp_tt_array.append(notes_svd[r])
        notes_svd.remove(notes_svd[r])
        a = a-1
    return temp_tt_array

output_file.write(r'''\version "2.16.0"\header{tagline=""}\paper{indent=0 line-width=130 top-margin=13}\layout{\context{\Staff \remove "Stem_engraver" \remove "Time_signature_engraver" \override Stem #'transparent = ##t}}\score{\transpose c c' << \new Staff''')

temp_tt_string = ''

for x in range(0, 16):
    output_file.write('\n' + r'{ \time 12/4 ')
    twelvetone_gen()
    for element in temp_tt_array:
        temp_tt_string+=element + ' '
    output_file.write(temp_tt_string)
    temp_tt_string = ''
    temp_tt_array = []
    output_file.write(r'\bar "||" }')

output_file.write('\n>>}')

output_file.close()

try:
    os.startfile(output_filename)
except AttributeError:
    subprocess.call(['open', output_filename])
