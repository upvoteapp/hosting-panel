from make_html import parse_all_js_css
import os

def compile():
    os.system('npm run build')
    parse_all_js_css()

if __name__ == '__main__':
    compile()