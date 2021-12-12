class MathHelper:
    def find_m(symbol_vertices, i, j)-> float:
        x1,y1 = symbol_vertices[i].x, symbol_vertices[i].y
        x2,y2 = symbol_vertices[j].x, symbol_vertices[j].y
        y_sub = y2-y1
        x_sub = x2-x1
        result = y_sub / x_sub if x_sub != 0 else 0
        return result
        
    def find_b(symbol_vertices,i,m)-> float:
        b = - (m * symbol_vertices[i].x - symbol_vertices[i].y)
        return b

    def find_linear_parameters(symbol_vertices)-> tuple:
        helper = MathHelper
        m = helper.find_m(symbol_vertices, 3,2)
        b = helper.find_b(symbol_vertices, 2, m)
        return (m,b)    

    def share_line(symbol_vertices, m, b, limit)->bool:
        x1, y1 = symbol_vertices[3].x, symbol_vertices[3].y
        return y1 - (m*x1 + b) < limit
