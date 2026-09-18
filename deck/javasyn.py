"""javasyn.py — tiny Java syntax highlighter (VS Code Dark+ inspired).

Emits HTML spans used inside the fake IDE windows of the deck.
It is intentionally small: it only needs to colour the fixed snippets
that appear in the presentation, but it is a real tokeniser, not a
per-snippet lookup table.
"""
import html
import re

# storage / declaration keywords  -> blue
DECL = {
    "public", "private", "protected", "static", "final", "abstract", "class",
    "interface", "enum", "record", "extends", "implements", "import", "package",
    "throws", "void", "int", "long", "short", "byte", "char", "boolean",
    "float", "double", "synchronized", "volatile", "transient", "native",
    "strictfp", "default",
}
# control-flow / literal keywords -> purple
KW = {
    "new", "return", "if", "else", "for", "while", "do", "switch", "case",
    "break", "continue", "try", "catch", "finally", "throw", "instanceof",
    "this", "super", "null", "true", "false", "var", "yield", "assert",
}
# well known JDK types -> teal
TYPES = {
    "String", "Integer", "Long", "Double", "Float", "Boolean", "Byte", "Short",
    "Character", "Object", "System", "List", "ArrayList", "LinkedList", "Map",
    "HashMap", "Set", "HashSet", "WeakHashMap", "Thread", "Math", "Arrays",
    "Collections", "Exception", "RuntimeException", "OutOfMemoryError", "Error",
    "StringBuilder", "Optional", "Stream", "Runtime", "Class", "MemoryMXBean",
    "JVM", "GarbageCollector", "SoftReference", "WeakReference", "Reference",
}

_CLS = "t-cls"
_CST = "t-cst"
_KW = "t-kw"
_MTD = "t-mtd"
_STR = "t-str"
_NUM = "t-num"
_CMT = "t-cmt"
_VAR = "t-var"

TOKEN = re.compile(
    r'("(?:\\.|[^"\\])*")'          # 1 string
    r"|(\b\d[\d_]*(?:\.[\d_]+)?[fFdDlL]?\b)"  # 2 number
    r"|(@[A-Za-z_]\w*)"             # 3 annotation
    r"|([A-Za-z_$][\w$]*)",         # 4 identifier
)


def _comment_index(line: str) -> int:
    """Index of a real `//` comment start (ignores `//` inside strings)."""
    in_str = False
    esc = False
    for i, ch in enumerate(line):
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = True
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if not in_str and ch == "/" and line[i:i + 2] == "//":
            return i
    return -1


def hl_line(line: str, vars_=(), classes=()) -> str:
    """Return HTML for one line of Java source."""
    cut = _comment_index(line)
    if cut >= 0:
        code, comment = line[:cut], line[cut:]
    else:
        code, comment = line, ""

    extra_cls = set(classes)
    known_vars = set(vars_)

    out = []
    pos = 0
    for m in TOKEN.finditer(code):
        if m.start() > pos:
            out.append(html.escape(code[pos:m.start()]))
        word = m.group(0)
        if m.group(1):
            out.append(f'<span class="{_STR}">{html.escape(word)}</span>')
        elif m.group(2):
            out.append(f'<span class="{_NUM}">{html.escape(word)}</span>')
        elif m.group(3):
            out.append(f'<span class="{_CST}">{html.escape(word)}</span>')
        else:
            rest = code[m.end():]
            nxt = rest.lstrip()[:1]
            if word in DECL:
                cls = _CST
            elif word in KW:
                cls = _KW
            elif nxt == "(":
                # constructor / method call: keep Capitalised names class-coloured
                cls = _CLS if (word[0].isupper() or word in TYPES or word in extra_cls) else _MTD
            elif word in TYPES or word in extra_cls:
                cls = _CLS
            elif word in known_vars:
                cls = _VAR
            elif word[0].isupper():
                cls = _CLS
            else:
                cls = None
            if cls:
                out.append(f'<span class="{cls}">{html.escape(word)}</span>')
            else:
                out.append(html.escape(word))
        pos = m.end()
    if pos < len(code):
        out.append(html.escape(code[pos:]))
    if comment:
        out.append(f'<span class="{_CMT}">{html.escape(comment)}</span>')
    return "".join(out)


def hl_code(source: str, vars_=(), classes=()) -> list:
    """Return a list of highlighted HTML lines for a whole snippet."""
    return [hl_line(l, vars_=vars_, classes=classes) for l in source.split("\n")]


if __name__ == "__main__":  # tiny self-test
    demo = [
        'public class GarbageDemo {',
        '',
        '    public static void main(String[] args) {',
        '        User user = new User("Oussama"); // created on the heap',
        '        user = null; // object becomes unreachable',
        '        System.gc();',
        '        int age = 20;',
        '        static List<byte[]> cache = new ArrayList<>();',
        '    }',
        '}',
    ]
    for l in hl_code("\n".join(demo), vars_=("user", "age", "args", "cache")):
        print(l)