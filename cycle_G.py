class Point:    #Модуль округленя чисел
    def __init__(self, var):
        self.var = var
    def del_point(self):
        if float(self.var) == int(float(self.var)):
            self.var = int(float(self.var))
        else:
            self.var = round(float(self.var),3)
        return self.var

cycle = input('Введите цикл:\n')

if 'CYCLE' in cycle:    #Если введен цикл Siemens
    cycle = cycle.replace('(',',')
    cycle = cycle.replace(')','')
    cycle = cycle.split(',')
    
    for parametr in cycle[1:]:    #Проверка на наличие "нечисел"
        try:
            if type(int(float(parametr))) == int:
                pass
        except ValueError:
            if parametr == '':
                pass
            else:
                print('Ошибка: неверные параметры.')
                exit()
    
    p1 = cycle[1]
    p2 = cycle[2]
    p3 = cycle[3]
    p4 = cycle[4]
    p5 = cycle[5]
    p6 = cycle[6]
    p7 = cycle[7]
    p8 = cycle[8]
    p9 = cycle[9]
   
    #Объявление переменных 
    g_cycle =0
    axis = 0
    g_axis = 0
    fanuc = 0
    h = 0
    r = float(p3) + float(p2)
    
    if p9 == '12':    #Проверка наличия необходимых параметров
        h = float(p4)
    elif p9 == '11':
        h = float(p2) + float(p5)
    elif p4 != '' and p5 == '':
        h = p4
    elif p4 == '' and p5 != '':
        h = float(p2) + float(p5)
    else:
        print('Ошибка: проверьте параметры P4, P5 и P9.')
        exit()
    
    #Запуск модуля округленя
    r_point = Point(r)
    R = r_point.del_point()
    
    h_point = Point(h)
    H = h_point.del_point()
    
    p1_point = Point(p1)
    P1 = p1_point.del_point()
    
    def siemens():    #Фунцуия вывода цикла Fanuc
        if p8 == '1':    #Определение плоскости
            axis = 'Z'
            g_axis = 'G17'
        elif p8 == '2':
            axis = 'Y'
            g_axis = 'G18'
        elif p8 == '3':
            axis = 'X'
            g_axis = 'G19'
        else:
            print('Ошибка: проверьте параметр P8.')
            exit()
        #Определение наличия параметра P    
        if p6 != '' and p6 != '0': 
            fanuc = f'\nFANUC:\n{g_axis} G0 {axis}{P1}\nG82 {axis}{H} R{R} P{p6} F200'
        elif p6 == '' or p6 == '0':
            fanuc = f'\nFANUC:\n{g_axis} G0 {axis}{P1}\nG81 {axis}{H} R{R} F200'
        return fanuc
    print(siemens())    #Вывод Фунцуии
    
elif 'G' in cycle[0]:    #Если введен цикл Fanuc

    #cycle = cycle.replace('\n',' ')
    cycle = cycle.split(' ')
    
    g_axis = cycle[0]
    axis_depth = cycle[2]
    #axis = axis_depth[0]
    depth = axis_depth[1:]
    g_cycle = cycle[3]
    h = cycle[4]
    h = h[1:]
    r = cycle[5]
    r = r[1:]
    p7 = 0
    p8 = 0
    p9 = 0
    siemens = 0
        
    def fanuc():
        
        if g_axis.upper() == 'G17':
            p8 = 1
        elif g_axis.upper() == 'G18':
            p8 = 2
        elif g_axis.upper() == 'G19':
            p8 = 3    
        else:
            print('Ошибка: проверьте правильность ввода плоскости.')
            
        if g_cycle.upper() == 'G81':
            regime = 'CYCLE81'
            p6 = 0
            siemens = f'{regime}({depth}, {p6}, {p7}, {p8}, )'
            return siemens
        
        elif g_cycle.upper() == 'G82':
            p = cycle[6]
            p6 = p[1:]
            regime = 'CYCLE82'
            siemens = f'{regime}({depth}, {p6}, {p7}, {p8}, )'
            return siemens
        
    print(fanuc())
        #G17 G0 Z100 
        #G82 Z90 R2 P1 F200


else:
    print('Ошибка: неизвестный цикл.')
    exit()
