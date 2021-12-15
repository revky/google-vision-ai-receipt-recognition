class MathHelper:
    def find_m(symbol_cords, i, j)-> float:
        x1,y1 = symbol_cords[i].x, symbol_cords[i].y
        x2,y2 = symbol_cords[j].x, symbol_cords[j].y
        y_sub = y2-y1
        x_sub = x2-x1
        result = y_sub / x_sub if x_sub != 0 else 0
        return result
        
    def find_b(symbol_cords,i,m)-> float:
        b = - (m * symbol_cords[i].x - symbol_cords[i].y)
        return b

    def find_linear_parameters(symbol_cords)-> tuple:
        helper = MathHelper
        m = helper.find_m(symbol_cords, 3,2)
        b = helper.find_b(symbol_cords, 2, m)
        return (m,b)    

    def if_share_line(symbol_cords, m, b)->bool:
        x1, y1 = symbol_cords[3].x, symbol_cords[3].y
        return y1 - (m*x1 + b) < 8
