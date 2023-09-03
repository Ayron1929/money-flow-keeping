from init import getDate, init
month_name, year_name, last_month_name = getDate()
from input import window_interact
from output import pdf_generate

# 换成自己的银行账户
konto = ['账户1', '账户2', '账户3']

# 把 < month_name > 替换成 < last_month_name > 就可以记录和生成上个月的流水
option = month_name

# 类别
kata = ['住宅', '交通', '娱乐', '餐饮', '旅游', '购物', '保险', '运动', '教育', '杂货', '日常开支', '礼物', '工资']


csv_file = f'{year_name}_{option}.csv'
output_file = f'{year_name}_{option}'
pdf_title = f'{year_name} {option}'

init(csv_file)
input_done = False
window_interact(csv_file, konto, kata)
input_done = True
if input_done == True:
    pdf_generate(output_file, pdf_title)
