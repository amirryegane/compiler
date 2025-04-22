import ply.lex as lex
import ply.yacc as yacc

#کتاب خانه های لازم را وارد کد میکنیم

tokens = (
    'NUMBER',
)

t_ignore = '\t' # اگه فاصلع یا فضای هالی دیدی نادیدع بگیر

#شناخت اغداد صحیح
def t_NUMBER(t): # مقادیر معتبر که میتوان وارد کرد
    r'\d+' # regex = digits +0 -> 9
    t.value = int(t.value)
    return t



def t_error(t):
    print(f"کاراکتر نامعتبر: {t.value[0]}")
    t.lexer.skip(1)
#t.value[0]: اولین کاراکتر ناشناخته رو چاپ می‌کنه.
#اون کاراکتر رو نادیده می‌گیره و lexer می‌ره سراغ کاراکتر بعد

#making lexer 
lexer = lex.lex()

#تغریف قواغد
def p_start(p):
    '''start : NUMBER'''  #بع طور حلاصع اگه کاربر هر غددی وارد کند lex میگه عدده و پارسر هم میگه چون شروغ با عدد بوده(number ) و این یک توکن معتبر هست پارسر اونو پارس میکنه
    if p[1]%2== 0:
        print(f"{p[1]} zooj ast")
    else:
        print(f"{p[1]} fard ast")

def p_error(p):
    print("syntax error") # مدیریت خظا در پازسر

#making parser 
parser = yacc.yacc()

#run proggram

while True:
    try:
        line = input("enter num (for exit ctrl+c): ")
    except EOFError :# End Of File Error  وقتی ورودی تموم میشع این هطا رخ میده
        break
    if not line:
        continue
    parser.parse(line)    

