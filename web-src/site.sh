pandoc -s -S --toc syllabus.md --filter=pandoc-citeproc -o ../index.html
pandoc -s -S schedule.md --filter=pandoc-citeproc -o ../instruction-notes.html
