import sys, zipfile, re
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def para_text(p):
    parts=[]
    for node in p.iter():
        if node.tag==W+'t':
            parts.append(node.text or '')
        elif node.tag==W+'tab':
            parts.append('\t')
        elif node.tag==W+'br':
            parts.append('\n')
    return ''.join(parts)

def walk(el, out):
    for child in el:
        if child.tag==W+'p':
            t=para_text(child).strip()
            style=''
            pPr=child.find(W+'pPr')
            if pPr is not None:
                ps=pPr.find(W+'pStyle')
                if ps is not None: style=ps.get(W+'val') or ''
                if pPr.find(W+'numPr') is not None: style=style+'+LIST'
            if t:
                out.append(('[%s] '%style if style else '')+t)
        elif child.tag==W+'tbl':
            out.append('--- TABLE ---')
            for tr in child.findall(W+'tr'):
                cells=[]
                for tc in tr.findall(W+'tc'):
                    sub=[]
                    walk(tc, sub)
                    cells.append(' / '.join(x for x in sub if x!='--- TABLE ---' and x!='--- END TABLE ---'))
                out.append(' || '.join(cells))
            out.append('--- END TABLE ---')
        else:
            walk(child, out)

for path in sys.argv[1:]:
    print('#'*80)
    print('# FICHIER :', path)
    print('#'*80)
    z=zipfile.ZipFile(path)
    root=ET.fromstring(z.read('word/document.xml'))
    out=[]
    walk(root, out)
    print('\n'.join(out))
