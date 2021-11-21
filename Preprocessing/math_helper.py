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
        m = helper.find_m(symbol_vertices,0 ,1)
        b = helper.find_b(symbol_vertices, 1, m)
        return (m,b)    

    def share_line(symbol_vertices, m, b, limit)->bool:
        x1, y1 = symbol_vertices[0].x, symbol_vertices[0].y
        return y1 - (m*x1 + b) < limit

    def is_space_here(symbol)->bool:
        return symbol.property.detected_break.type_ != 0
