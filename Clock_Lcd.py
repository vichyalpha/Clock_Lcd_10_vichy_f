from mcje.minecraft import Minecraft
import param_MCJE as param
import datetime
import time

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('This is a clock made with LCDfont and transferred to mincraft world')

mc.setBlock(5, 70, 5,  param.GOLD_BLOCK)

LCD_0 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 1,
         1, 0, 1, 0, 1,
         1, 1, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_1 = (0, 0, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0)

LCD_2 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1)

LCD_3 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 1, 1, 0,
         0, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)

LCD_4 = (0, 0, 1, 0, 0,
         0, 1, 1, 0, 0,
         1, 0, 1, 0, 0,
         1, 0, 1, 0, 0,
         1, 1, 1, 1, 1,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,)

LCD_5 = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)

LCD_6 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)

LCD_7 = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,)

LCD_8 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)

LCD_9 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 1,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,)

LCD_10 = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 1, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,)

LCD_11 = (0, 0, 0, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 0, 0, 0,)

LCD_font_styles = (LCD_0, LCD_1, LCD_2,LCD_3,LCD_4,LCD_5,LCD_6,LCD_7,LCD_8,LCD_9,LCD_10,LCD_11)

def update_col( col=0, code=2):
    i = 34
    for y in range(7):
        for x in range(5):
            if  LCD_font_styles[int(code)][i]  == 1:
                mc.setBlock(-x + col*8, y+40, 5,  param.GOLD_BLOCK)
            else:
                mc.setBlock(-x + col*8, y+40, 5,  param.AIR)
            i -= 1

def update_col1( col=0, code=2):
    i = 34
    for y in range(7):
        for x in range(5):
            if  LCD_font_styles[int(code)][i]  == 1:
                mc.setBlock(-x + col*8, y+20, 5,  param.GOLD_BLOCK)
            else:
                mc.setBlock(-x + col*8, y+20, 5,  param.AIR)
            i -= 1

running = True
while running:
    
    date = datetime.datetime.now()
    update_col(col= 0, code= date.hour//10)
    update_col(col= 1, code= date.hour%10)
    update_col(col= 2, code= 11)
    update_col(col= 3, code= date.minute//10)
    update_col(col= 4, code= date.minute%10)
    update_col(col= 5, code= 11)
    update_col(col= 6, code= date.second//10)
    update_col(col= 7, code= date.second%10)
    update_col1(col= 0, code= date.year//1000%10)
    update_col1(col= 1, code= date.year//100%10)
    update_col1(col= 2, code= date.year//10%10)
    update_col1(col= 3, code= date.year%10)
    update_col1(col= 4, code= 10)
    update_col1(col= 5, code= date.month//10)
    update_col1(col= 6, code= date.month%10)
    update_col1(col= 7, code= 10)
    update_col1(col= 8, code= date.day//10)
    update_col1(col= 9, code= date.day%10)
    time.sleep(0.1)